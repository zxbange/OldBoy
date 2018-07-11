
import json
from bin import atm



def buy_option(acc_info):
    base_dir = atm.BASE_DIR
    file1 = base_dir + "\\db\\shop_list"
    with open(file1, "r") as f:
        shop_list = json.load(f)
        num = 1
        for i in shop_list:
            list = '''%s: %s   price:%s''' %(num, i["key"], i["price"])
            print(list)
    buy_num = int(input("Please Input Which Your Want Buy: ")) - 1
    stuff = shop_list[buy_num]
    # print(stuff["key"])
    file2 = base_dir + "\\db\\%s" %acc_info["ACC_NAME"]
    with open(file2, "r") as f2:
        user_info = json.load(f2)
        # print(user_info)
        if stuff["key"] in user_info["TMALL"]["shopping_cart"]:
            user_info["TMALL"]["shopping_cart"][stuff["key"]]["count"] = user_info["TMALL"]["shopping_cart"][stuff["key"]]["count"] + 1
        else:
            user_info["TMALL"]["shopping_cart"][stuff["key"]] = {"count":1,"price": stuff["price"]}
            # print(user_info)
    with open(file2, "w") as f3:
        json.dump(user_info, f3)


