from libs.my_pickle import Mypickle
from conf import settings
from core import school


class Manager(object):

    manager_list = [("创建学校", "create_school"), ("招聘老师", "create_teacher"),
                    ("创建课程", "create_course"), ("创建班级", "create_class")]

    def __init__(self, name):
        self.name = name
        self.school_path = Mypickle(settings.SCHOOL_PATH)

    def create_school(self):
        """
        创建学校，输入学校名称和地址
        然后再用pickle序列化到文件中
        """
        school_addr = ""
        school_name = input("school_name>>>: ").strip()
        address = {
            1: "上海",
            2: "北京"
        }
        for key in address:
            print(key,address[key])
        num = input("选择你要在哪里办校：").strip()
        if num in address:
            school_addr = address[num]
        sch = school.School(school_name, school_addr)
        self.school_path.dump(sch)
