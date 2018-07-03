#-*- coding:UTF-8 -*-

import json


info = {
    "name": "zhangxin",
    "age": 22,
    "sex": "male"
}

f = open("test.txt", "w")

# print(json.dumps(info)) 将其变为了字符串
# f.write(json.dumps(info))
json.dump(info, f)


# info["age"] = 21
# json.dump(info, f)  # 将会生成两个字典存进取, 但是无法load，会报错，所以建议只dump一次，只load一次

f.close()