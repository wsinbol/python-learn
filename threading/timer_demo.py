# -*- coding:utf-8 -*-

'''
flush_time_list：待刷新的时间列表
当前时间大于列表中的最小时间：立即弹出列表中时间
当前时间小于列表中最小的时间：执行等待过程
列表中元素为空时：停止定时器操作
待补充部分：
linux定时触发操作
flush_time_list由redis操作
'''

import threading
flush_time_list = ['18:03','18:05','18:10']

def work (): 
  t = threading.Timer(1, work)
  current_time = time.strftime('%X', time.localtime())
  
  if len(flush_time_list) > 0:
  	if flush_time_list[0] <= current_time:
	  	if len(flush_time_list) == 0:
	  		print('doing')
	  		t.cancel()
	  	else:
	  		t.start()
	  		print(flush_time_list.pop(0))
  else:
  	t.cancel()

work()