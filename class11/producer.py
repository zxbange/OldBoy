import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")    # 创建一个链接
)

channel = connection.channel()  # 创建一个管道，可有多个队列

channel.queue_declare(queue="hello", durable=True)  # 声明一个队列 durable表示持久化，就是rabbitmq服务挂了再启动不会丢失队列

channel.basic_publish(exchange="",
                      routing_key="hello",
                      body="hello world",
                      properties=pika.BasicProperties(
                          delivery_mode = 2,  # 这是将消息持久化。上面durable只是让队列持久化，消息依然会丢失
                      ))


print(" [x] sent  'hello world' ")
connection.close()