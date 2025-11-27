import pywmapi as wm
from pywmapi.common import Platform

def get_syndicate():
    syndicates = {
        1: 'ArbitersOfHexis',
        2: 'CephalonSuda',
        3: 'NewLoka',
        4: 'RedVeil',
        5: 'SteelMeridian',
        6: 'ThePerrinSequence',
    }

    while True:
        try:
            choice = int(input('''What syndicate do you have standing with?
1. Arbiters Of Hexis
2. Cephalon Suda
3. New Loka
4. Red Veil
5. Steel Meridian
6. The Perrin Sequence

Syndicate: '''))
            if choice in syndicates:
                return syndicates[choice]
        except ValueError:
            pass
        print("Invalid input. Enter a number 1-6.")
    


def filter_orders(orders):
    online = []
    for order in orders:
        if ('ingame' in str(order.user.status)) and ('buy' in str(order.order_type)):
            online.append(order)
    return online

def multi_plat_orders(item):
    platforms = [Platform.pc, Platform.xbox, Platform.switch, Platform.ps4]

    orders = []
    for platform in platforms:
        platform_orders = wm.orders.get_orders(item, platform)
        if platform_orders:
            for order in platform_orders:
                orders.append(order)
    return orders

def get_weapon_list(syndicate):
    file_path = f"./Weapons/{syndicate}.txt"

    with open(file_path, 'r') as file:
        weapon_list = file.readlines()

    weapon_list = [line.strip() for line in weapon_list]
    
    for weapon in weapon_list:
        weapon_orders = multi_plat_orders(weapon)
        weapon_orders = filter_orders(weapon_orders)
        if weapon_orders:
            print(f"Weapon: {weapon}")
            for order in weapon_orders:
                print(f"{order.platinum}p for {order.quantity} unit(s) by {order.user.ingame_name}")
            print("-----------")
        


def get_mod_list(syndicate):
    file_path = f"./Mods/{syndicate}.txt"

    with open(file_path, 'r') as file:
        mod_list = file.readlines()

    mod_list = [line.strip() for line in mod_list]

    mod_dict = {}
    
    for i, mod in enumerate(mod_list):
        print(str(i) + "/" + str(len(mod_list)) + " mods checked.")
        mod_orders = multi_plat_orders(mod)
        mod_orders = filter_orders(mod_orders)
        if mod_orders:
            for order in mod_orders:
                if mod not in mod_dict:
                    mod_dict[mod] = [order]
                if mod in mod_dict:
                    mod_dict[mod].append(order)

    print("==================")

    mod_count = len(mod_dict.keys())
    if mod_count == 0:
        print("No orders found.")
    if mod_count == 1:
        print("There was " + str(len(mod_dict.keys())) + " item found with orders.")
    else:
        print("There were " + str(len(mod_dict.keys())) + " items found with orders.")
    
    print("-------------------")
    for modName, modOrders in mod_dict.items():
        print(modName + " orders: ")
        for order in modOrders:
            print(f"{order.platinum}p for {order.quantity} unit(s) by {order.user.ingame_name}")
    print("-------------------")
    print("==================")


def choice(syndicate):
    choosing = True
    while choosing:
        items = input("Weapons (W) or Mods (M)? ")
        if items.lower() == 'w':
            print("\n")
            weapon_orders = get_weapon_list(syndicate)
            choosing = False
        elif items.lower() == 'm':
            print("\n")
            mod_orders = get_mod_list(syndicate)
            choosing = False
        else:
            print("Please enter W or M")