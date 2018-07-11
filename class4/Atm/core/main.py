
from core import auth
from core import tmall
from bin import atm
import json


acc_info = {
    "ACC_NAME": None,
    "TMALL": False,
    "CREDIT_CARD": False,
}


def run():
    platformSelect = ""
    platform = input('''
    1. TMALL
    2. CREDIT CARD
    3. QUIT
    Please choose your option: ''')
    if platform == "1":
        platformSelect = "TMALL"
        res = auth.acc_login(acc_info, platformSelect)
        tmall_interactive(res)
    elif platform == "2":
        platformSelect ="CREDIT_CARD"
        res = auth.acc_login(acc_info, platformSelect)
        credit_interactive(res)
    elif platform == "3":
        exit("Hope to come again!")



def tmall_interactive(acc_info):
    menu = '''
    1. Buy something
    2. Check shopping cart
    3. Check out
    4. quit
    Please input your option: '''
    menu_dict = {
        "1": "buy",
        "2": "shopping_cart",
        "3": "checkout",
        "4": "logout"
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dict:
            exit_flag = do_real_thing(acc_info, menu_dict[user_option])
        else:
            print("It's not a good choose!")

def do_real_thing(acc_info, option):
    if option == "buy":
        tmall.buy_option(acc_info)
    elif option == "shoping_cart":
        tmall.go_shopping(acc_info)
    elif option == "checkout":
        tmall.check_out(acc_info)
    else:
        return True




def credit_interactive(acc_info):
    pass