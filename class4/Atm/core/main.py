
from core import auth


acc_info = {
    "acc_id": None,
    "acc_status": None,
}


def run():
    #  choose which platform you want login
    platformSelect = input('''
choose which platform you want login:
1. TMALL
2. Credit Card Center
your choice:''')
    if platformSelect == "1":
        auth.tmall_auth()
    elif platformSelect == "2":
        auth.credit_card_auth()
    else:
        print("Not a good choice")
