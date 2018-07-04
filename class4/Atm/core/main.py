
from core import auth
from core import tmall


acc_info = {
    "acc_name": None,
    "tmall_status": False,
    "credit_card_status": False,
    "administrator_status": False
}


def run():
    #  choose which platform you want login
    platformSelect = input('''
===choose which platform you want login===
1. TMALL
2. Credit Card Center
3. Manage Account
your choice:''')

    if platformSelect == "1":
        check_login_status("tmall_status")
    elif platformSelect == "2":
        check_login_status("credit_card_status")
    elif platformSelect == "3":
        check_login_status("administrator_status")
    else:
        print("Not a good choice")


def check_login_status(platform):
    if acc_info[platform]:
        do_run(platform)
    else:
        username = auth.login_auth(platform)
        acc_info["acc_name"] = username
        acc_info[platform] = True
        do_run(platform)


def do_run(platform):
    if platform == "tmall_status":
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

    elif platform == "credit_card_status":
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

    else:
        pass
