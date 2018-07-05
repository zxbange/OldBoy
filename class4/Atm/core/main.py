
from core import auth
from core import tmall


acc_info = {
    "acc_name": None,
    "tmall_status": False,
    "credit_card_status": False
}


def run():
    #  choose which platform you want login
    platformSelect = input('''
===choose which platform you want login===
1. TMALL
2. Credit Card Center
3. Manage Account
4. QUIT
your choice:''')
    acc_info["acc_name"] = input("Please Input Your Name: ")
    if platformSelect == "1":
        flag = True
        while flag:
            flag = check_tmall_status(acc_info)
        else:
            run()
    elif platformSelect == "2":
        check_credit_status(acc_info)
    elif platformSelect == "3":
        check_administrator_status(acc_info)
    elif platformSelect == "4":
        exit("Hope to come again!")
    else:
        print("Not a good choice")


@auth.auth("tmall")
def check_tmall_status(acc_info):
    acc_info["tmall_status"] = True
    option_select = input('''
    =========welcome to tmall!============
    |        choose you option           |
    |    1. buy some thing               |
    |    2. check my shopping cart       |
    |    3. check out                    |
    |    4. QUIT                         |
    ======================================
    Please input your option:''')

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

@auth.auth("credit")
def check_credit_status(acc_info):
    acc_info["credit_card_status"] = True
    option_select = input('''
    =======welcome to Credit Card Center!========
    |            choose you option              |
    |        1. buy some thing                  |
    |        2. check my shopping cart          |
    |        3. check out                       |
    |        4. QUIT                            |
    =============================================
    Please input your option:''')
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

@auth.auth("tmall")
def check_administrator_status(acc_info):
    acc_info["tmall_status"] = True
    pass