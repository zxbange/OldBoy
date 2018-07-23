from core.manager import Manager
from libs.login import login


role_list = {}


def run():
    menu = '''==========选课系统============
    1. 管理员
    2. 学生
    3. 老师
    4. 退出
    '''
    while True:
        print(menu)
        num = input("who are you: ")
        if num in role_list:
            role_list[num]()
        else:
            print("It is not a good choice!")
            run()


def choice_role(num):
    def inner(func):
        role_list[num] = func
    return inner


@choice_role("1")
def administrator():
    user = login("manager")
    if user and user["identified"] == "manager":
        admin = Manager('admin')
        while True:
            for index, i in enumerate(admin.manager_list,start=1):
                print("%s: %s" % (index, i[0]))
            choice_act = int(input("请选择：").strip())
            if choice_act <= len(admin.manager_list):
                getattr(admin, admin.manager_list[choice_act-1][1])()
            else:
                print("选择错误！请重新选择")


@choice_role("2")
def student():
    pass


@choice_role("3")
def teacher():
    pass

# run()
