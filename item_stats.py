from bs4 import BeautifulSoup
from Queue import Queue
import re
import requests
from threading import Thread

def get_item_worker():
    while True:
        i = q.get()
        try:
            page = requests.get("http://forum.toribash.com/tori_shop_item.php?id=" + str(i))
            soup = BeautifulSoup(page.text)
            name = soup.table.h1.text

            stock, qi, price, owned_by, total_items, total_circulation = map(
                lambda s: int(re.sub(r"[^\d]", "", s.string)),
                soup.table.find_all("tr")[5].find_all("td")
            )

            print "{:5} {:20} {:10} {:10}".format(i, name, price, total_circulation)

            items[name] = {
                "name": name, "stock": stock, "qi": qi, "price": price,
                "owned_by": owned_by, "total_items": total_items,
                "total_circulation": total_circulation, 'id': i
            }
        except Exception as e:
            print i, e
        q.task_done()

if __name__ == "__main__":
    import json
    
    q = Queue()
    items = {}

    for i in range(4):
        t = Thread(target=get_item_worker)
        t.daemon = True
        t.start()

    for i in xrange(2500):
        q.put(i)

    q.join()
    open("items.json", "w").write(json.dumps(items))