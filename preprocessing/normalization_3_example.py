import numpy as np
#要格外注意数据结构类型
# dataset = [[1,1],[7,7]]

dataset = np.array([
	[1,0,0,1,0],
	[1,0,1,1,1],
	[1,0,0,1,0],
	[0,0,0,1,0],
	[0,1,0,1,1],
	[0,0,0,1,0]
	])

# dataset = np.array([
# 	[2,3,4],
# 	[1,4,7]
# 	])

# print(dataset.max())
max = dataset.max() #axis=0表示在列上运算该函数，axis=1表示在行上运算该函数，不指定为在整体上运算
min = dataset.min()
sigma = dataset.std() #标准差
# mu = dataset.average() #均值
# mu = np.mean(dataset)
mu = dataset.mean()
# print(mu)
# print('标准差',dataset.std())

newDataSet = dataset.reshape((1,30))
#遍历ndarray结构数据
shapeDataSet = []

for element in dataset.flat:
	# value = (element-min)/(max-min) # 0-1标准归化
	# value = (element-mu)/sigma #Z-score标准化
	value = 1.0 / (1 + np.exp(-float(element))) #sigmoid标准化
	shapeDataSet.append(value)
finalDataSet = np.array(shapeDataSet).reshape((6,5))
print(finalDataSet)

u,sigma,vt = np.linalg.svd(dataset)
print(u)
print(sigma)
print(vt)