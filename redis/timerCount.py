# -*- coding:utf-8 -*-
'''
基于redis列表结构的定时触发操作demo
	需要在其他文件中对timer进行添加元素操作
'''
import threading
import time
import redis

connection = redis.Redis(host='localhost', port=6379, decode_responses=True)
'''
connection.lpop('timer')
connection.rpush('timer','23:43','23:45','23:50')
print('待执行时间队列：',connection.lrange('timer', 0, -1))
'''
print('待执行时间队列：',connection.lrange('timer', 0, -1))

def work (): 
  t = threading.Timer(1, work)
  current_time = time.strftime('%X', time.localtime())

  if connection.lindex('timer',0):
  	if connection.lindex('timer', 0) <= current_time:
  		print(connection.lindex('timer', 0),'doing...')
  		connection.lpop('timer')
  		t.start()
  	else:
  		print(connection.lindex('timer', 0),'waiting...')
  		t.start()
  else:
  	t.cancel()

work()