import pickle



def sayhi(name):
    print("Hello,", name)

f = open("test1.txt", "rb")
data = pickle.loads(f.read())
print(data)
f.close()