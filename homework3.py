import numpy as np


def fastest_way(e1, e2, x1, x2, a, t, n):
    f1, f2, l1, l2 = np.zeros(n), np.zeros(n), np.zeros(n), np.zeros(n)
    f1[0] = e1 + a[0][0]
    f2[0] = e2 + a[1][0]
    for i in range(1, n):
        if f1[i - 1] + a[0][i] <= f2[i - 1] + a[0][i] + t[1][i - 1]:
            f1[i] = f1[i - 1] + a[0][i]
            l1[i - 1] = 1
        else:
            f1[i] = f2[i - 1] + a[0][i] + t[1][i - 1]
            l1[i - 1] = 2
        if f2[i - 1] + a[1][i] <= f1[i - 1] + a[1][i] + t[0][i - 1]:
            f2[i] = f2[i - 1] + a[1][i]
            l2[i - 1] = 2
        else:
            f2[i] = f1[i - 1] + a[1][i] + t[0][i - 1]
            l2[i - 1] = 1
    if f1[n - 1] + x1 <= f2[n - 1] + x2:
        f = f1[n - 1] + x1
        l1[n - 1] = 1
    else:
        f = f2[n - 1] + x2
        l2[n - 1] = 1
    return f, l1, l2


def lcs(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    res = np.zeros([len1 + 1, len2 + 1])
    b = np.zeros([len1 + 1, len2 + 1])
    sub=""
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                res[i, j] = res[i - 1, j - 1] + 1
                b[i, j] = 1                 #1表示左上
            elif res[i - 1, j] >= res[i, j - 1]:
                res[i, j] = res[i - 1, j]
                b[i, j] = 2                 #2表示上
            else:
                res[i, j] = res[i, j - 1]
                b[i, j] = 3                 #3表示左
    i,j=len1,len2
    while b[i,j]!=0:
        if b[i,j]==1:
            sub+=s1[i-1]
            #sub.append(s1[i-1])
            i-=1
            j-=1
        if b[i,j]==2:
            i-=1
        if b[i,j]==3:
            j-=1



    return sub,res[len1, len2]


def main():

    e1, e2 = 2, 4
    x1, x2 = 3, 6
    n = 5
    a = [[7, 9, 3, 4, 8],
         [8, 5, 6, 4, 5]]
    t = [[2, 3, 1, 3],
         [2, 1, 2, 2]]
    f, l1, l2 = fastest_way(e1, e2, x1, x2, a, t, n)
    if l1[n - 1] == 1:
        l = l1

    else:
        l = l2

    for index in range(1, 6):
        print("line %d, station %d\n" % (l[index - 1], index))
    print("total time:%d" % f)
    #LCS
    s1 = "ACCGGTCGAGATGCAG"
    s2 = " GTCGTTCGGAATGCAT"
    b,l=lcs(s1,s2)
    print("最长公共子序列为:%s"%b[::-1])
    print("长度为:%d"%l)

