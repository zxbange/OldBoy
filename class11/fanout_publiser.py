import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

# 这里是广播，所以不需要声明queue，routing_key也不需要指定
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

# message = ' '.join(sys.argv[1:]) or "info: Hello World!"
message = "info: Hello World!"

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()