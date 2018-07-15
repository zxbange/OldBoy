import pickle

# info = {
#         "name": "admin",
#         "identified": "manager",
#         "password": "123456"
# }
#
# with open("userinfo.pkl", "wb") as f:
#     pickle.dump(info,f)

with open("school.pkl", 'rb') as f:
    data = pickle.load(f)

print(data)