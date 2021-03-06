#!/usr/bin/env python
import pika
import time
from influxdb import InfluxDBClient
import json

credentials = pika.PlainCredentials('admin', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1',credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='local_queue', durable=True)

client = InfluxDBClient(host='localhost', port=8086)
client.create_database('server')
client.get_list_database()
client.switch_database('server')





print("waiting for message")

def callback(ch, method, properties, body):
    #time.sleep(body.count(b'.'))
    ch.basic_ack(delivery_tag = method.delivery_tag)
    test1=body.decode("utf-8")
    #print("\nfrom pi got",body)
    json_write=json.loads(test1)
    print("\n\nReceived from car-\n",test1)
    #print(type(json_write))
    ltodb=[json_write]
    print("Data added to influx- ",client.write_points(ltodb))

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='local_queue')
channel.start_consuming()



#print(json_write)
#client.write_points(json_write)

#result=client.query('SELECT "duration" FROM "server_test"."autogen"."car" WHERE time > now() - 4d GROUP BY "user"')

#points = result.get_points(tags={'user':'Saurabh'})
#print(points)


