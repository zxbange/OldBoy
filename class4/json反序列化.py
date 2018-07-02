import json

# f = open("test.txt", "r")
# data = eval(f.read())
#
# f.close()
#
# print(data["age"])

f = open("test.txt", "r")
# data = json.loads(f.read())
data = json.load(f)
print(data)
f.close()