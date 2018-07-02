

def foo():
    print("in the foo")
    def func():
        print("in the func")
    func()

foo()