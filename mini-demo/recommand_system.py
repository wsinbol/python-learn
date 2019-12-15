
import math

# initialize data
# 需要注意数据非结构化数据时程序对数据的处理
critics = {
	'zhao' : {'A' : 3.0, 'B' : 4.0},
	'qian' : {'A' : 3.0, 'B' : 4.0, 'C' : 2.0},
	'wang' : {'A' : 4.0, 'B' : 1.0},
	}

# print([critics['zhao'][l] for l in critics['zhao']])

'''
# 皮尔逊相关度评价：判断两组数据与某一直线拟合程度的度量
# 1.先求总和
# 2.再求平方和
# 3.乘积之和
# 4.皮尔逊相关度
n = 2 #由二人共同评价的个数决定

# 1
sum1 = sum(critics['zhao'][item] for item in critics['zhao'])
sum2 = sum(critics['qian'][item] for item in critics['qian'])
# 2
sum1Sq = sum([pow(critics['zhao'][item], 2) for item in critics['zhao']])
sum2Sq = sum([pow(critics['qian'][item], 2) for item in critics['qian']])
# 3
sumProduct = sum(critics['zhao'][item] * critics['qian'][item] for item in critics['zhao'])
# 4
num = sumProduct - (sum1 * sum2 / n)
den = math.sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))

r = num /den 
print(r)
'''

# 计算两个人之间的欧几里得距离
def euclideanDistanceScore(dataset, person1, person2):
	if person1 not in dataset:
		return person1 + ' not exists!'
	if person2 not in dataset:
		return person2 + ' not exists!'

	# 此处需要判断两个用户是否都对同一个item进行过评价，否则计算无意义

	sum_of_squares = sum(pow(dataset[person1][item] - dataset[person2][item], 2) for item in dataset[person1] if item in dataset[person2])
	standardization_value = 1 / (1 + math.sqrt(sum_of_squares))
	return standardization_value

# 计算两个人之间的皮尔逊相关系数
def pearsonScore(dataset, person1, person2):
	if person1 not in dataset:
		return person1 + ' not exists!'
	if person2 not in dataset:
		return person2 + ' not exists!'

	shared_item = {}

	for item in dataset[person1]:
		if item in dataset[person2]:
			shared_item[item] = 1

	n = len(shared_item)
	if n == 0:
		return 'It does no means!'

	sumPerson1 = sum([dataset[person1][item] for item in shared_item])
	sumPerson2 = sum([dataset[person2][item] for item in shared_item])

	sumPerson1Square = sum([pow(dataset[person1][item], 2) for item in shared_item])
	sumPerson2Square = sum([pow(dataset[person2][item], 2) for item in shared_item])

	productSum = sum([dataset[person1][item] * dataset[person2][item] for item in shared_item])

	num = productSum - (sumPerson1 * sumPerson2 / n)
	den = math.sqrt((sumPerson1Square - pow(sumPerson1, 2) / n) * (sumPerson2Square - pow(sumPerson2, 2) / n))
	if den == 0:
		return 0
	weight = num / den

	return weight


result = pearsonScore(critics, 'zhao', 'qian')
print(result)