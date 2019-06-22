import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

################################################Series用法#################################

'''
# 通过Numpy数组创建Series
s = pd.Series(np.random.rand(5))
# print(s)
# print(s.index) # RangeIndex(start=0, stop=5, step=1)
# print(s.values)
exit()
'''


'''
#传递list对象创建Series
s = pd.Series([1,3,8,9,5])
print(s)
'''

'''
# 设置重复索引
s = pd.Series(np.random.rand(5), index = list('abcaa'))
print(s)
exit()
'''


# 通过字典创建Series
# d = {'a' : 1, 'b' : 2, 'c':3, 'd' : 4, 'e' : 5}
# s = pd.Series(d)
# s = pd.Series(d, index = list('bcdef'))

'''
b    2.0
c    3.0
d    4.0
e    5.0
f    NaN
'''
# print(s)
# exit()

'''
# 生成相同值的Series
s = pd.Series(1, index = list('abcde'))
print(s)
exit()
'''

# s = pd.Series(3, index = list('abcde'))
# print(s['a']) # 推荐用法
# print(s.a)
# print(s[['a','e']])
# print(s['f'])
# Passing list-likes to .loc or [] with any missing label will raise
# KeyError in the future, you can use .reindex() as an alternative.
# print('a' in s)
# print('f' in s)

# print(s*2)
# print(s**2)
# print(np.sin(s))
# print(s[1:] + s[:-1])
# 对应数据进行运算，不对应数据返回NaN
'''
a    NaN
b    6.0
c    6.0
d    6.0
e    NaN
'''
# exit()

################################DataFrame用法#####################################

'''
data = {
	'城市' : ['A','B','C','D','E'],
	'序号' : ['1','2','3','4','5'],
	'年份' : [2015,2015,2015,2015,2016],
}
# df = pd.DataFrame(data)
# 设置各列先后顺序，不存在的列数据显示为NaN
df = pd.DataFrame(data, columns = ['年份','序号','城市','产值'])
# 定义各行标签
# df = pd.DataFrame(data, index = list('abcde'))
print(df)
'''


# date_range的用法 
#通过时间索引以及列标签创建DataFrame
dates = pd.date_range('20180101', periods = 6) # 创建时间索引，从2018-01-01到2018-01-06
# print(date)
# np.random.randn(6,4)生成6行4列的随机数组，以index为行索引，指定columns为列项
# df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = ['a','b','c','d'])
# df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list('abcd'))
df = pd.DataFrame(np.arange(24).reshape(6,4), index = dates, columns = ['a','b','c','d'])
# print(df)


'''
# 各种方式创建DataFrame
df2 = pd.DataFrame({
	'A' : 1.,
	'B' : pd.Timestamp('20180101'),
	'C' : pd.Series(1, index = list(range(4))),
	'D' : np.array([3]*4),
	'E' : pd.Categorical(["test", "train", "test", "train"]),
	'F' : 'symbol',
	})
print(df2)
print(df2.dtypes) # 查看不同列数据类型
'''

'''
dates = pd.date_range('20181231', periods = 6) # 20181232时会报错
df = pd.DataFrame(np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]), index = dates, columns = list('ABCD'))
'''


'''
# print(df)
# exit()
# print(df.head(1))
# print('*'*140)
# print(df.tail(2))
# print('*'*140)
# print(df.index) # 显示索引
# print('*'*140)
# print(df.columns) # 显示列
# print('*'*140)
print(df.values) # 显示值
print('*'*140)
print(df.describe()) # 显示统计信息
exit()
'''

'''
# print(df.T) # 行列转置
print(df.sort_index(axis = 0, ascending = False)) # ascending-上升 axis为0表示按行执行，为1表示按列执行
print(df.sort_values(by = 'B', ascending = False)) # 按指定列的值降序排列
exit()
'''

'''
print(df.A) # 等同于d['A']
print(df[0:3]) # 对行切片
print(df['20181231':'20190102'])
'''

'''
df = pd.read_csv('user.csv',encoding = 'gb2312')
print(df)
'''

############################################高级用法##############################################

# .at .iat .loc .iloc .ix

#######################################################################
# .at用法: Access a single value for a row/column label pair.
# dateIndex = pd.date_range('20180101', periods = 1)
# print(dateIndex[0])
# print(df.index)
# print(df.at[dateIndex[0],'a']) # Right

# 下面两种方式都是错误的，因为索引类型是不一样的，所以要构造DatetimeIndex类型才可以
# print(df.at['2018-01-01', 'a'])
# print(df.at['2018-01-01 00:00:00', 'a'])

# 使用标签获取交叉区域,dates[0]为2018-01-01且类型为DatetimeIndex，调用.loc方法获取改行数据
# print(df.loc[dates[0]]) 

#####################################################################
# .iat用法: Access a single value for a row/column pair by integer position.
# 通过整数类型的位置类获取单个值，不要使用任何index/column索引
# print(df)
# print(df.iat[1, 10])

