import numpy as np
from math import sqrt
import time

# 暴力求解
def direct(m1, m2):
    if len(m1) != len(m2):
        print("ERROR!")
        exit()
    n = len(m1)
    m = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            for k in range(n):
                m[i][j] += m1[i][k] * m2[k][j]

    return m


# 分解矩阵成四个小矩阵
def division(m):
    n = len(m) // 2
    a, b, c, d = np.zeros([n, n]), np.zeros([n, n]), np.zeros([n, n]), np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            a[i, j] = m[i, j]
            b[i, j] = m[i, j + n]
            c[i, j] = m[i + n, j]
            d[i, j] = m[i + n, j + n]
    return a, b, c, d


# 矩阵相加/减
def add_minus(m1, m2, flag):
    if len(m1) != len(m2):
        print('ERROR')
        exit()
    n = len(m1)
    m = np.zeros([n, n])
    if flag > 0:
        for i in range(n):
            for j in range(n):
                m[i, j] = m1[i, j] + m2[i, j]
    else:
        for i in range(n):
            for j in range(n):
                m[i, j] = m1[i, j] - m2[i, j]
    return m


# 将生成的四个子矩阵组合成一个大矩阵
def combine(a, b, c, d):
    n = len(a)
    m = np.zeros([n * 2, n * 2])
    for i in range(n * 2):
        for j in range(n * 2):
            if i < n and j < n:
                m[i, j] = a[i, j]
            elif i < n <= j:
                m[i, j] = b[i, j - n]
            elif i >= n > j:
                m[i, j] = c[i - n, j]
            else:
                m[i, j] = d[i - n, j - n]
    return m


#strassen算法
def strassen(m1, m2):
    n = len(m1)
    m = np.zeros([n, n])
    if n == 1:
        m[0, 0] = m1[0, 0] * m2[0, 0]
    else:
        a, b, c, d = division(m1)
        e, f, g, h = division(m2)
        h1 = add_minus(f, h, -1)
        h2 = add_minus(a, b, 1)
        h3 = add_minus(c, d, 1)
        h4 = add_minus(g, e, -1)
        h5 = add_minus(a, d, 1)
        h6 = add_minus(e, h, 1)
        h7 = add_minus(b, d, -1)
        h8 = add_minus(g, h, 1)
        h9 = add_minus(a, c, -1)
        h10 = add_minus(e, f, 1)
        s1 = strassen(a, h1)
        s2 = strassen(h2, h)
        s3 = strassen(h3, e)
        s4 = strassen(d, h4)
        s5 = strassen(h5, h6)
        s6 = strassen(h7, h8)
        s7 = strassen(h9, h10)
        i = add_minus(s5, add_minus(s6, add_minus(s4, s2, -1), 1), 1)
        j = add_minus(s1, s2, 1)
        k = add_minus(s3, s4, 1)
        l = add_minus(s5, add_minus(s1, add_minus(s3, s7, 1), -1), 1)
        m = combine(i, j, k, l)
    return m


def get_distance(s):
    return sqrt((s[0][0] - s[1][0])**2+(s[0][1] - s[1][1])**2)


#最近点对算法
def nearest_dots(s):
    n = len(s)
    left = s[0:n // 2]
    right = s[n // 2:]
    mid = (left[-1][0] + right[0][0]) / 2.0

    if len(left) > 2:
        lmin = nearest_dots(left)  # 左侧部分最近点对
    else:
        lmin = left
    if len(right) > 2:
        rmin = nearest_dots(right)  # 右侧部分最近点对
    else:
        rmin = right

    if len(lmin) > 1:
        dis_l = get_distance(lmin)
    else:
        dis_l = float("inf")
    if len(rmin) > 1:
        dis_r = get_distance(rmin)
    else:
        dis_r = float("inf")

    if dis_l<dis_r:
        minimum=dis_l       #最近距离
        min_dots=lmin       #最近点对
    else:
        minimum=dis_r
        min_dots=rmin

    for i in left:
        if mid-i[0]<=minimum:        #左点在minimum区域内
            for j in right:
                if abs(i[0]-j[0])<=minimum and abs(i[1]-j[1]<=minimum):     #右点在矩形内
                    if get_distance((i,j))<=minimum:
                        minimum=get_distance((i,j))
                        min_dots=(i,j)
    return min_dots

def main():
    for x in np.logspace(3,10,8,base=2,dtype=int):
        m1 = np.random.randint(0, 10, (x, x))
        m2 = np.random.randint(0, 10, (x, x))
        start=time.process_time()
        strassen(m1, m2)
        end =time.process_time()
        print("%d维矩阵的Strassen's方法所需要的时间为:%s\n"%(x,end-start))
    s = [(0, 1), (3, 2), (4, 3), (5, 1), (1, 2), (2, 1), (6, 2), (7, 2), (8, 3), (4, 5), (9, 0), (6, 4)]
    s.sort()
    print(nearest_dots(s))
