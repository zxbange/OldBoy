import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()  # 继续创建一个通道

channel.queue_declare(queue='hello', durable=True)  # 这里需要再次声明队列名称，否则先徐宁消费后生产，会报错找不到callback
#You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
#was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.


def callback(ch, method, properties, body):  # 回调函数
    print(ch, method, properties)
    # time.sleep(30)
    print("[x] is recived %r" % body )
    ch.basic_ack(delivery_tag=method.delivery_tag)  # no_ack=False时，需要手动给producer确认

channel.basic_qos(prefetch_count=1)   # 处理完这一条才会发下一条
channel.basic_consume(callback,
                      queue = 'hello',
                      # no_ack = True   #
                      )

print("[x] waiting for messages, To exist prress CRL")

channel.start_consuming()