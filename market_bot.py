from collections import deque
import copy
from datetime import timedelta
import hashlib
import logging
from Queue import Queue
import requests
from threading import Thread
import time

from expire_dict import DataCache
import config

logger = logging.getLogger('market_bot')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

BASE_URL = 'http://forum.toribash.com/'

session = requests.session()
#session.headers['User-Agent'] = 'Firefox 30.0'

logger.info("Logging in")
session.post(BASE_URL + 'login.php?do=login', {
    'vb_login_username':        config.username,
    'vb_login_password':        '',
    'vb_login_md5password':     hashlib.md5(config.password).hexdigest(),
    'vb_login_md5password_utf': hashlib.md5(config.password).hexdigest(),

    'cookieuser': 1, #stay logged in
    'do': 'login',
    's': '',
    'securitytoken': 'guest'
})
"""
session.post(BASE_URL + 'tori.php',{
    'username': config.username, 'password': config.password, 'submit': 'Login'
})
"""

logger.info("Downloading token")
token = session.get('http://forum.toribash.com/bank_ajax.php?bank_ajax=get_token').json()['token']

def token_updater():
    while True:
        time.sleep(3600)
        logger.info("Downloading token")
        try:
            token = session.get('http://forum.toribash.com/bank_ajax.php?bank_ajax=get_token').json()['token']
        except Exception as e:
            logger.exception(e)

def bump_worker(bump):
    while True:
        offset = 0
        logger.info("Bumping items")
        while True:
            try:
                data = session.get(BASE_URL + 'bank_ajax.php', params={
                    'bank_ajax': 'get_inventory',
                    'username': config.username,
                    'offset': offset,
                }).json()

                offset += data['inventory']['max_items_per_request']

                bump_items = [item for item in data['inventory']['items'] if item['is_for_sale']]

                for item in bump_items:
                    logger.debug("Bumping %s at %i (%i)", item['item_name'], item['sale_price'], item['inventid'])

                    session.get(BASE_URL + 'bank_ajax.php', params={
                        'bank_ajax': 'remove_market_item',
                        'inventid': item['inventid'],
                        'token': token
                    })
                    session.get(BASE_URL + 'bank_ajax.php', params={
                        'bank_ajax': 'add_market_item',
                        'inventid': item['inventid'],
                        'price': item['sale_price'],
                        'token': token
                    })

                if offset > data['inventory']['total_user_items']:
                    break
            except Exception as e:
                logger.exception(e)
                time.sleep(bump / 4)

        logger.info("Finished bumping items")
        time.sleep(bump)

def bank_ajax_worker():
    while True:
        jobs = bank_ajax_jobs.get()
        for job in jobs:
            session.get(BASE_URL + 'bank_ajax.php', params=job)
        bank_ajax_jobs.task_done()

check_pages_init = getattr(config, 'check_pages_init', 0)
check_pages      = getattr(config, 'check_pages', 0)

check_buy_items_init = getattr(config, 'check_buy_items_init')
check_buy_items      = getattr(config, 'check_buy_items')

intersperse_buy_items       = getattr(config, 'intersperse_buy_items')
intersperse_buy_items_pages = getattr(config, 'intersperse_buy_items_pages', 1)

buy_item_if_not_sellable = getattr(config, 'buy_item_if_not_sellable')

check_sets = getattr(config, 'check_sets')

auto_buy = getattr(config, 'auto_buy', 0)

test_run = getattr(config, 'test_run', False)
bump     = getattr(config, 'bump')

buy_items_keys = config.buy_items.keys()
most_expensive_buy_item = max(config.buy_items.itervalues())

# Don't check an item for a minute after we found it once
items_cache = DataCache(timedelta(0, 3600))
items_prices_cache = DataCache(timedelta(0, 1800))

bank_ajax_jobs = Queue()
market_jobs = deque()

if check_pages_init < 0:
    market_jobs.append({'all_pages': True})
else:
    for page in range(1, config.check_pages_init + 1):
        market_jobs.append({'page': page})

