class AbbottException(Exception):
    def __init__(self, msg):
        self.message = msg

    # def __str__(self):
    #     return self.message



try:
    raise AbbottException('数据库连不上')
except AbbottException as e:
    print(e)