
row = int(input('please input rows:'))

'''
for i in range(1,row + 1):
	for j in range(1, i + 1):
		print('*', end='\t')
	print('')
'''

#1
'''
for i in range(1,row + 1):
	print('*' * (i), end='\n')
'''

#2
'''
for i in range(row, 0, -1):
	# for j in range(1, i - j):
	print(' ' * (i - 1), '*' * (row - i))
print('*'*row)
'''

#3
# 2 * i -1
'''
for i in range(1, row + 1):
	print(' ' * (row - i), '*' * (2 * i - 1), ' ' * (row - i))
'''

for i in range(1, row + 1):
	for j in range(1, 2 * row):

