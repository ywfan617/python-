#递归版本
"""
输入：可选物品集W，物品集对应的价值集，给定可选物品集合{i,i+2.....n},给定的背包容量j
输出: 可装入背包物品的最大价值
算法:见笔记
"""
def RECURSIVE_knapsack(W,V,i,j):
    n=len(W)
    if i==n-1 or j==0:
        if j>=W[i]:
            return V[i]
        else:
            return 0
    else:
        if W[i]>j:
            return RECURSIVE_knapsack(W,V,i+1,j)
        else:
            return max(RECURSIVE_knapsack(W,V,i+1,j-W[i])+V[i],RECURSIVE_knapsack(W,V,i+1,j))
#DP版本
"""
"""
def knapsack(W,V,C):
    n=len(W)
    max_w=C
    m=[[0 for j in range(max_w+1)]for j in range(n)]
    for j in range(1,max_w+1):
        if W[-1]<=j:
            m[-1][j]=V[-1]
    for i in range(n-2,-1,-1):
        for j in range(1,max_w+1):
            if j<W[i]:
                m[i][j]=m[i+1][j]
            else:
                m[i][j]=max(m[i+1][j-W[i]]+V[i],m[i+1][j])
    return m
#根据DP版本构造最优解
def print_knapsack(W,V,C,m):
    n = len(W)
    max_w = C
    x=[0]*n
    c=max_w
    for i in range(n-1):
        if m[i][c]!=m[i+1][c]:
            x[i]=1
            c=-W[i]
    x[n-1]=int(m[n-1][c]!=0)
    return x




W=[10,20,30]
V=[60,100,120]
n=len(W)
print(RECURSIVE_knapsack(W,V,0,50))
m=knapsack(W,V,50)
print(m[0][50])
print(print_knapsack(W,V,50,m))
