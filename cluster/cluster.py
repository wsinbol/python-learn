#!/usr/bin/env python
# coding: utf-8

# In[84]:


def read_file(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        lines = f.readlines()
        
    row = lines[0]
    row_name = row.strip().split('\t')[1:]
    
    column_name = []
    data = []
    for line in lines[1:]:
        row_data = line.strip().split('\t')
        column_name.append(row_data[0])
        data.append([int(i) for i in row_data[1:]])
    return row_name,column_name,data
        
key_words,blog_titles,data = read_file('blogdata.txt')


# key_words.index('yahoo') # 3
# blog_titles.index('Quick Online Tips') # 85
# data[85][3]


# In[30]:


class bicluster:
    def __init__(self,vec,left=None,right=None,distance=0.0,id=None):
        self.left = left
        self.right = right
        self.vec = vec
        self.id = id
        self.distance = distance


# In[87]:


from math import sqrt
def pearson(v1,v2):
    sum1 = sum(v1)
    sum2 = sum(v2)
    
    sum1sq = sum([pow(v,2) for v in v1])
    sum2sq = sum([pow(v,2) for v in v2])
    
    multi_sum = sum([v1[i] * v2[i] for i in range(len(v1))])
    
    num = multi_sum - (sum1 * sum2 / len(v1))
    den = sqrt((sum1sq - pow(sum1, 2) / len(v1)) * (sum2sq - pow(sum2,2) / len(v2)))
    if den == 0:
        return 0
    return 1.0 - num/den


# In[111]:


def all_distance_pair(rows,distance=pearson):
    all_distance = {}
    clust = [bicluster(rows[i],id=i) for i in range(len(rows))]
    for i in range(len(clust)):
        for j in range(i+1, len(clust)):
            all_distance[(clust[i].id, clust[j].id)] = distance(clust[i].vec, clust[j].vec)
    return all_distance

all_distance_dict = all_distance_pair(data)
all_distance_dict


# In[115]:


all_distance_dict.keys()


# In[119]:


def hcluster(rows,all_distance_dict,distance=pearson):
    clust = [bicluster(rows[i],id=i) for i in range(len(rows))]
    distance_pair = {}
    currentclustid=-1
    
    while len(clust) > 1:
        lowestpair = (0,1)
        closest = distance(clust[0].vec, clust[1].vec)
        
        for i in range(len(clust)):
            for j in range(i+1, len(clust)):
                d = all_distance_dict.get(clust[i].id, clust[j].id)
                if d < closest:
                    closest = d
                    lowestpair = (i,j)
                    
        mergevec=[(clust[lowestpair[0]].vec[i]+clust[lowestpair[1]].vec[i])/2.0 for i in range(len(clust[0].vec))]
        newcluster=bicluster(mergevec,left=clust[lowestpair[0]],right=clust[lowestpair[1]],distance=closest,id=currentclustid)
        
        currentclustid-=1
        del clust[lowestpair[1]]
        del clust[lowestpair[0]]
        clust.append(newcluster)
    
    return clust[0]

result = hcluster(data,all_distance_dict)


# In[121]:


def printclust(clust,labels=None,n=0):
    for i in range(n): 
        print(' ')
    if clust.id<0:
        print('-')
    else:
        if labels==None: print(clust.id)
        else: print(labels[clust.id])

    if clust.left!=None: printclust(clust.left,labels=labels,n=n+1)
    if clust.right!=None: printclust(clust.right,labels=labels,n=n+1)
        
printclust(result,blog_titles)

