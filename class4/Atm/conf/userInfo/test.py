import json

info = {
    "administrater": True,
    "TMALL": {
        "password": "zxbange",
        "shopping_cart": {
            "computer":{
                "count": 1,
                "price": 300
            }
        }
    },
    "CREDIT_CARD": {
        "password": "901020",
        "limit": 15000,
        "repay_day": 5
    }
}

f = open("abbott", "w")

json.dump(info, f)

f.close()