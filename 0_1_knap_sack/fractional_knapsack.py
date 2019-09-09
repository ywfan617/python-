"""
输入：W,C是已经按照单位重量最大价值排好序的物品重量以及价值
输出：装包方案X
算法：贪心算法
"""
def fractional_knapsack(W,V,C):
    n=len(W)
    X=[0]*n
    M=[0]*n
    for i in range(n):
        if W[i]<C:
            X[i]=1
            M[i]=W[i]
            C-=W[i]

    if i<n:
        X[i]=C/W[i]
        M[i]=C
    return X,M
W=[10,20,30]
V=[60,100,120]
C=50
print(fractional_knapsack(W,V,C))