import json
from bin import atm


def auth(auth_type):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if auth_type == "tmall":
                print(args)
                if args[0]["tmall_status"]:
                    print(args)
                    func(*args, **kwargs)
                else:
                    args[0]["acc_name"] = input("Please Input Yout Name:")
                    res = login_auth("TMALL", acc_info)
                    if res:
                        func(*args, **kwargs)
            elif auth_type == "credit_card":
                if acc_info["credit_card_status"]:
                    func(*args, **kwargs)
                else:
                    acc_info["acc_name"] = input("Please Input Yout Name:")
                    res = login_auth("CREDIT_CARD", acc_info)
                    if res:
                        func(*args, **kwargs)
            elif auth_type == "administrator":
                pass
        return wrapper
    return outer_wrapper




def login_auth(platform):
    # this function is judge that your password is correct
    username = input("Please Input Your Name:")
    base_dir = atm.BASE_DIR
    file = base_dir + "/conf/userInfo/%s" %username
    times = 0
    info = {}
    try:
        with open(file, "r") as f:
            info = json.load(f)
    except FileNotFoundError:
        exit("Not a valid Account")
    while times < 3:
        password = input("Please Input Your Password")
        if password == info[platform]["password"]:
            return username
        else:
            print("Incorret Password")
            times += 1
    else:
        exit("Your Account is Locked")