####################################################################
# .loc用法：Access a group of rows and columns by label(s) or a boolean array.
# .loc[] is primarily label based, but may also be used with a boolean array.
# 通过标签或者布尔数组获得行列组，且标签的数据类型不需要和源数据保持一致(只有一个索引的情况下)
# 如果索引恰恰也是整型，则可以统一通过整型标签进行操作
# print(df.loc['2018-01-01'])
# print(df.loc['b']) # 不能对column进行索引

# print(df.loc[[dates[0],dates[1]]]) # right
# print(df.loc[['2018-01-01','2018-01-02']]) # error
# print(df.loc[[dates[0],dates[1]], 'a'])
# print(df.loc[[dates[0],dates[1]], ['a','b']])

# print(df.loc[[dates[0:2]], ['a','b']]) # error

# 切片操作注意[]的不同，而且下面两种返回结果不一样！！！
# print(df.loc[dates[0:2], 'a':'c'])
# print(df.loc[dates[0]:dates[2], 'a':'c'])

# print(df.loc[[True,False,True]])
# print(df.loc[[0,1,0]]) # error

# print(df.loc[ df['a'] > 8 ])
# 下面做法错误,因为相对于对column进行loc操作，也就是判断条件必须是column索引，然后返回的是index行索引
# print(df.loc[ df['2018-01-01'] > 1 ]) # error

# print(df.loc[ df['a'] > 8, ['a', 'c'] ])
# print(df.loc[ lambda df: df['a'] == 8 ])

# 修改值
# 将前两行的前3列的值统一修改成50！
# df.loc[ [dates[0], dates[1]], ['a','b','c'] ] = 50
# print(df)

# 将第一行的值全部修改成50
# df.loc[ dates[0] ] = 50
# print(df)


# 将第一列的值全部修改成50
# df.loc[ :, 'a' ] = 50
# print(df)
# df.loc[:, 'a':'c'] = 50

# 将‘a’列中值小于10的行全部置为0
# df.loc[ df['a'] < 10 ] = 0
# print(df)


# 标签切片
# print(df.loc['20190101':'20190102',['A','B']])
'''
            A   B
2019-01-01  5   6
2019-01-02  9  10
'''


# print(df.loc['20190101',['A','B']]) # 维度缩减
'''
A    5
B    6
Name: 2019-01-01 00:00:00, dtype: int32
'''

'''
print(df.loc[dates[0],'A']) # 获取一个标量
print(df.at[dates[0],'A']) # 与上一个方法等价
'''

##########一个多重索引的例子#######################################
'''
tuples = [
   ('cobra', 'mark i'), ('cobra', 'mark ii'),
   ('sidewinder', 'mark i'), ('sidewinder', 'mark ii'),
   ('viper', 'mark ii'), ('viper', 'mark iii')
]
index = pd.MultiIndex.from_tuples(tuples)
values = [[12, 2], [0, 4], [10, 20],
        [1, 4], [7, 1], [16, 36]]
df = pd.DataFrame(values, columns=['max_speed', 'shield'], index=index)
'''
# print(df)
# print(df.loc['cobra'])
# print(df.loc['cobra','mark i'])
# print(df.loc[('cobra','mark i')]) # 结果同上
# print(df.loc[[('cobra', 'mark ii')]])

# 注意返回数据类型的不同
# print(type(df.loc[('cobra','mark i')])) # return Series
# print(type(df.loc[[('cobra', 'mark ii')]])) # return DataFrame

# 注意返回结果的不同
# print(df.loc[('cobra', 'mark i'), 'shield'])
'''
2
'''
# print(df.loc[['cobra', 'mark i'], 'shield'])
'''
cobra  mark i     2
       mark ii    4
Name: shield, dtype: int64
'''

# print(df.loc[('cobra', 'mark i'):'viper'])
# print(df.loc[('cobra', 'mark i'):('viper', 'mark ii')]) # 与上面唯一的不同就是mark iii不会显示

###########################################################################
# .iloc用法：Purely integer-location based indexing for selection by position.
# 整数类型的位置索引，也可以使用布尔数组，只对index进行索引，不对column进行索引
# 注意类型的不同
# print(df.iloc[0])
# print(df.iloc[[0]])

# print(df.iloc[0,2])
# print(df.iloc[(0,2)]) # 与上例同
# print(df.iloc[[0,2]]) # 与上述两例子差距甚多

# print(df.iloc[[True, False, True]])

# 如果index索引是整型，可以使用下述条件过滤
# print(df.iloc[lambda x: x.index % 2 == 0])

# print(df.iloc[3]) # 传递数值进行位置选择，选择的是行
# print(df.iloc[3:5,0:2]) # 通过[行，列]切片获取数据
# print(df.iloc[[1,3,4],[0,2]])
# print(df.iloc[1,1]) # 获取特定的值
# print(df.iat[1,1]) # 获取特定的值

# print(df[df.A > 7])
# print(df[df > 7])
'''
               A     B     C     D
2018-12-31   NaN   NaN   NaN   NaN
2019-01-01   NaN   NaN   NaN   8.0
2019-01-02   9.0  10.0  11.0  12.0
2019-01-03  13.0  14.0  15.0  16.0
2019-01-04  17.0  18.0  19.0  20.0
2019-01-05  21.0  22.0  23.0  24.0
'''

