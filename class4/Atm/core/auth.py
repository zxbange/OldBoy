import json
from bin import atm


def acc_login(acc_info, platform):
    acc_info["ACC_NAME"] = input("Please Input Your Name: ")
    base_dir = atm.BASE_DIR
    file = base_dir + "\\db\\%s" %acc_info["ACC_NAME"]
    times = 0
    info = {}
    try:
        with open(file, "r") as f:
            info = json.load(f)
    except FileNotFoundError:
        exit("Not a valid Account")
    while times < 3:
        password = input("Please Input Your Password: ")
        if password == info[platform]["password"]:
            acc_info[platform] = True
            return acc_info
        else:
            times += 1
            print("Incorret Password")
    else:
        exit("Your Account is Locked")


def auth(auth_type):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if auth_type == "tmall":
                print(args)
                if args[0]["tmall_status"]:
                    print(args)
                    func(*args, **kwargs)
                else:
                    res = login_auth("TMALL", args)
                    if res:
                        func(*args, **kwargs)
            elif auth_type == "credit":
                if args[0]["credit_card_status"]:
                    func(*args, **kwargs)
                else:
                    res = login_auth("CREDIT_CARD", args)
                    if res:
                        func(*args, **kwargs)
            elif auth_type == "administrator":
                if args[0]["tmall_status"]:
                    pass
        return wrapper
    return outer_wrapper



