# -*- coding:utf-8 -*-
'''
基于redis双集合结构的定时触发操作demo
  一个集合用来存储时间节点
  另一个集合用来存储对应时间点的操作数据
  集合的添加、删除操作由另外文件操作
'''
import threading
import time
import redis

connection = redis.Redis(host='localhost', port=6379, decode_responses=True)
connection.flushall()

# 初始化添加时间节点
# connection.rpush('timer','23:43','23:45','23:50')
connection.sadd('timer', '16:31','15:40','16:26')

print('待执行时间队列：',connection.smembers('timer'))

# 对应时间节点添加操作数据
min_time = min(connection.smembers('timer'))
# print(min_time)

for index, item in enumerate(connection.smembers('timer')):
  connection.sadd('timer-'+item, 0+index, 1+index)
  print(item, connection.smembers('timer-'+item))

print()

def work():
  t = threading.Timer(1, work)
  current_time = time.strftime('%X', time.localtime())

  if connection.smembers('timer'):
    min_time = min(connection.smembers('timer'))
    if min_time <= current_time:
      print(connection.smembers('timer-'+min_time), 'coming')
      for item in connection.smembers('timer-'+min_time):
        connection.srem('timer-'+min_time, item)
        print(item, 'deleting')
      connection.srem('timer',min_time)

      for index, item in enumerate(connection.smembers('timer')):
        # connection.sadd('timer-'+item, 0+index, 1+index)
        print(item, connection.smembers('timer-'+item))
      t.start()
    else:
      print(connection.smembers('timer-'+min_time), 'waiting')
      t.start()
  else:
    t.cancel()


work()


