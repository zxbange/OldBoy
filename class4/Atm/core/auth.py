import json
from bin import atm


def auth():
    def wrapper(*args,**kwargs):
        acc_statuts = acc_info[""]


def login_auth(platform):
    '''this function is judge that your password is correct'''
    username = input("Please Input Yout Name:")
    base_dir = atm.BASE_DIR
    file = base_dir + "\\conf\\userInfo\%s" %username
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
            return (True, username)
        else:
            print("Incorret Password")
            times += 1
    else:
        exit("Your Account is Locked")

def credit_card_auth():
    pass