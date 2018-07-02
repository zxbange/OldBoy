

user, passwd = "abbott", "123"


def auth(func):
    def wrapper(*agrs, **kwargs):
        username = input("Username:")
        passwrod = input("Password:")
        if user == username and passwd == passwrod:
            print("\033[32;1mUser has passed authentication\033[0m")
            res = func()
            print("----------after authentication-----------")
            return res
        else:
            exit("\033[31;1mInvalied user or password\033[0m")
    return wrapper


def auth2(auth_type):
    def outer_wrapper(func):
        def wrapper(*agrs, **kwargs):
            if auth_type == "local":
                username = input("Username:")
                passwrod = input("Password:")
                if user == username and passwd == passwrod:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    res = func()
                    print("----------after authentication-----------")
                    return res
                else:
                    exit("\033[31;1mInvalied user or password\033[0m")
            elif auth_type == "ldap":
                print("不会，草")
        return wrapper
    return outer_wrapper


@auth  # 当这里没有传参数的时候，会将index作为参数传入，所以 index = wrapper
def index():
    print("in the index")


@auth2(auth_type="local") # 当这里有参数传入的时候，会先执行最外层，返回一个结果，然后再将home作为参数传入，所以 home = wrapper
def home():
    print("in the home")
    aaa = "from home"
    return aaa


@auth2(auth_type="ldap")
def bbs():
    print("in the bbs")


index()
bbb = home() # bbb = wrapper() = home()
print(bbb)
bbs()