# 判断素数
from math import sqrt
# 只要确定是数字的，最好都强制转化
num = int(input('input the number:'))
end = int(sqrt(num))
'''
is_prime = True
for i in range(2, end + 1):
	if num % 2 == 0:
		is_prime = False
		break

if is_prime and num != 1:
	print('Yes')
else:
	print('No')
'''

is_prime = False
for i in range(2, end + 1):
	if num % 2 == 0:
		is_prime = True
		break

if is_prime or num == 1:
	print('No')
else:
	print('Yes')