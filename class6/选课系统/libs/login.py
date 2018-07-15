from conf import settings
from libs.my_pickle import Mypickle
import os

def login(type):
    while True:
        username = input("请输入用户名：").strip()
        password = input("请输入密码：").strip()
        path = settings.USERINFO_PATH
        if os.path.isfile(path):
            data = Mypickle(path).load()
            for i in data:
                # print(i)
                if i["identified"] == type:
                    if i["name"] ==username:
                        if i["password"] == password:
                            print('welcome'.center(20, '='))
                            return {'user': username, 'identified': i["identified"]}
                        else:
                            print("用户名密码错误")
                            break
        else:
            print("暂无用户")