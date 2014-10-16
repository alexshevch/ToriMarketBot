from collections import OrderedDict
import getpass

username = raw_input('Username: ')
password = getpass.getpass('Password: ')

check_pages_init = 0 # if negative, check all
check_pages = 2

check_buy_items = True
intersperse_buy_items = 8
intersperse_buy_items_pages = 2

auto_buy = 3 # Cheapest item is 5 (and they're shit, we only want to buy items with the price set accidentally too cheap)

worst_profit_margin = 1.1 # most sold items, interpolated by total_circulation's rank
best_profit_margin  = 1.3 # least sold items

test_run = True

bump = 900 # Fish says this won't work anymore, but it does

buy_items = OrderedDict([
    #item name                                     buy price    market price   shop price
    (u'Music'                              ,              81), #          98          100
   #(u'Set'                                ,              83), #         100           10
    (u'Orc Right Hand Motion Trail'        ,               7), #          20           10
    (u'Chronos Grip'                       ,               3), #           9            5
    (u'Chronos Right Hand Motion Trail'    ,               3), #          10            5
    (u'Head Texture'                       ,             180), #         193          200
   #(u'Shiai Token'                        ,               0), #           0            0
    (u'Orc Left Hand Motion Trail'         ,               7), #          20           10
    (u'Gladiator Right Hand Motion Trail'  ,               3), #          10            5
    (u'Orc Grip'                           ,               7), #          70           10
    (u'Chronos Force'                      ,              50), #          59           75
    (u'Chronos Left Hand Motion Trail'     ,               3), #          15            5
    (u'Gladiator Blood'                    ,              20), #          24           50
    (u'Orc Blood'                          ,              65), #          79          100
    (u'Orc Torso'                          ,              25), #          30           30
    (u'Orc Right Leg Motion Trail'         ,               7), #          20           10
    (u'Orc Force'                          ,             105), #         127          150
    (u'Gladiator Force'                    ,              41), #          50           75
    (u'Chronos Torso'                      ,              10), #          30           15
    (u'Orc Relax'                          ,              70), #          85          100
    (u'Gladiator Left Hand Motion Trail'   ,               3), #          20            5
    (u'Orc Left Leg Motion Trail'          ,               7), #          20           10
    (u'Gladiator Primary Gradient'         ,              10), #          15           15
    (u'Gladiator Torso'                    ,              10), #          15           15
    (u'Chronos Blood'                      ,              20), #          25           50
    (u'Gladiator Relax'                    ,              32), #          39           50
    (u'Chronos Relax'                      ,              39), #          47           50
    (u'Gladiator Grip'                     ,               3), #          10            5
    (u'Chronos Primary Gradient'           ,              10), #          10           15
    (u'Orc Secondary Gradient'             ,              16), #          20           30
    (u'Orc Primary Gradient'               ,              16), #          20           30
    (u'Gladiator Secondary Gradient'       ,              10), #          10           15
    (u'Chronos Left Leg Motion Trail'      ,               3), #          10            5
    (u'Chronos Right Leg Motion Trail'     ,               3), #          19            5
    (u'Gladiator Right Leg Motion Trail'   ,               3), #          15            5
    (u'Orc DQ'                             ,               7), #          20           10
    (u'Orc Ghost'                          ,              40), #          48           50
    (u'Chronos Secondary Gradient'         ,              10), #          12           15
    (u'Orc User Text'                      ,              12), #          15           20
    (u'Gladiator Left Leg Motion Trail'    ,               3), #          23            5
    (u'Orc Emote'                          ,               7), #          20           10
    (u'Chronos DQ'                         ,               3), #          25            5
    (u'Orc Hair'                           ,              23), #          28           30
    (u'Acid Blood'                         ,            3332), #        3999         6000
    (u'Chronos User Text'                  ,               7), #          15           10
    (u'Gladiator Emote'                    ,               3), #          10            5
    (u'Chronos Hair'                       ,              10), #          20           15
    (u'Gladiator Hair'                     ,              10), #          20           15
    (u'Chronos Emote'                      ,               3), #          15            5
    (u'Gladiator DQ'                       ,               3), #          30            5
    (u'Orc Timer'                          ,              15), #          18           20
    (u'Gladiator User Text'                ,               9), #          11           10
    (u'Gladiator Ghost'                    ,              15), #          18           25
    (u'Chronos Ghost'                      ,              18), #          22           25
    (u'Chronos Timer'                      ,               7), #          22           10
    (u'Gladiator Timer'                    ,               7), #          10           10
    (u'Aqua Right Hand Motion Trail'       ,              50), #         450           80
    (u'Gaia Force'                         ,             490), #         589          600
    (u'Marine Primary Gradient'            ,             207), #         249          270
    (u'Kiai Sound'                         ,             831), #         998         1000
    (u'Aqua Primary Gradient'              ,             158), #         190          240
    (u'Aqua Secondary Gradient'            ,             200), #         300          240
   #(u'Flame'                              ,            6833), #        8200            0
    (u'Radioactive Force'                  ,             807), #         969         1050
    (u'Aqua Force'                         ,             945), #        1135         1200
    (u'Radioactive Relax'                  ,             575), #         690          700
    (u'Marine Secondary Gradient'          ,             158), #         190          270
    (u'Marine Right Hand Motion Trail'     ,              70), #          85           90
    (u'Gaia Primary Gradient'              ,              83), #         100          120
    (u'Gaia Secondary Gradient'            ,              82), #          99          120
    (u'Aqua Relax'                         ,             561), #         674          800
    (u'Marine Force'                       ,             998), #        1198         1350
    (u'Gaia Right Hand Motion Trail'       ,              30), #          50           40
    (u'Knox Primary Gradient'              ,              75), #          90           90
    (u'Aqua DQ'                            ,              65), #          78           80
    (u'Marine Left Hand Motion Trail'      ,              66), #          80           90
    (u'Aqua Left Leg Motion Trail'         ,              65), #          78           80
    (u'Gaia Relax'                         ,             275), #         330          400
    (u'Aqua Right Leg Motion Trail'        ,              65), #          78           80
    (u'Aqua Left Hand Motion Trail'        ,              66), #          80           80
    (u'Aqua Torso'                         ,             199), #         239          240
    (u'Left Leg Texture'                   ,            1750), #        1792         2000
    (u'Juryo Primary Gradient'             ,              57), #          69           90
   #(u'Radioactive Primary Gradient'       ,             416), #         500          210
    (u'Aqua Emote'                         ,              62), #          75           80
    (u'Juryo Force'                        ,             299), #         359          450
    (u'Right Hand Texture'                 ,            1750), #        1899         2000
    (u'Left Hand Texture'                  ,            1750), #        1898         2000
    (u'Radioactive Right Hand Motion Trail',              50), #         150           70
    (u'Radioactive Secondary Gradient'     ,             150), #         500          210
    (u'Knox Force'                         ,             333), #         400          450
    (u'Right Leg Texture'                  ,            1750), #        1949         2000
    (u'Radioactive Torso'                  ,             150), #         400          210
    (u'Sphinx Force'                       ,             925), #        1110         1500
    (u'Gaia Torso'                         ,              83), #         100          120
    (u'Gaia Left Hand Motion Trail'        ,              25), #         100           40
    (u'Breast Texture'                     ,            1750), #        1796         2000
    (u'Marine Relax'                       ,             665), #         799          900
    (u'Sphinx Secondary Gradient'          ,             203), #         244          300
    (u'Right Bicep Texture'                ,            1750), #        1999         2000
    (u'Gaia Right Leg Motion Trail'        ,              25), #          80           40
    (u'Marine DQ'                          ,              73), #          88           90
    (u'Left Bicep Texture'                 ,            1600), #        1749         2000
    (u'Sphinx Primary Gradient'            ,             208), #         250          300
    (u'Marine Torso'                       ,             208), #         250          270
    (u'Marine Right Leg Motion Trail'      ,              70), #          85           90
    (u'Left Thigh Texture'                 ,            1750), #        2500         2000
    (u'Left Tricep Texture'                ,            1750), #        1997         2000
    (u'Marine Left Leg Motion Trail'       ,              73), #          88           90
    (u'Aqua Hair'                          ,             166), #         200          240
    (u'Left Foot Texture'                  ,            1665), #        1999         2000
    (u'Aqua Blood'                         ,             624), #         749          800
    (u'Head Avatar'                        ,            1208), #        1450         1500
    (u'Juryo Secondary Gradient'           ,              71), #          86           90
    (u'Right Thigh Texture'                ,            1750), #           0         2000
    (u'Right Foot Texture'                 ,            1750), #        1899         2000
    (u'Right Tricep Texture'               ,            1750), #        1999         2000
    (u'Radioactive Right Leg Motion Trail' ,              50), #         200           70
    (u'Flame Particle Texture'             ,            6833), #        8200        10000
    (u'Aqua User Text'                     ,             115), #         139          160
    (u'Quicksilver Force'                  ,           10665), #       12799        24000
    (u'Aqua Grip'                          ,              65), #          78           80
    (u'Chest Texture'                      ,            1750), #        1999         2000
    (u'Radioactive Left Hand Motion Trail' ,              50), #         290           70
    (u'Knox Secondary Gradient'            ,              73), #          88           90
    (u'Gaia Left Leg Motion Trail'         ,              25), #         111           40
    (u'Right Pec Texture'                  ,            1750), #        1887         2000
    (u'Amethyst Primary Gradient'          ,             283), #         340          360
    (u'Sphinx Relax'                       ,             748), #         898         1000
    (u'Superfly Primary Gradient'          ,              91), #         110          150
    (u'Hit 1 Sound'                        ,             665), #         798          800
    (u'Radioactive Left Leg Motion Trail'  ,              57), #          69           70
   #(u'Daimyo Hat and Scarf'               ,            9074), #       10889            0
    (u'Marine Emote'                       ,              73), #          88           90
    (u'Radioactive Blood'                  ,             581), #         698          700
    (u'Groin Texture'                      ,            1750), #        1999         2000
    (u'Knox Relax'                         ,             250), #         300          300
    (u'Left Pec Texture'                   ,            1750), #        1949         2000
    (u'Amethyst Secondary Gradient'        ,             283), #         340          360
    (u'Stomach Texture'                    ,            1750), #        6000         2000
    (u'Juryo Relax'                        ,             225), #         270          300
    (u'Ivory Force'                        ,            1836), #        2204         2250
    (u'Superfly Force'                     ,             458), #         550          750
    (u'Superfly Relax'                     ,             374), #         449          500
    (u'Radioactive Ghost'                  ,             290), #         348          350
    (u'Gaia Ghost'                         ,             145), #         175          200
    (u'Aqua Ghost'                         ,             331), #         398          400
    (u'Helios Secondary Gradient'          ,             150), #         375          240
    (u'Ecto Primary Gradient'              ,             248), #         298          300
    (u'Knox Right Hand Motion Trail'       ,              25), #          30           30
    (u'Radioactive DQ'                     ,              50), #         280           70
    (u'Ecto Secondary Gradient'            ,             195), #         235          300
    (u'Amethyst Right Hand Motion Trail'   ,              98), #         118          120
    (u'Vampire Relax'                      ,            3333), #        4000         5000
    (u'Gaia Blood'                         ,             305), #         366          400
    (u'Marine Hair'                        ,             200), #         400          270
    (u'Marine Blood'                       ,             575), #         690          900
    (u'Sphinx Right Hand Motion Trail'     ,              80), #          97          100
    (u'Helios Primary Gradient'            ,             150), #         500          240
    (u'Marine User Text'                   ,             115), #         138          180
   #(u'Dread Tail'                         ,            5083), #        6100            0
    (u'Knox Torso'                         ,              66), #          80           90
    (u'Gaia DQ'                            ,              25), #         100           40
    (u'Helios Force'                       ,             915), #        1098         1200
    (u'Uke Hair'                           ,             750), #         900         1000
    (u'Radioactive Hair'                   ,             173), #         208          210
    (u'Left Hand Trail Texture'            ,            4000), #        4749         5000
    (u'Hit 2 Sound'                        ,             665), #         798          800
    (u'Right Hand Trail Texture'           ,            4000), #        4700         5000
    (u'Tori Hair'                          ,             833), #        1000         1000
    (u'Gaia Grip'                          ,              25), #          50           40
    (u'Ecto Torso'                         ,             204), #         245          300
    (u'Superfly Secondary Gradient'        ,             123), #         148          150
    (u'Radioactive Emote'                  ,              50), #         990           70
    (u'Vampire Force'                      ,            4832), #        5799         7500
    (u'Sphinx Left Hand Motion Trail'      ,              79), #          95          100
    (u'Pure Relax'                         ,           12035), #       14443        20000
   #(u'Appreciation Token'                 ,               0), #           0            0
    (u'Helios Relax'                       ,             620), #         744          800
    (u'Beetle Primary Gradient'            ,             249), #         299          360
    (u'Gaia User Text'                     ,              65), #          78           80
    (u'Marine Grip'                        ,              74), #          89           90
    (u'Gaia Hair'                          ,              75), #        1000          120
    (u'Beetle Secondary Gradient'          ,             250), #         300          360
    (u'Ecto Force'                         ,            1081), #        1298         1500
    (u'Juryo Torso'                        ,              74), #          89           90
    (u'Marine Ghost'                       ,             346), #         416          450
    (u'Amethyst Relax'                     ,             915), #        1099         1200
    (u'Aqua Timer'                         ,             125), #         150          160
    (u'Sphinx Torso'                       ,             248), #         298          300
   #(u'Pure Force'                         ,           35000), #       42000        30000
    (u'512x512 Head Texture'               ,           16500), #       19799        20000
    (u'Radioactive User Text'              ,              79), #          95          140
    (u'Gaia Emote'                         ,              25), #         150           40
   #(u'Santa Hat'                          ,               0), #        9500         5000
    (u'Knox Left Hand Motion Trail'        ,              25), #          30           30
    (u'Beetle Force'                       ,            1250), #        1500         1800
    (u'Juryo Right Hand Motion Trail'      ,              20), #         100           30
    (u'Radioactive Grip'                   ,              50), #         500           70
    (u'Left Leg Trail Texture'             ,            4000), #        4434         5000
   #(u'Mayan Warrior'                      ,            5000), #        6000            0
    (u'Right Leg Trail Texture'            ,            4000), #        4500         5000
    (u'Helios Left Hand Motion Trail'      ,              55), #         150           80
    (u'Hit 4 Sound'                        ,             650), #         798          800
    (u'Hit 3 Sound'                        ,             650), #        1550          800
    (u'Juryo Ghost'                        ,              83), #         100          150
    (u'Acid Force'                         ,            5333), #        6400         9000
    (u'Elf Force'                          ,            3250), #        3900        21000
    (u'Amethyst Left Hand Motion Trail'    ,              98), #         118          120
    (u'Ivory Relax'                        ,            1124), #        1349         1500
    (u'Beetle Relax'                       ,             833), #        1000         1200
    (u'[GUI] Background'                   ,             308), #         370         1000
    (u'Helios Right Hand Motion Trail'     ,              66), #          80           80
    (u'Superfly Right Hand Motion Trail'   ,              40), #          48           50
    (u'Amethyst Hair'                      ,             166), #         200          360
   #(u'Shutter Shades'                     ,           23750), #       28500            0
    (u'Juryo Blood'                        ,             240), #         289          300
    (u'Juryo Left Hand Motion Trail'       ,              23), #          28           30
    (u'Knox Blood'                         ,             248), #         298          300
    (u'Hit 5 Sound'                        ,             666), #         800          800
    (u'Bronze Primary Gradient'            ,             333), #         400          420
    (u'Amethyst Force'                     ,            1250), #        1500         1800
    (u'Knox Right Leg Motion Trail'        ,              20), #         333           30
    (u'Knox Left Leg Motion Trail'         ,              20), #          50           30
    (u'Juryo DQ'                           ,              22), #          27           30
    (u'Ivory Primary Gradient'             ,             333), #         400          450
    (u'Helios Torso'                       ,             150), #         300          240
   #(u'Barbed Wire'                        ,           12500), #       15000            0
    (u'Juryo Grip'                         ,              23), #          28           30
    (u'Gaia Timer'                         ,              65), #          78           80
    (u'Toxic Hair'                         ,             831), #         998         1800
    (u'Hunter Force'                       ,            5000), #           0        15000
    (u'Amethyst Right Leg Motion Trail'    ,              98), #         118          120
    (u'Ecto Relax'                         ,             823), #         988         1000
    (u'Amber Relax'                        ,            1499), #        1799        14000
    (u'Ecto Right Hand Motion Trail'       ,              50), #         400          100
    (u'Radioactive Timer'                  ,             115), #         139          140
    (u'Bronze Relax'                       ,            1000), #        1200         1400
    (u'Elf Relax'                          ,            3000), #        3600        14000
    (u'Noxious Relax'                      ,            1632), #        1959         2000
   #(u'Santa Beard'                        ,           12500), #       15000         5000
    (u'Beetle Right Hand Motion Trail'     ,              82), #          99          120
    (u'Sphinx Right Leg Motion Trail'      ,              79), #          95          100
    (u'Amethyst Torso'                     ,             291), #         350          360
    (u'Amethyst User Text'                 ,             181), #         218          240
    (u'Hunter Hair'                        ,            2333), #        2800         3000
    (u'Juryo Right Leg Motion Trail'       ,              20), #          50           30
    (u'Toxic Relax'                        ,            3749), #        4499         6000
    (u'[GUI] Header'                       ,             458), #         550         1000
    (u'Helios Right Leg Motion Trail'      ,              75), #          90           80
    (u'Amethyst Left Leg Motion Trail'     ,              98), #         118          120
    (u'Pure Blood'                         ,            7500), #        9000        20000
    (u'Acid Relax'                         ,            3207), #        3849         6000
    (u'[GUI] Splatter'                     ,             358), #         430         1000
    (u'Superfly Left Hand Motion Trail'    ,              41), #          50           50
    (u'Knox User Text'                     ,              41), #          50           60
    (u'Bronze Secondary Gradient'          ,             333), #         400          420
    (u'Vampire Hair'                       ,            1248), #        1498         1500
    (u'Amethyst Ghost'                     ,             458), #         550          600
    (u'Toxic Force'                        ,            5312), #        6375         9000
    (u'Copper Relax'                       ,            1498), #        1798         7000
    (u'Pure Hair'                          ,            2916), #        3500         6000
   #(u'Eye Patch'                          ,           14916), #       17900            0
    (u'Ivory Secondary Gradient'           ,             333), #         400          450
   #(u'Sphinx Left Leg Motion Trail'       ,             166), #         200          100
    (u'Amethyst DQ'                        ,              81), #          98          120
    (u'Noxious Secondary Gradient'         ,             496), #         596          600
    (u'Juryo Hair'                         ,              50), #         500           90
    (u'Minihawk'                           ,            7499), #        8999        10000
    (u'Vampire Ghost'                      ,            1666), #        2000         2500
    (u'Elf Emote'                          ,             287), #         345         1400
    (u'Sphinx Hair'                        ,             225), #         270          300
    (u'Vampire Primary Gradient'           ,            1247), #        1497         1500
    (u'Knox Ghost'                         ,              83), #         100          150
    (u'Superfly Torso'                     ,             123), #         148          150
    (u'Amethyst Blood'                     ,             872), #        1047         1200
    (u'Juryo Emote'                        ,              22), #          27           30
    (u'Vampire Right Hand Motion Trail'    ,             167), #         201          200
    (u'Gold Relax'                         ,            5996), #        7196         8000
    (u'Noxious Primary Gradient'           ,             291), #         350          600
    (u'Sphinx DQ'                          ,              50), #         200          100
    (u'Ecto Left Leg Motion Trail'         ,              50), #         200          100
    (u'Cat Ears'                           ,           36666), #       44000       100000
    (u'Sphinx Emote'                       ,              50), #         130          100
    (u'Ivory Hair Color'                   ,             166), #         200          450
    (u'Knox Hair'                          ,              50), #         999           90
    (u'Pure Torso'                         ,            3333), #        4000         6000
    (u'Cobra Relax'                        ,            4416), #        5300         6000
    (u'Noxious Force'                      ,            1249), #        1499         3000
    (u'Viridian Relax'                     ,            4415), #        5298        20000
    (u'Ecto Right Leg Motion Trail'        ,              50), #         500          100
    (u'Ecto Left Hand Motion Trail'        ,              50), #         144          100
    (u'Knox Grip'                          ,              23), #          28           30
    (u'Knox Emote'                         ,              15), #         100           30
    (u'Marine Timer'                       ,             100), #        1000          180
   #(u'Green Hat'                          ,           20833), #       25000            0
    (u'[GUI] Logo'                         ,             500), #         600         1000
    (u'Sphinx User Text'                   ,             165), #         198          200
    (u'Helios DQ'                          ,              40), #         100           80
    (u'Beetle User Text'                   ,             165), #         198          240
    (u'Juryo Left Leg Motion Trail'        ,              15), #          50           30
    (u'Maya Force'                         ,            2620), #        3144         7500
    (u'Bronze Force'                       ,            1291), #        1550         2100
    (u'Beetle Left Hand Motion Trail'      ,              99), #         119          120
    (u'Sapphire Force'                     ,            4999), #        5999         7500
    (u'Viridian Force'                     ,            5333), #        6400        30000
    (u'Crimson Force'                      ,            3750), #        4500        42000
    (u'Hot Pink Relax'                     ,            1666), #        2000        24000
   #(u'Vampire Secondary Gradient'         ,            4166), #        5000         1500
    (u'Titan Force'                        ,            2583), #        3100         7500
    (u'Hunter Relax'                       ,            7458), #        8950        10000
   #(u'Toxic DQ'                           ,             800), #         960          600
    (u'Helios Left Leg Motion Trail'       ,              75), #          90           80
    (u'Sapphire Relax'                     ,            2341), #        2810         5000
    (u'Ecto Ghost'                         ,             374), #         449          500
    (u'512x512 Left Bicep Texture'         ,           16249), #       19499        20000
    (u'Bronze Torso'                       ,             348), #         418          420
    (u'512x512 Breast Texture'             ,           16184), #       19421        20000
    (u'512x512 Right Thigh Texture'        ,           15833), #       19000        20000
    (u'Beetle Hair'                        ,             283), #         340          360
   #(u'Vampire Left Hand Motion Trail'     ,             790), #         949          200
    (u'Toxic Primary Gradient'             ,            1250), #        1500         1800
    (u'Alpha Relax'                        ,          133333), #      160000       200000
    (u'Helios Emote'                       ,              63), #          76           80
    (u'Ecto User Text'                     ,             124), #         149          200
    (u'Bronze Right Hand Motion Trail'     ,             115), #         138          140
   #(u'Pure User Text'                     ,           16666), #       20000         4000
    (u'512x512 Right Hand Texture'         ,           16249), #       19499        20000
    (u'Beetle Torso'                       ,             250), #         300          360
    (u'Toxic Secondary Gradient'           ,            1250), #        1500         1800
    (u'Elf Ghost'                          ,            4166), #        5000         7000
    (u'Toxic Torso'                        ,            1324), #        1589         1800
    (u'Ecto DQ'                            ,              81), #          98          100
    (u'Ecto Blood'                         ,             748), #         898         1000
   #(u'Hunter Secondary Gradient'          ,               0), #           0         3000
    (u'Platinum Relax'                     ,           16665), #       19999        28000
   #(u'Amethyst Grip'                      ,             370), #         444          120
    (u'Knox DQ'                            ,              25), #          30           30
   #(u'Vampire DQ'                         ,             687), #         825          500
    (u'Beetle Right Leg Motion Trail'      ,              49), #          59          120
    (u'512x512 Right Leg Texture'          ,           16249), #       19499        20000
    (u'512x512 Left Leg Texture'           ,           16249), #       19499        20000
    (u'512x512 Left Hand Texture'          ,           16249), #       19499        20000
    (u'512x512 Right Bicep Texture'        ,           16249), #       19499        20000
    (u'Camo Force'                         ,            1666), #        2000         3600
    (u'Sphinx Blood'                       ,             787), #         945         1000
   #(u'Sphinx Ghost'                       ,               0), #           0          500
    (u'Vampire Torso'                      ,            1203), #        1444         1500
    (u'Hunter Primary Gradient'            ,            2325), #        2790         3000
    (u'Ecto Emote'                         ,              75), #          90          100
    (u'Vampire Right Leg Motion Trail'     ,             358), #         430          500
    (u'512x512 Left Thigh Texture'         ,           16250), #       19500        20000
    (u'256x256 Left Hand Texture'          ,            7999), #        9599        10000
    (u'Crimson Emote'                      ,             582), #         699         2800
    (u'Toxic Ghost'                        ,            2000), #        2400         3000
    (u'Gold Force'                         ,            9791), #       11750        12000
    (u'Cobra Primary Gradient'             ,            1250), #        1500         1800
   #(u'Dark Duke'                          ,           21458), #       25750            0
    (u'Elf Blood'                          ,            4165), #        4999        14000
    (u'Beetle DQ'                          ,              96), #         116          120
    (u'Beetle Left Leg Motion Trail'       ,              95), #         114          120
    (u'Copper Force'                       ,            3165), #        3798        10500
   #(u'Collectors Card'                    ,           20000), #       24000            0
   #(u'Noxious Torso'                      ,            3331), #        3998          600
    (u'Superfly Right Leg Motion Trail'    ,              41), #          50           50
    (u'Elf Grip'                           ,             620), #         745         1400
    (u'Superfly Ghost'                     ,             166), #         200          250
    (u'Juryo Timer'                        ,              48), #          58           60
   #(u'Helios Hair'                        ,             333), #         400          240
    (u'Cobra Force'                        ,            7124), #        8549         9000
    (u'Cobra Left Hand Motion Trail'       ,             400), #         480          600
    (u'Quicksilver Relax'                  ,            9833), #       11800        16000
    (u'Neptune Relax'                      ,            1832), #        2199         4000
    (u'Void Relax'                         ,           83332), #       99999       180000
    (u'Beetle Grip'                        ,              61), #          74          120
    (u'Demon Relax'                        ,           73250), #       87900       160000
   #(u'Olive Force'                        ,           16666), #       20000         2100
    (u'512x512 Left Tricep Texture'        ,           16249), #       19499        20000
    (u'512x512 Left Pec Texture'           ,           16249), #       19499        20000
    (u'Superfly User Text'                 ,              76), #          92          100
    (u'256x256 Head Texture'               ,            8083), #        9700        10000
    (u'256x256 Right Hand Texture'         ,            8165), #        9799        10000
    (u'Pharos Force'                       ,            7830), #        9397        15000
    (u'Pharos Relax'                       ,            6583), #        7900        10000
   #(u'Vampire Emote'                      ,            3333), #        4000          500
    (u'Raider Force'                       ,           35000), #       42000        48000
    (u'Acid Secondary Gradient'            ,            1249), #        1499         1800
    (u'Acid DQ'                            ,             458), #         550          600
    (u'Toxic Right Hand Motion Trail'      ,             373), #         448          600
    (u'Supernova Primary Gradient'         ,             791), #         950         7200
    (u'Amethyst Emote'                     ,              98), #         118          120
    (u'Elf Primary Gradient'               ,             833), #        1000         4200
    (u'Sphinx Grip'                        ,              82), #          99          100
    (u'Adamantium Force'                   ,            4333), #        5200        12000
    (u'Camo Primary Gradient'              ,             333), #         400          720
    (u'Acid Primary Gradient'              ,            1415), #        1698         1800
   #(u'Grip Sound'                         ,            6250), #        7500         5000
    (u'Viridian Primary Gradient'          ,             833), #        1000         6000
    (u'Elf User Text'                      ,             749), #         899         2800
   #(u"Surfer's Seishin"                   ,               0), #           0        25000
    (u'Typhon Force'                       ,            3332), #        3999         4500
    (u'Hydra Blood'                        ,            5833), #        7000        20000
    (u'Beetle Blood'                       ,             791), #         950         1200
    (u'Demon Force'                        ,          108333), #      130000       240000
    (u'Superfly Blood'                     ,             415), #         498          500
    (u'Superfly DQ'                        ,              33), #          40           50
    (u'512x512 Chest Texture'              ,           16249), #       19499        20000
    (u'512x512 Right Tricep Texture'       ,           16249), #       19499        20000
    (u'Shaman Relax'                       ,            9159), #       10991        16000
   #(u'Headphones'                         ,           50000), #       60000            0
    (u'Knox Timer'                         ,              50), #          60           60
    (u'Sphinx Timer'                       ,             157), #         189          200
    (u'Hydra Emote'                        ,            1125), #        1350         2000
   #(u'Superfly Grip'                      ,             166), #         200           50
    (u'Elf Secondary Gradient'             ,             833), #        1000         4200
   #(u'Pure Grip'                          ,           25000), #       30000         2000
   #(u'Acid Ghost'                         ,               0), #           0         3000
    (u'Neptune Force'                      ,            2666), #        3200         6000
   #(u'Organic Cucumber'                   ,            5000), #        6000            0
    (u'Platinum Force'                     ,           29581), #       35498        42000
   #(u'Helios Ghost'                       ,             545), #         655          400
    (u'Beetle Emote'                       ,              93), #         112          120
    (u'Olive Relax'                        ,            1037), #        1245         1400
    (u'Supernova Force'                    ,            9791), #       11750        36000
    (u'Viridian Secondary Gradient'        ,             833), #        1000         6000
    (u'Olive Primary Gradient'             ,             308), #         370          420
    (u'Viridian Left Leg Motion Trail'     ,             665), #         799         2000
    (u'512x512 Stomach Texture'            ,           16249), #       19499        20000
    (u'512x512 Right Pec Texture'          ,           16249), #       19499        20000
    (u'256x256 Right Leg Texture'          ,            7333), #        8800        10000
   #(u'Shaman Force'                       ,               0), #           0        24000
    (u'Noxious Blood'                      ,            1249), #        1499         2000
    (u'256x256 Groin Texture'              ,            8081), #        9698        10000
   #(u'Bronze DQ'                          ,             166), #         200          140
    (u'Viridian DQ'                        ,             416), #         500         2000
    (u'Viridian Blood'                     ,            1000), #        1200        20000
    (u'Crimson Relax'                      ,            2500), #        3000        28000
    (u'Sapphire Emote'                     ,             166), #         200          500
    (u'Supernova Relax'                    ,           14583), #       17500        24000
    (u'Static Relax'                       ,           24999), #       29999       100000
    (u'Gold Hair'                          ,            1666), #        2000         2400
    (u'Plasma Force'                       ,            3749), #        4499        54000
    (u'Neptune Secondary Gradient'         ,             658), #         790         1200
    (u'Ivory Torso'                        ,             373), #         448          450
    (u'Raptor Relax'                       ,            2083), #        2500        20000
   #(u'Helios Timer'                       ,             250), #         300          160
   #(u'Typhon Relax'                       ,            3625), #        4350         3000
    (u'Beetle Ghost'                       ,             333), #         400          600
    (u'Copper Right Hand Motion Trail'     ,             416), #         500          700
    (u'Dragon Force'                       ,            7333), #        8800        15000
    (u'Helios Blood'                       ,             646), #         776          800
    (u'Camo Torso'                         ,             416), #         500          720
    (u'Beetle Timer'                       ,             145), #         175          240
    (u'Noxious Hair'                       ,             406), #         488          600
   #(u'Helios User Text'                   ,             165), #         199          160
    (u'Dragon Relax'                       ,            1665), #        1999        10000
    (u'Viridian Emote'                     ,             333), #         400         2000
    (u'Viridian Ghost'                     ,             832), #         999        10000
    (u'Acid Torso'                         ,            1496), #        1796         1800
    (u'512x512 Groin Texture'              ,           15833), #       19000        20000
    (u'256x256 Right Tricep Texture'       ,            8165), #        9799        10000
    (u'256x256 Right Thigh Texture'        ,            7291), #        8750        10000
    (u'256x256 Left Leg Texture'           ,            7915), #        9499        10000
    (u'Maya Relax'                         ,            1491), #        1790         5000
    (u'Vampire Left Leg Motion Trail'      ,             358), #         430          500
    (u'Elf Timer'                          ,             499), #         599         2800
    (u'Neptune Ghost'                      ,             625), #         750         2000
    (u'Pure Primary Gradient'              ,            2083), #        2500         6000
    (u'Crimson Timer'                      ,            2333), #        2800         5600
   #(u'Void Force'                         ,               0), #           0       270000
    (u'Ivory DQ'                           ,              78), #          94          150
    (u'Elf Right Leg Motion Trail'         ,             375), #         450         1400
    (u'Adamantium Blood'                   ,            2665), #        3198         8000
    (u'Cobra Right Hand Motion Trail'      ,             332), #         399          600
    (u'Vortex Relax'                       ,           12499), #       14999       100000
    (u'Adamantium Primary Gradient'        ,            1831), #        2198         2400
    (u'Adamantium User Text'               ,            1329), #        1595         1600
    (u'Ivory Left Hand Motion Trail'       ,              81), #          98          150
    (u'Mysterio Force'                     ,           14166), #       17000        90000
   #(u'Contact KiTFoX'                     ,            7500), #        9000            0
    (u'512x512 Left Foot Texture'          ,           16249), #       19499        20000
    (u'512x512 Right Foot Texture'         ,           16249), #       19499        20000
    (u'Azurite Relax'                      ,           32500), #       39000        40000
    (u'Superfly Left Leg Motion Trail'     ,              40), #          48           50
    (u'Void Secondary Gradient'            ,            1000), #       40000        54000
   #(u'Ecto Timer'                         ,             832), #         999          200
    (u'DQ Texture'                         ,           40832), #       48999        50000
    (u'256x256 Right Bicep Texture'        ,            7833), #        9400        10000
    (u'256x256 Left Tricep Texture'        ,            8165), #        9799        10000
    (u'Hydra User Text'                    ,             833), #        1000         4000
    (u'Amethyst Timer'                     ,             198), #         238          240
    (u'256x256 Stomach Texture'            ,            8165), #        9799        10000
    (u'256x256 Chest Texture'              ,            7875), #        9450        10000
    (u'Acid Hair'                          ,            1666), #        2000         1800
    (u'Ivory Grip'                         ,              65), #          78          150
   #(u'Cobra Hair'                         ,               0), #           0         1800
    (u'Bronze Hair'                        ,             333), #         400          420
    (u'Juryo User Text'                    ,              48), #          58           60
   #(u'Ecto Hair'                          ,             833), #        1000          300
    (u'Titan Relax'                        ,            3056), #        3668         5000
   #(u'Superfly Hair'                      ,             500), #         600          150
   #(u'Vampire Grip'                       ,               0), #           0          500
    (u'Ivory Blood'                        ,            1158), #        1390         1500
    (u'Noxious Right Leg Motion Trail'     ,             150), #         180          200
    (u'Velvet Relax'                       ,            7291), #        8750        14000
    (u'Adamantium Secondary Gradient'      ,            1915), #        2298         2400
    (u'Camo Relax'                         ,            1707), #        2049         2400
    (u'Ivory User Text'                    ,             142), #         171          300
   #(u'Helios Grip'                        ,             500), #         600           80
    (u'Void Primary Gradient'              ,            1000), #        8000        54000
    (u'Elf DQ'                             ,             333), #         400         1400
    (u'Camo Secondary Gradient'            ,             250), #         300          720
    (u'Warrior Relax'                      ,            7165), #        8599        60000
    (u'Copper DQ'                          ,             375), #         450          700
    (u'Supernova Ghost'                    ,            7333), #        8800        12000
    (u'Vampire Blood'                      ,            4082), #        4899         5000
    (u'Noxious Left Leg Motion Trail'      ,             150), #         180          200
    (u'Amber Force'                        ,            6250), #        7500        21000
    (u'Crimson User Text'                  ,             833), #        1000         5600
   #(u'Bronze Left Leg Motion Trail'       ,             250), #         300          140
    (u'Elf Right Hand Motion Trail'        ,            1114), #        1337         1400
   #(u'Pure Secondary Gradient'            ,           43333), #       52000         6000
    (u'256x256 Left Thigh Texture'         ,            8165), #        9799        10000
    (u'Vampire User Text'                  ,             749), #         899         1000
    (u'Toxic Left Leg Motion Trail'        ,             498), #         598          600
   #(u'Pickled Cucumbers'                  ,            2666), #        3200            0
    (u'Crimson Blood'                      ,            3750), #        4500        28000
    (u'Supernova Secondary Gradient'       ,            1665), #        1999         7200
    (u'Ivory Ghost'                        ,             582), #         699          750
    (u'Demon Secondary Gradient'           ,           14583), #       17500        54000
    (u'Viridian Grip'                      ,            1249), #        1499         2000
    (u'Plasma Right Leg Motion Trail'      ,            2500), #        3000         3600
    (u'Elf Hair'                           ,            3333), #        4000         4200
    (u'Bronze Ghost'                       ,             500), #         600          700
    (u'Cobra User Text'                    ,             705), #         847         1200
    (u'Cobra Secondary Gradient'           ,            1250), #        1500         1800
    (u'Hunter Blood'                       ,            8165), #        9799        10000
   #(u"The Sultan's Fez"                   ,               0), #           0        35000
    (u'Neptune User Text'                  ,             260), #         312          800
    (u'Vulcan Relax'                       ,           11666), #       14000        20000
    (u'Sapphire Blood'                     ,            4165), #        4998         5000
    (u'Copper Blood'                       ,            5333), #        6400         7000
    (u'Supernova Grip'                     ,             458), #         550         2400
    (u'Bronze Blood'                       ,             666), #         800         1400
    (u'Azurite Force'                      ,           50000), #       60000        60000
    (u'256x256 Right Foot Texture'         ,            8165), #        9799        10000
    (u'256x256 Left Foot Texture'          ,            8124), #        9749        10000
    (u'Shaman Torso'                       ,            1406), #        1688         4800
    (u'Ground Texture'                     ,           20000), #       24000        25000
   #(u'Superfly Timer'                     ,             208), #         250          100
    (u'Acid Right Hand Motion Trail'       ,             415), #         499          600
    (u'Typhon Secondary Gradient'          ,             540), #         648          900
    (u'Toxic Blood'                        ,            3750), #        4500         6000
    (u'Gold Blood'                         ,            3750), #        4500         8000
    (u'Toxic Timer'                        ,             915), #        1099         1200
    (u'256x256 Breast Texture'             ,            8165), #        9799        10000
   #(u'Supernova User Text'                ,               0), #           0         4800
    (u'Supernova Right Leg Motion Trail'   ,             658), #         790         2400
    (u'Typhon Right Hand Motion Trail'     ,             165), #         199          300
    (u'Crimson Primary Gradient'           ,             750), #         900         8400
    (u'Hydra Ghost'                        ,            5000), #        6000        10000
   #(u'Plasma Left Hand Motion Trail'      ,               0), #           0         3600
   #(u'Bronze Right Leg Motion Trail'      ,             250), #         300          140
    (u'Sapphire Hair'                      ,             833), #        1000         1500
    (u'Quicksilver Hair'                   ,            3916), #        4700         4800
   #(u'Cobra Left Leg Motion Trail'        ,             665), #         799          600
    (u'Old Gold Relax'                     ,            3165), #        3799         7000
    (u'Toxic Grip'                         ,             415), #         499          600
    (u'Raider Relax'                       ,           10831), #       12998        32000
   #(u'Left wrist joint texture'           ,               0), #           0        10000
    (u'Cobra Torso'                        ,            1469), #        1763         1800
    (u'Adamantium DQ'                      ,             640), #         769          800
   #(u'Left pecs joint texture'            ,               0), #           0        15000
   #(u'Chest joint texture'                ,               0), #           0        15000
    (u'Adamantium Left Hand Motion Trail'  ,             332), #         399          800
   #(u'Adamantium Ghost'                   ,               0), #           0         4000
    (u'Adamantium Relax'                   ,            4582), #        5499         8000
    (u'Adamantium Right Hand Motion Trail' ,             499), #         599          800
    (u'Acid Left Hand Motion Trail'        ,             415), #         498          600
    (u'Aurora DQ'                          ,             416), #         500          900
    (u'Adamantium Timer'                   ,             833), #        1000         1600
    (u'Static Ghost'                       ,           16666), #       20000        50000
    (u'Static Emote'                       ,            8332), #        9999        20000
    (u'Static Primary Gradient'            ,            7500), #        9000        30000
    (u'Ivory Left Leg Motion Trail'        ,              82), #          99          150
    (u'Alpha Force'                        ,           30000), #       36000       300000
   #(u"Gentleman's Essentials"             ,               0), #           0        70000
    (u'Aurora Relax'                       ,            6250), #        7500         9000
    (u'Void Torso'                         ,            1000), #       10000        54000
    (u'Copper Left Leg Motion Trail'       ,             500), #         600          700
    (u'Copper Left Hand Motion Trail'      ,             579), #         695          700
    (u'Copper Torso'                       ,            1666), #        2000         2100
    (u'Viridian User Text'                 ,            1082), #        1299         4000
    (u'Viridian Right Leg Motion Trail'    ,             665), #         799         2000
   #(u'Vulcan Force'                       ,               0), #           0        30000
    (u'Copper User Text'                   ,             915), #        1099         1400
    (u'Magma Force'                        ,           41666), #       50000       105000
   #(u'Officer Cap'                        ,           41666), #       50000            0
   #(u'Viridian Timer'                     ,            6000), #        7200         4000
   #(u'Toxic Right Leg Motion Trail'       ,            1666), #        2000          600
    (u'Ecto Grip'                          ,              84), #         101          100
    (u'Elf Left Leg Motion Trail'          ,            1114), #        1337         1400
    (u'Sapphire Torso'                     ,             916), #        1100         1500
   #(u'256x256 Left Bicep Texture'         ,               0), #           0        10000
    (u'Pure Right Leg Motion Trail'        ,            1250), #        1500         2000
    (u'Superfly Emote'                     ,              20), #          25           50
    (u'Static Force'                       ,           58333), #       70000       150000
    (u'Bumpmap Head Texture'               ,            3333), #        4000        10000
    (u'Magnetite Force'                    ,            7916), #        9500        42000
   #(u'Vampire Timer'                      ,               0), #           0         1000
    (u'256x256 Right Pec Texture'          ,            8165), #        9799        10000
   #(u'Toxic Emote'                        ,            1583), #        1900          600
   #(u'Supernova Timer'                    ,               0), #           0         4800
    (u'Neptune DQ'                         ,             297), #         357          400
    (u'Elf Left Hand Motion Trail'         ,            1114), #        1337         1400
   #(u'Raider Left Hand Motion Trail'      ,            8333), #       10000         3200
    (u'Crimson Grip'                       ,             832), #         999         2800
    (u'Noxious Right Hand Motion Trail'    ,             165), #         199          200
    (u'Acid Emote'                         ,             416), #         500          600
    (u'Bronze Emote'                       ,             115), #         138          140
    (u'Demon Primary Gradient'             ,           16666), #       20000        48000
    (u'Cobra DQ'                           ,             333), #         400          600
    (u'Acid Right Leg Motion Trail'        ,             415), #         499          600
   #(u'Raider Torso'                       ,           23333), #       28000         9600
    (u'Cobra Right Leg Motion Trail'       ,             375), #         450          600
    (u'Tyrian Relax'                       ,            2000), #        2400         3000
    (u'Hydra Force'                        ,            2083), #        2500        30000
   #(u'Abs joint texture'                  ,               0), #           0        10000
   #(u'Adamantium Grip'                    ,            3666), #        4400          800
   #(u'Adamantium Right Leg Motion Trail'  ,            1125), #        1350          800
   #(u'Bronze Left Hand Motion Trail'      ,            2916), #        3500          140
    (u'Aurora Emote'                       ,             158), #         190          900
    (u'Adamantium Torso'                   ,            1831), #        2198         2400
    (u'Neptune Torso'                      ,             790), #         949         1200
    (u'Void Right Hand Motion Trail'       ,            1000), #        7999        18000
   #(u'Noxious DQ'                         ,            1333), #        1600          200
   #(u'Witch Hat'                          ,               0), #           0            0
    (u'Copper Right Leg Motion Trail'      ,             283), #         340          700
    (u'Viridian Torso'                     ,            1500), #        1800         6000
    (u'Viridian Right Hand Motion Trail'   ,             374), #         449         2000
   #(u'Olive Secondary Gradient'           ,             666), #         800          420
    (u'Copper Emote'                       ,             666), #         800          700
    (u'Quicksilver User Text'              ,            2500), #        3000         3200
    (u'Viridian Left Hand Motion Trail'    ,             665), #         799         2000
    (u'Elf Torso'                          ,            1999), #        2399        15000
    (u'Hydra Right Leg Motion Trail'       ,             334), #         401         2000
    (u'Kevlar Relax'                       ,            7666), #        9200        16000
    (u'Kung Fu Master Beard'               ,          140831), #      168998       200000
    (u'Quicksilver Torso'                  ,            3333), #        4000         4800
    (u'Acid Left Leg Motion Trail'         ,             416), #         500          600
    (u'Pure Timer'                         ,            1666), #        2000         4000
    (u'256x256 Left Pec Texture'           ,            7500), #        9000        10000
    (u'Shaman Grip'                        ,             415), #         499         1600
    (u'Demolition Relax'                   ,           29165), #       34999        44000
   #(u'DQ Sound'                           ,           26665), #       31999            0
   #(u'Spiky Hair'                         ,               0), #           0        50000
    (u'Supernova Torso'                    ,            2666), #        3200         7200
    (u'Pure Right Hand Motion Trail'       ,            1250), #        1500         2000
    (u'Typhon Primary Gradient'            ,             682), #         819          900
   #(u'Camo Hair'                          ,          833333), #     1000000          720
    (u'Hot Pink Ghost'                     ,            7405), #        8886        12000
   #(u'Red Submarine'                      ,           19750), #       23700            0
    (u'Static Right Hand Motion Trail'     ,            3583), #        4300        10000
    (u'Static Right Leg Motion Trail'      ,            4165), #        4999        10000
   #(u'Plasma Left Leg Motion Trail'       ,           16666), #       20000         3600
    (u'Typhon Left Hand Motion Trail'      ,             165), #         199          300
    (u'Cobra Blood'                        ,            4899), #        5879         6000
    (u'Pure Left Hand Motion Trail'        ,            1250), #        1500         2000
    (u'Pharos Grip'                        ,             707), #         849          900
    (u'Ivory Emote'                        ,             119), #         143          150
    (u'Raider Right Leg Motion Trail'      ,             740), #         888         3200
    (u'Kevlar Force'                       ,           19999), #       23999        24000
   #(u'Left shoulder joint texture'        ,               0), #           0        15000
    (u'Plasma Emote'                       ,             790), #         949         3600
    (u'Noxious Grip'                       ,             165), #         198          200
   #(u'Neck joint texture'                 ,               0), #           0        10000
    (u'Imperial Force'                     ,            5000), #       24899        75000 # TODO ^
    (u'Hunter Torso'                       ,             100), #           0         3000
    (u'Camo Emote'                         ,              30), #         150          240
    (u'Camo DQ'                            ,              30), #         198          240
    (u'Ivory Right Leg Motion Trail'       ,              20), #         148          150
    (u'Ivory Timer'                        ,              30), #         249          300
    (u'Camo Blood'                         ,             300), #        1200         2400
    (u'Typhon Torso'                       ,             100), #         475          900
    (u'Void Emote'                         ,             500), #       17000        18000
    (u'Acid User Text'                     ,              75), #        2000         1200
    (u'Quicksilver DQ'                     ,             100), #        1000         1600
    (u'Aurora User Text'                   ,             100), #        1500         1800
    (u'Void Left Leg Motion Trail'         ,            1000), #        9000        18000
    (u'Void Right Leg Motion Trail'        ,            1000), #       14000        18000
    (u'Candy Locks'                        ,           15000), #       39989        50000
    (u'Copper Primary Gradient'            ,             200), #        1999         2100
    (u'Camo User Text'                     ,              50), #         450          480
    (u'Mysterio Relax'                     ,            5000), #        6700        60000
    (u'Raptor Force'                       ,            3000), #        5999        30000
    (u'Platinum Secondary Gradient'        ,             500), #        6000         8400
    (u'Supernova Left Hand Motion Trail'   ,             300), #        2000         2400
    (u'Amber Ghost'                        ,             400), #        3500         7000
    (u'Crimson Torso'                      ,             500), #         849         8400
   #(u"Right Kickin' Kick"                 ,               0), #           0            0
   #(u"Left Kickin' Kick"                  ,               0), #           0            0
    (u'Magnetite Secondary Gradient'       ,             500), #        2000         8400
    (u'Magnetite Relax'                    ,            3000), #        6800        28000
    (u'Magnetite Primary Gradient'         ,             500), #        3000         8400
    (u'Tyrian DQ'                          ,              50), #         235          300
    (u'Shaman Primary Gradient'            ,             300), #        1450         4800
    (u'Bronze User Text'                   ,              50), #        2000          280
    (u'Pure Left Leg Motion Trail'         ,             250), #        1500         2000
    (u'Magnetite Ghost'                    ,            1500), #        6500        14000
    (u'Pure Emote'                         ,             300), #         900         2000
    (u'Persian Relax'                      ,            3000), #        8450        20000
    (u'Titan Left Leg Motion Trail'        ,              75), #         170          500
    (u'Typhon Left Leg Motion Trail'       ,              50), #         199          300
    (u'Typhon Timer'                       ,              50), #         400          600
    (u'Acid Timer'                         ,             100), #        4300         1200
    (u'Bronze Timer'                       ,              30), #         999          280
    (u'Persian Force'                      ,            5000), #       19908        30000
    (u'Demon Grip'                         ,             500), #           0        16000
    (u'Copper Ghost'                       ,             500), #        1900         3500
    (u'Raider Emote'                       ,             100), #           0         3200
    (u'Titan Primary Gradient'             ,             300), #         899         1500
    (u'Typhon Ghost'                       ,             300), #        1490         1500
    (u'Sapphire Ghost'                     ,             500), #        1500         2500
    (u'Crimson Ghost'                      ,             500), #        1199        14000
    (u'Noxious Ghost'                      ,             200), #         899         1000
    (u'Typhon Hair'                        ,             200), #         648          900
    (u'Supernova DQ'                       ,             500), #        1499         2400
    (u'Static Secondary Gradient'          ,             500), #           0        30000
    (u'Static Torso'                       ,            1000), #        7499        30000
    (u'Static Timer'                       ,             500), #           0        20000
    (u'Cobra Grip'                         ,             100), #         400          600
    (u'Velvet Force'                       ,            5000), #       19500        21000
    (u'Raider Right Hand Motion Trail'     ,             400), #        1950         3200
    (u'Raider Secondary Gradient'          ,             500), #           0         9600
    (u'Hydra Primary Gradient'             ,             500), #        1000         6000
    (u'Left knee joint texture'            ,            5000), #           0        15000
    (u'Plasma Ghost'                       ,            1000), #        2000        18000
    (u'Sapphire Grip'                      ,              60), #         400          500
    (u'Tyrian Left Hand Motion Trail'      ,              40), #         299          300
    (u'Neptune Blood'                      ,             500), #         900         4000
    (u'Neptune Grip'                       ,              50), #         368          400
    (u'Hunter DQ'                          ,             100), #           0         1000
    (u'Right shoulder joint texture'       ,            5000), #           0        15000
    (u'Right pecs joint texture'           ,            5000), #           0        15000
    (u'Adamantium Left Leg Motion Trail'   ,             300), #         666          800
    (u'Propeller Hat'                      ,            5000), #       90000            0
    (u'Bronze Grip'                        ,              40), #         139          140
    (u'Typhon Blood'                       ,             750), #        1999         3000
    (u'Neptune Right Leg Motion Trail'     ,              50), #         290          400
    (u'Aurora Force'                       ,            5000), #       13229        13500
    (u'Platinum Blood'                     ,            7500), #       12500        28000
])