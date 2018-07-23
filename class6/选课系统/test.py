
func_dict = {}
#
# def make_route(num):
#     def inner(func):
#         func_dict[num] = func
#     return inner
#
#
# @make_route("1")
# def manager():
#     print("manager")
#
#
# def run():
#     msg = '''
#     1.管理员登录
#     2.讲师登录
#     3.学员登录
#     4.学员注册
#     5.退出
#     '''
#     while True:
#         print(msg)
#         num = input('num>>>:').strip()
#         if num in func_dict:
#             func_dict[num]()
#         else:
#             print('\033[1;31m请重新输入正确的序号！\033[0m')
#
#
# run()

address = [{1: "上海"}, {2: "北京"}]
for i in address:
    for key in i:
        print(key, i[key])