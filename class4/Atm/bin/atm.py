import os, sys

# print(__file__)  # 打印相对路径
#
# print(os.path.abspath(__file__))  # 打印绝对路径
#
# print(os.path.dirname(os.path.abspath(__file__)))  # 打印父路径

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from conf import settings

from core import main