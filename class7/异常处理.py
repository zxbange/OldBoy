# def bulk(self):
#     print("%s is yelling..." %self.name)
#
#
# class Dog(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self, food):
#         print("%s is eating %s" %(self.name, food))
#
#     # def talk(self):
#     #     print("%s is bulking..." %self.name)
#
#
# d = Dog("Alex")
# choice = input(">>:").strip()
# 缩进错误和语法错误无法抓取
names = [1,2,3]
date = {}
try:
    # open("test.txt")
    # names[3]
    data['name']
    a = 1
    print(a)


except IndexError as e:
    print("错误",e)
except NameError as e:
    print("错误",e)


except Exception as e:
    print("未知错误",e)

else:  # 如果没有错执行这个
    print("一切正常")

finally:
    print("不管有没有错，都执行")