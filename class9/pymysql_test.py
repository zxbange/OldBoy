import pymysql
import time,datetime


# datetime时间转为字符串
def Changestr(datetime1):
    str1 = datetime1.strftime('%Y-%m-%d %H:%M:%S')
    return str1


# 字符串时间转为时间戳
def Changetime(str1):
    Unixtime = time.mktime(time.strptime(str1, '%Y-%m-%d %H:%M:%S'))
    return Unixtime


# datetime时间转为时间戳
def Changestamp(dt1):
    Unixtime = time.mktime(time.strptime(dt1.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'))
    return Unixtime


# 时间戳转为datetime时间
def Changedatetime(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt

# uinx时间戳转换为本地时间
def Localtime(datetime1):
    Localtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(datetime1))
    return Localtime


# 字符串时间转换函数
def Normaltime(datetime1):
    Normaltime = datetime.datetime.strptime(datetime1,'%Y-%m-%d %H:%M:%S')
    return Normaltime
# now_time = time.time()
# local_time = time.localtime(ct)
# data_head = time.strftime("%Y%m%d%H%M%S", local_time)

# now_time = datetime.datetime.strptime(time_set.next_time, "%Y-%m-%d %H:%M")
# now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
now_time = datetime.datetime.now()
print(now_time)
# dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# ts = time.time()
# timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
# print(timestamp)

# print(dt)
conn = pymysql.connect(host="192.168.50.11", port=3306, user="root",
                       password="root", db="bug-collect",  charset='utf8', cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()
# cursor.execute("select * from test;")
cursor.execute("insert into home_application_user(name,age,birth) values('zx',22,now_time)")
cursor.close()
conn.commit()
# result = cursor.fetchall()
conn.close()
# print(result)

result = [i for i in SystemInfo.objects.filter(Q(name__contains=get_data['keyword']) | Q(code__contains=get_data['keyword'])).values().to_dic()]
# def now_time():
#     ct = time.time()
#     local_time = time.localtime(ct)
#     data_head = time.strftime("%Y%m%d%H%M%S", local_time)
#     # data_secs = (ct - long(ct)) * 1000
#     # time_stamp = "%s%03d" % (data_head, data_secs)
#     print(data_head)
#
# now_time()

