import pywmapi as wm
from pywmapi.common import Platform
import os

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

def get_order_list(syndicate, folder):
    file_path = f"./{folder}/{syndicate}.txt"

    with open(file_path, 'r') as file:
        item_list = file.readlines()

    item_list = [line.strip() for line in item_list]

    item_dict = {}
    
    for i, item in enumerate(item_list):
        print(str(i) + "/" + str(len(item_list)) + f"{folder.lower()} checked.")
        item_orders = multi_plat_orders(item)
        item_orders = filter_orders(item_orders)
        if item_orders:
            for order in item_orders:
                if item not in item_dict:
                    item_dict[item] = [order]
                if item in item_dict:
                    item_dict[item].append(order)

    print("==================")

    item_count = len(item_dict.keys())
    if item_count == 0:
        print("No orders found.")
    if item_count == 1:
        print("There was " + str(len(item_dict.keys())) + f" {folder.lower()} found with orders.")
    else:
        print("There were " + str(len(item_dict.keys())) + f" {folder.lower()} found with orders.")
    
    print("-------------------")
    for itemName, itemOrders in item_dict.items():
        print(itemName + " orders: ")
        for order in itemOrders:
            print(f"{order.platinum}p for {order.quantity} unit(s) by {order.user.ingame_name}")
    print("-------------------")
    print("==================")


def choice(syndicate):
    choosing = True
    folders = [f for f in os.listdir() if os.path.isdir(f) if not f[0] == "_" if not f[0] == "."]
    if not folders:
        print("No folders found. Please add a folder with lists of items.")

    while choosing:
        print("Please choose an item from the options below: ")
        for i, folder in enumerate(folders):
            print(str(i) + ". " + folder)
        folderChosen = input("Please enter a number from 0-" + str(len(folders) - 1) + ": ")

        if (0 <= int(folderChosen) < len(folders)):
            print("\n")
            orders = get_order_list(syndicate, folders[int(folderChosen)])
            choosing = False
        else:
            print("Invalid selection.")