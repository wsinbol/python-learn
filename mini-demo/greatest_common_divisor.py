# 计算最大公约数和最小公倍数

x = int(input('input x = '))
y = int(input('input y = '))

if x > y:
	end = x
else:
	end = y
'''
如果采用升序的方式遍历，那么就无法提前break出来
采用降序的方式提升了性能
'''
for i in range(end, 0, -1):
	if x % i == 0 and y % i == 0:
		print('最大公约数：',i)
		print('最小公倍数', x * y // i)
		break




