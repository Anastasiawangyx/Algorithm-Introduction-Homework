

import numpy as np


def getEdges(G):
    """ 输入图G，返回其边与端点的列表 """
    v1 = []  # 出发点
    v2 = []  # 对应的相邻到达点
    w = []  # 顶点v1到顶点v2的边的权值
    for i in G:
        for j in G[i]:
            if G[i][j] != 0:
                w.append(G[i][j])
                v1.append(i)
                v2.append(j)
    return v1, v2, w


def Bellman_Ford(G, v0, INF=999):
    v1, v2, w = getEdges(G)

    # 初始化源点与所有点之间的最短距离
    dis = dict((k, INF) for k in G.keys())
    dis[v0] = 0

    # 核心算法
    for k in range(len(G) - 1):  # 循环 n-1轮
        check = 0  # 用于标记本轮松弛中dis是否发生更新
        for i in range(len(w)):  # 对每条边进行一次松弛操作
            if dis[v1[i]] + w[i] < dis[v2[i]]:
                dis[v2[i]] = dis[v1[i]] + w[i]
                check = 1
        if check == 0: break

    # 检测负权回路
    # 如果在 n-1 次松弛之后，最短路径依然发生变化，则该图必然存在负权回路
    flag = 0
    for i in range(len(w)):  # 对每条边再尝试进行一次松弛操作
        if dis[v1[i]] + w[i] < dis[v2[i]]:
            flag = 1
            break
    if flag == 1:
        return False
    return dis


def Floyd(D,INF=999):
    lengthD = len(D)  # 邻接矩阵大小
    map=np.zeros([lengthD+1,lengthD+1])
    dist=np.zeros([lengthD+1,lengthD+1,lengthD+1])
    res=np.zeros([lengthD,lengthD])
    for i in range(1,lengthD+1):
        for j in range(1,lengthD+1):
            map[i,j]=D[i-1,j-1]
            if i!=j and map[i,j]==0:
                map[i,j]=INF
    for i in range(1, lengthD + 1):
        for j in range(1, lengthD + 1):
            dist[i,j,0]=map[i,j]

    for k in range(1,lengthD+1):
        for i in range(1, lengthD + 1):
            for j in range(1, lengthD + 1):
                dist[i][j][k] = dist[i][j][k - 1]
                if dist[i][k][k - 1] + dist[k][j][k - 1] < dist[i][j][k]:
                    dist[i][j][k] = dist[i][k][k - 1] + dist[k][j][k - 1]
    for i in range(1, lengthD + 1):
        for j in range(1, lengthD + 1):
            res[i-1,j-1]=min((p)for p in dist[i,j])

    print(res)


