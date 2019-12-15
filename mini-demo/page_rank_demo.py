"""
Created on Sun Jan  8 23:41:29 2017
 
@author: whenif
"""
 
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
 
 
def getGm(A):
    '''
    功能：求状态转移概率矩阵Gm
    @A：网页链接图的邻接矩阵
    '''
    Gm = []
    for i in range(len(A)):
        cnt = 0
        for j in range(len(A[i])):
            if A[i][j] != 0:
                cnt += 1
        tran_prob = 1 / cnt  # 转移概率
        Gm_tmp = []
        for j in range(len(A[i])):
            Gm_tmp.append(tran_prob * A[i][j])
        Gm.append(Gm_tmp)
    Gm = np.transpose(Gm)
    return Gm
 
 
def getBaseLev(N):
    '''
    功能：计算网页所获得的基本级别(1-P)*e/n
    @N：网页总个数
    '''
    P = 0.85
    e = np.ones(N)
    R = [[(1 - P) * i * 1 / N] for i in e]
    return R
 
 
def getPR(P, Gm, R, PR):
    '''
    功能：获取PR值
    @P：加权系数，通常取 0.85 左右,按照超链接进行浏览的概率
    @Gm：状态转移概率矩阵
    @R：网页所获得的基本级别
    @PR：每个网页节点的PageRank值
    '''
    # 状态转移概率矩阵Gm与PR值相乘矩阵相乘
    Gm_PR = np.dot(Gm, PR)
    # 矩阵乘以常数P
    P_Gm_PR = P * Gm_PR
    # 矩阵相加
    new_PR = P_Gm_PR + R  # PR=P*Gm'PR+(1-d)*e/n PageRank算法的核心
    return new_PR
 
 
def res_vis(A, PR):
    '''
    将计算出来的值进行可视化展示
    @A：网页链接图的邻接矩阵
    @PR：每个网页节点最终的PageRank值
    '''
    # G=nx.Graph()构造的是无向图， G=nx.DiGraph()构造的是有向图
    # 初始化有向图，节点数为7,edge（边）被创造的随机概率
    all_edges = []
    for i in range(7):
        for j in range(len(A)):
            if A[i][j] == 1:
                all_edges.append([i + 1, j + 1])
                # （1）初始化有向图
    G = nx.DiGraph()
    # （2）添加节点
    G.add_nodes_from(range(1, len(A)))
    # （3）添加有向边
    G.add_edges_from(all_edges)
    # （4）添加PR值
    pr = {}
    for i in range(len(PR)):
        pr[i + 1] = PR[i][0]
    # (5)画图
    layout = nx.spring_layout(G)
    plt.figure(1)
    nx.draw(G, pos=layout, node_size=[x * 6000 for x in pr.values()],
            node_color='m', with_labels=True)
    plt.show()
 
 
def main():
    # 初始化参数
    N = 7  # 网页个数
    P = 0.85  # 一个加权系数，通常取 0.85 左右,按照超链接进行浏览的概率
    # 网页链接图的邻接矩阵，每一列表示一个网页的出度
    A = np.array([[0, 1, 1, 0, 1, 1, 0],
                  [1, 0, 1, 1, 0, 0, 0],
                  [1, 0, 0, 1, 1, 0, 0],
                  [1, 0, 0, 0, 1, 0, 0],
                  [1, 0, 0, 1, 0, 1, 1],
                  [0, 0, 0, 0, 1, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0]])
    A = np.transpose(A)  # 转置
    # 初始化PR值为0
    new_PR = []
    for i in range(N):
        new_PR.append([0])
    count = 0  # 迭代计数器
    while True:
        PR = new_PR
        R = getBaseLev(N)
        Gm = getGm(A)
        new_PR = getPR(P, Gm, R, PR)
        count = count + 1
        print("第 %s 轮迭代" % count)
        print(str(round(new_PR[0][0], 5))
              + "\t" + str(round(new_PR[1][0], 5))
              + "\t" + str(round(new_PR[2][0], 5))
              + "\t" + str(round(new_PR[3][0], 5))
              + "\t" + str(round(new_PR[4][0], 5))
              + "\t" + str(round(new_PR[5][0], 5))
              + "\t" + str(round(new_PR[6][0], 5)))
        # 设置迭代条件
        if (round(PR[0][0], 5) == round(new_PR[0][0], 5)
                and round(PR[1][0], 5) == round(new_PR[1][0], 5)
                and round(PR[2][0], 5) == round(new_PR[2][0], 5)
                and round(PR[3][0], 5) == round(new_PR[3][0], 5)
                and round(PR[4][0], 5) == round(new_PR[4][0], 5)
                and round(PR[5][0], 5) == round(new_PR[5][0], 5)
                and round(PR[6][0], 5) == round(new_PR[6][0], 5)):
            break
    print("-------------------")
    print("PageRank值已计算完成")
    res_vis(A, new_PR)
 
 
if __name__ == '__main__':
    main()