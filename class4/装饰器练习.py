
username = 'abbott'
user_list = ['abbott','zx','bange']

def auth(username):
    def decorater(func):
        def _wrapper(*args, **kwargs):
            if username in user_list:
                func()
            else:
                print("权限不够")
        return _wrapper
    return decorater


@auth("bange1")
def run_task():
    print("成功")


run_task()