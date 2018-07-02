import pickle


def sayhi(name):
    print("Hello,", name)


info = {
    "name": "zhangxin",
    "age": 22,
    "func": sayhi
}

f = open("test1.txt", "wb")
# print(pickle.dumps(info)) 将其变为了二进制
pickle.dump(info, f)

f.close()