
'''
文件读取操作
共4种方法
前3种方法 print 会有多余换行，但是写入文件时却没有问题
'''

file_name = 'yewu.txt'

'''
# 1
# for in 结构读取文件, 不借助文件读取函数，返回 str 结构
with open(file_name, 'r') as f:
	for line in f:
		print(line)
'''

'''
# 2
# readline 每次只读一行文件, 返回 str 结构
content = ''
with open(file_name, 'r') as f:
	line = f.readline()
	while line:
		# print(line)
		with open('yewu2.txt', 'a') as wf:
			wf.write(line)
		content += line
		line = f.readline()
'''


'''
# 3
# readlines 一次性读取文件所有行，返回 list 结构
with open(file_name, 'r') as f:
	lines = f.readlines()
	for line in lines:
		print(line)
'''

'''
# 4
# read 读取整个文件，返回 str 结构
# 输出内容和原文一致
with open(file_name, 'r') as f:
	content = f.read()
	print(content)
'''	