##########################################################################################
# .ix用法：已经废弃，不需要掌握

'''
df2 = df.copy()
df2['E'] = ['one','one','two','three','four','three']
# print(df2)
print(df2[df2['E'].isin(['two','four'])]) # isin的用法
'''

'''
s1 = pd.Series([25,26,27,28,29,30],index = pd.date_range('20181231', periods = 6))
# print(s1)
df['F'] = s1
print(df)
'''

'''
df.at[dates[0],'A'] = 0
df.iat[0,0] = 0
df.loc[:,'D'] = np.array([5]*len(df))
print(df)
'''

'''
# 缺失值处理
# reindex()方法可以对指定轴上的索引进行改变、增加、删除操作，并将返回原始数据的一个拷贝
# print(df)
df1 = df.reindex(index=dates[0:4], columns = list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
print(df1)
print('*'*100)
print(df1.dropna(how = 'any')) # 去掉缺失值，把整个行都去掉了。。。
print(df1.fillna(value = '5')) # 对缺失值进行填充
print(pd.isnull(df1)) # 对数据进行布尔填充
'''

'''
print(df.mean())
print(df.mean(1))
'''

'''
s = pd.Series([1,3,5,np.nan,6,8], index = dates).shift(2) # shift的含义？
# s = pd.Series([1,3,5,np.nan,6,8], index = dates)
# print(s)
df1 = df.sub(s, axis = 'index')
print(df1)
'''

# apply - 对数据应用函数
'''
df1 = apply(np.cumsum)
df1 = apply(lambda x: x.max() - x.min())
'''

'''
# 直方图，这个名字好
s = pd.Series(np.random.randint(0,7,size = 10))
print(s)
print('#'*100)
print(s.value_counts()) # 返回值数量的降序排列
'''

'''
# 对字符串的操作
s = pd.Series(['A','ABAB','NBA','Cba',np.nan,'cat'])
print(s.str.lower())
'''

'''
# 合并 concat
df = pd.DataFrame(np.random.randn(10,4))
pieces = [df[:3],df[3:7],df[7:]]
print(pieces)
print('!'*100)
print(pd.concat(pieces))
'''


# 合并 join 类似于SQL的合并,举一反三，找到应用场景
'''
left = pd.DataFrame({'key':['foo','foo'], 'lval':[1,2]})
right = pd.DataFrame({'key':['foo','foo'], 'rval':[4,5]})
# print(left)
df1 = pd.merge(left, right, on = 'key')
print(df1)
'''

'''
left = pd.DataFrame({'key':['foo','bar'], 'lval':[1,2]})
right = pd.DataFrame({'key':['foo','bar'], 'rval':[4,5]})
# print(left)
df1 = pd.merge(left, right, on = 'key')
print(df1)
'''

'''
df = pd.DataFrame(np.random.randn(8,4), columns = ['A','B','C','D'])
s = df.iloc[3]
df1 = df.append(s, ignore_index = True) # 将索引为3的行追加到元数据的末尾
print(df1)
'''

'''
分组 - group by 
1.splitting 按照一些规则将数据分为不同的组
2.applying 对于每组数据分别执行一个函数
3.combining 将结果组合到一个数据结构中
'''
'''
df = pd.DataFrame({
	'A' : ['foo','bar','foo','bar','foo','bar','foo','foo'],
	'B' : ['one','one','two','three','two','two','one','three'],
	'C' : np.random.randn(8),
	'D' : np.random.randn(8)
	})

# df1 = df.groupby('A').sum()
# print(df1)


df1 = df.groupby(['A','B']).sum()
print(df1)
'''

'''
df = pd.DataFrame({
	'A' : ['one','one','two','three'] * 3,
	'B' : ['A','B','C'] * 4,
	'C' : ['foo','foo','foo','bar','bar','bar'] * 2,
	'D' : np.random.randn(12),
	'E' : np.random.randn(12)
	})
# 生成数据透视表
df1 = pd.pivot_table(df, values = 'D', index = ['A','B'], columns = ['C'])
print(df1)
'''



'''
# 时间序列
rng = pd.date_range('1/1/2012', periods = 100, freq = 'S')
ts = pd.Series(np.random.randint(0,500,len(rng)), index = rng)
df = ts.resample('5Min').sum()
# print(df)
# print(ts)
'''

# categorical 这部分没看



'''
# 画图
ts = pd.Series(np.random.randn(1000), index = pd.date_range('1/1/2000', periods = 1000))
# ts = ts.cumsum()
# ts.plot()
# plt.show()


df = pd.DataFrame(np.random.randn(1000,4), index = ts.index, columns = ['A','B','C','D'])
df = df.cumsum()
# plt.figure()
df.plot()
plt.legend(loc = 'best')
plt.show()
'''

'''
data = pd.read_csv('user.csv', encoding = 'gb2312')
print(data)
'''
