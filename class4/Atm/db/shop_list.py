import json

info = [
    {"key": "computer", "price": 6000},
    {"key": "pen", "price": 30},
    {"key": "cup", "price": 50},
    {"key": "notebook", "price": 100},
    {"key": "desktable", "price": 500},
]
f = open("shop_list", "w")

json.dump(info, f)

f.close()