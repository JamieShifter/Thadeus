import random as r
import dnd_data




def roll(x, y):
    wynik = 0
    for i in range(y):
        wynik += r.randint(1, x)
    return wynik

def randomize_money(level):
    copper = 0
    silver = 0
    gold = 0
    electrum = 0
    platinum = 0
    if level == 0:
        copper = r.randint(0, 100)
        silver = r.randint(0, 10)
        gold = r.randint(0, 10)
        electrum = 0
        platinum = 0
    elif level == 1:
        copper = r.randint(0, 100)
        silver = r.randint(0, 100)
        gold = r.randint(0, 30)
        electrum = r.randint(0, 2)
        platinum = 0
    elif level == 2:
        copper = 0
        silver = r.randint(0, 100)
        gold = r.randint(0, 200)
        electrum = r.randint(0, 100)
        platinum = r.randint(0, 7)
    elif level == 3:
        copper = 0
        silver = r.randint(0, 100)
        gold = r.randint(0, 400)
        electrum = r.randint(0, 200)
        platinum = r.randint(0, 17)
    elif level == 4:
        copper = r.randint(0, 100)
        silver = r.randint(0, 100)
        gold = r.randint(0, 1000)
        electrum = 0
        platinum = r.randint(0, 22)
    elif level == 5:
        copper = r.randint(0, 100)
        silver = r.randint(0, 100)
        gold = r.randint(0, 1000)
        electrum = 0
        platinum = r.randint(0, 100)
    elif level == 6:
        copper = 0
        silver = 0
        gold = r.randint(0, 1000)
        electrum = r.randint(0, 1000)
        platinum = r.randint(0, 100)
    else:
        pass
    moneybag = {
        "cp": copper,
        "sp": silver,
        "gp": gold,
        "ep": electrum,
        "pp": platinum
    }
    return moneybag

def calculate_money(moneybag):
    worth = 0
    worth += int(moneybag['cp'])/100 if 'cp' in moneybag else 0
    worth += int(moneybag['sp'])/10 if 'sp' in moneybag else 0
    worth += int(moneybag['gp']) if 'gp' in moneybag else 0
    worth += int(moneybag['ep'])/2 if 'ep' in moneybag else 0
    worth += int(moneybag['pp'])*10 if 'pp' in moneybag else 0
    return format(worth, '.2f')


def countDeathSavingThrows(target):
    # calculated in runtime
    if target.death_saves["failure"] >= 3:
        target.physical_state = "dead"
    elif target.death_saves["success"] >= 3:
        target.hp = 1
        target.physical_state = "normal"
        target.resetDeathSavingThrows()


def randomizedItemList(level):
    max_quantity_for_level_index = [4, 6, 8, 10, 11, 12, 13, 14, 16]
    itemlist = dnd_data.itemlist
    quantity_of_items = r.randint(0, max_quantity_for_level_index[level])
    indexes = list(range(0, quantity_of_items))
    gained_items = []
    for i in indexes:
        num = r.randint(0, len(itemlist[level]))
        gained_items.append(itemlist[level][num])
    return gained_items








if __name__=="__main__":
    mon = {'cp': 0, 'sp': 19, 'gp': 159, 'ep': 3, 'pp': 1}
    calculate_money(mon)