if bump:
    bump_thread = Thread(target=bump_worker, args=(bump,))
    bump_thread.daemon = True
    bump_thread.start()

token_thread = Thread(target=token_updater)
token_thread.daemon = True
token_thread.start()

for i in xrange(10):
    t = Thread(target=bank_ajax_worker)
    t.daemon = True
    t.start()

if check_buy_items_init:
    for i, item in enumerate(config.buy_items):
        if intersperse_buy_items and i % intersperse_buy_items == 0:
            for page in range(1, intersperse_buy_items_pages + 1):
                market_jobs.append({'page': page})
        market_jobs.append({'item': item})
        if check_sets:
            market_jobs.append({'item': 'Set', 'all_pages': True})
            #Sets are the only interesting item that we could buy if they're not in the first page

while True:
    if not market_jobs:
        if check_buy_items:
            for i, item in enumerate(config.buy_items):
                if intersperse_buy_items and i % intersperse_buy_items == 0:
                    for page in range(1, intersperse_buy_items_pages + 1):
                        market_jobs.append({'page': page})
                market_jobs.append({'item': item})
            if check_sets:
                market_jobs.append({'item': 'Set', 'all_pages': True})
        for page in range(1, check_pages + 1):
            market_jobs.append({'page': page})

    try:
        start = time.time()
        job = market_jobs.popleft()

        all_pages = job.get('all_pages', False)

        args = {'format': 'json', 'max': most_expensive_buy_item}
        if 'page' in job:
            args['page'] = job['page']
        if 'item' in job:
            args['action'] = 'search'
            args['item'] = job['item']

        logger.debug("Downloading %s", job)
        r = session.get(BASE_URL + 'tori_market.php', params=args)
        data = r.json()

        if 'item' in job:
            items_prices_cache[job['item']] = data

        if all_pages:
            q, r = divmod(data['total_items'], data['results_per_page'])
            pages = q + bool(r)
            for page in range(2, pages + 1):
                market_jobs.append({'item': job['item'], 'page': page})
        
        for item in data['items']:
            if item['inventid'] in items_cache:
                continue
            items_cache[item['inventid']] = True
            if item['setid']:
                logger.debug("Found set")
                """
                set_items = session.get(BASE_URL + 'bank_ajax.php, {
                    'bank_ajax': 'get_items',
                    'inventid': item['setid']
                }).json()
                max_price = 0
                for item in set_items['items']:
                    max_price += config.buy_items.get(item['name'], config.auto_buy)
                    
                if item['price'] <= max_price:
                    logging.info('Buying set {} for {} tc'.format(item['set_name'], item['price']))
                    if not test_run:
                        pass
                        response = session.get(BASE_URL + 'bank_ajax.php', {
                            'bank_ajax': 'buy_market_item',
                            'inventid': item['inventid'],
                            'item_price': item['price'] #or max_price?
                            'set_md5': item['set_md5']
                        }).json()
                """
                #get_items is not working correctly, only returns the set
                #item['setid'] is null

            else:
                if data['user']['qi'] < item['qi']:
                    # We don't have enough qi to buy it
                    # Could be a marketeers item, though they're crazy expensive and shitty
                    continue

                if item['store_price'] <= item['price'] and not item['out_of_stock']:
                    #logger.debug("Prevented from buying %s in stock for %i tc which is more than store price (%i tc)",
                    #    item['name'], item['price'], item['store_price']
                    #)
                    continue

                max_price = config.buy_items.get(item['name'], auto_buy)

                if item['price'] <= max_price:
                    logger.info("Trying to buy %s below max_price (%i)", item['name'], max_price)

                    if 'item' in job:
                        # We already are searching for this item, don't do it again
                        items_data = copy.deepcopy(data)
                        """
                        our_price = None
                        for i in items_data['items']:
                            if i['username'].lower() == config.username.lower():
                                our_price = i['price']
                                break

                        if our_price:
                            # Only items cheaper than we're already selling for
                            # We could raise our price if we don't find anything and the second cheapest item has > 1tc difference in price
                            items_data['items'] = [i for i in items_data['items'] if i['price'] < our_price]
                        """
                    else:
                        if item['username'].lower() == config.username.lower():
                            continue
                        #time.sleep(1)
                        if item['name'] in items_prices_cache:
                            items_data = copy.deepcopy(items_prices_cache[item['name']])
                            logger.debug("Reusing cached data for %s", item['name'])
                        else:
                            logger.debug("Downloading %s's market list to check if it's worth it to buy it", item['name'])
                            items_data = session.get(BASE_URL + 'tori_market.php', params={
                                'format': 'json',
                                'action': 'search',
                                'item':   item['name']
                            }).json()
                            items_prices_cache[item['name']] = copy.deepcopy(items_data)

                    # Let's ignore our items from the list
                    #items_data['items'] = [it for it in items_data['items'] if it['username'].lower() != config.username.lower()]

                    if not items_data['items']:
                        logger.debug("Search for %s didn't give any results (item already sold?)", item['name'])
                        continue

                    if items_data['items'][0]['username'].lower() == config.username.lower():
                        logger.debug("We can't buy our own items")
                        continue

                    if items_data['items'][0]['price'] < item['price']:
                        logger.debug("Found %s for %i tc while searching, instead of %i tc", item['name'], items_data['items'][0]['price'], item['price'])
                        # We can buy that one instead
                        # item = items_data['items'][0]
                        # We already checked it though, we'll continue
                        continue

                    cheapest_on_market = None
                    # Cheapest one after we buy one
                    if len(items_data['items']) >= 2:
                        cheapest_on_market = items_data['items'][1]['price']

                    sell_price = None

                    # Don't sell it if it's neither on market nor stocked on store
                    # Assumes we are buying cheaper than store price with stock (there's a check before)
                    if cheapest_on_market and \
                        cheapest_on_market > item['price'] and \
                        item['out_of_stock']:
                        sell_price = cheapest_on_market - 1
                    elif not item['out_of_stock']:
                        if cheapest_on_market and cheapest_on_market < item['store_price']:
                            sell_price = max(item['price'], cheapest_on_market - 1)
                        else:
                            sell_price = item['store_price'] - 1

                    if not sell_price and not buy_item_if_not_sellable:
                        logger.debug("No sell price for %s, not buying", item['name'])
                        continue

                    t = 1.0
                    if item['name'] in config.buy_items:
                        i = buy_items_keys.index(item['name'])
                        t = float(i) / ((len(config.buy_items) - 1) or 1)
                    
                    desired_profit = config.worst_profit_margin + (config.best_profit_margin - config.worst_profit_margin) * t
                    if int(item['price'] * desired_profit) >= sell_price:
                        logger.debug("Buying %s for %i tc doesn't has enough profit margin (%i tc < %i tc)", item['name'], item['price'], item['price'] * desired_profit, sell_price)
                        continue

                    if len(items_data['items']) >= 2 and \
                       sell_price >= items_data['items'][1]['price']:
                        logger.debug("Skipping %s, there's someone else already selling it for less than our sell price", item['name'])
                        continue

                    bank_ajax_job = []

                    logger.info("Buying %s for %i tc (%i - %s)", item['name'], item['price'], item['inventid'], item['username'])
                    if not test_run:
                        bank_ajax_job.append({
                            'bank_ajax': 'buy_market_item',
                            'inventid': item['inventid'],
                            'item_price': item['price'],
                            'token': token
                        })

                    if sell_price:
                        logger.info("Reselling %s for %i tc", item['name'], sell_price)
                        if not test_run:
                            bank_ajax_job.append({
                                'bank_ajax': 'add_market_item',
                                'inventid': item['inventid'],
                                'price': sell_price,
                                'token': token
                            })

                    if bank_ajax_job:
                        bank_ajax_jobs.put(bank_ajax_job)

    except Exception as e:
        market_jobs.append(job)
        logger.exception(e)
        time.sleep(2) #We could be getting rate limited

    time.sleep(max(0, 1 - (time.time() - start)))