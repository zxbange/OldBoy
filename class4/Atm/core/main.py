
from core import auth
from core import tmall


acc_info = {
    "acc_name": None,
    "acc_id": None,
    "tmall_status": False,
    "credit_card_status": False
}


def tmall_ption():
    option_select = input('''
=========welcome to tmall!============
|        choose you option           |
|    1. buy some thing               |
|    2. check my shopping cart       |
|    3. check out                    |
|    4. QUIT                         |
======================================
Please input your option''')

    if option_select == "1":
        tmall.to_shop()
    elif option_select == "2":
        tmall.check_cart()
    elif option_select == "3":
        tmall.check_out()
    elif option_select == "4":
        return False
    else:
        print("not a good choise!")

def credit_card_option():
    option_select = input('''
=======welcome to Credit Card Center!========
|            choose you option              |
|        1. buy some thing                  |
|        2. check my shopping cart          |
|        3. check out                       |
|        4. QUIT                            |
=============================================
Please input your option''')
    if option_select == "1":
        tmall.to_shop()
    elif option_select == "2":
        tmall.check_cart()
    elif option_select == "3":
        tmall.check_out()
    elif option_select == "4":
        return False
    else:
        print("not a good choise!")


@auth.auth
def run(acc_info):
    #  choose which platform you want login
    platformSelect = input('''
===choose which platform you want login===
1. TMALL
2. Credit Card Center
3. Manage Account
your choice:''')
    platform = ""
    flag = True
    if platformSelect == "1":
        platform = "TMALL"
    elif platformSelect == "2":
        platform = "CREDIT_CARD"
    else:
        print("Not a good choice")

    if platformSelect == "1":
        acc_info["tmall_status"], acc_info["acc_name"] = auth.login_auth(platform)
        while flag:
            flag = tmall_ption()
        else:
            run()
    else:
        acc_info["credit_card_status"], acc_info["acc_name"] = auth.login_auth(platform)
        while flag:
            flag = credit_card_option()
        else:
            run()


