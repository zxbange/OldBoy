

import time


def timer(func):  # timer(test1) --> func=test1
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print("the function is cost %s sec" %(stop_time-start_time))
    return deco


@timer  # test1=timer(test1)
def test1():
    time.sleep(1)
    print("in the test1")


# @timer
# def test2(name="bbb"):
#     print("name", name)



# test1=timer(test1)
test1()  # --> deco()
test2("Abbott")