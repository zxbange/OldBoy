from wsgiref.simple_server import make_server
import time

'''
"hello,world".encode("utf8")
bytes("hello,world", encoding="utf8")
b"hello,world"
'''


def handle_index():
    v = str(time.time())
    f = open("index.html", mode='rb')
    data = f.read()
    f.close()
    data = data.replace(b"@uuu", v.encode("utf8"))
    return [data, ]


def handle_data():
    return [bytes('<h1>Hello, data!</h1>', encoding='utf-8'), ]

URL_DICT = {
    "/index": handle_index,
    "/data": handle_data,
}


def RunServer(environ, start_response):
    # environ 封装了客户端所有的请求
    # start_response 封装要返回给用户的数据，相应头和状态
    current_url = environ['PATH_INFO']
    start_response('200 OK', [('Content-Type', 'text/html')])
    func = None
    if current_url in URL_DICT:
        func = URL_DICT[current_url]
    if func:
        return func()

    # if current_url == "/index":
    #     return handle_index()
    # elif current_url == "/data":
    #     return handle_data()
    else:
        return [bytes('<h1>404</h1>', encoding='utf-8'), ]
    # # 返回的内容
    # return [bytes('<h1>Hello, web!</h1>', encoding='utf-8'), ]

if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()

