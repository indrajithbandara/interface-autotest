#!/usr/bin/env python
#coding=utf-8
import amqplib.client_0_8 as amqp
def showmsg(msg):
    print msg.body
    msg.channel.basic_ack(msg.delivery_tag)
    if msg.body == 'quit':
        msg.channel.basic_cancel(msg.consumer_tag)
def main():
    server = {'host':'localhost', 'userid':'linvo', 'password':'111', 'ssl':False}
    x_name = 'x1'
    q_name = 'q1'
    conn = amqp.Connection( server['host'],
                            userid=server['userid'],
                            password=server['password'],
                            ssl=server['ssl'])
    ch = conn.channel()
    ch.access_request('/data', active=True, read=True)
    ch.exchange_declare(exchange=x_name, type='fanout', durable=True, auto_delete=False)
    ch.queue_declare(queue=q_name, durable=True, exclusive=False, auto_delete=False)
    ch.queue_bind(queue=q_name, exchange=x_name)
    ch.basic_consume(q_name, callback=showmsg)
    while ch.callbacks:
        ch.wait()
    ch.close()
    conn.close()
if __name__ == '__main__':
    main()