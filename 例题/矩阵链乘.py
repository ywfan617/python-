#穷举括号化方案的数量，时间复杂度Ω（4^n/n^(3/2)）
"""
输入:矩阵(A1,A2,A3.......An)的个数n
输出:该矩阵链的完全括号化方案的数量
算法:p(n)=1 n=1
     p(n)=∑p(k)p(n-k),k从1到n-1
"""
def p(n):

    if n==1:
        return n
    else:
        sum=0
        for k in range(1,n):
            sum=sum+(p(k)*p(n-k))
        return sum
"""
矩阵链乘法问题可描述如下:给定n个矩阵的链p<A1,A2,A3.....An>,
矩阵Ai的规模是pi-1*pi(1<=i<=n),
求完全括号话方案，使得计算矩阵A1A2A3...An所用标量乘法次数最少

输入:[p0,p1,p2.....pn],(pi-1，pi)为矩阵Ai的行数和列数

算法:定义m[i,j]表示计算Ai..j所需的标量乘法次数的最小值，那么原问题的最优解是求解m[1,n]
m[i,j]=0,i==j
m[i,j]=min{m[i,k]+m[k+1,j]+pi-1*pk*pj},k=[i,j-1],i<j
同时，我们用s[i,j]保存AiAi+1....Aj最优化括号方案的分割点位置k

输出:m,s

时间复杂度:O(N^3)
"""
def RECURSIVE_MATRIX_CHAIN(p,i,j):
    if i==j:
        return 0
    m=float("inf")  #无穷大的数
    for k in range(i,j):
        q=RECURSIVE_MATRIX_CHAIN(p,i,k)+RECURSIVE_MATRIX_CHAIN(p,k+1,j)+p[i-1]*p[k]*p[j]
        if q<m:
            m=q
    return m
def MATRIX_CHAIN_ORDER(p):
    n=len(p)-1
    m=[[0 for i in range(n+1)] for j in range(n+1)]
    s=[[0 for i in range(n + 1)] for j in range(n + 1)]
    for l in range(2,n+1):
        for i in range(1,n-l+2):
            j=i+l-1
            m[i][j]=float("inf")
            for k in range(i,j):
                q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if q<m[i][j]:
                    m[i][j]=q
                    s[i][j]=k
    return m,s
#备忘录版本，自顶向下，记忆求解，维持一张备忘录表，类似于规划表
"""
输入:[p0,p1,p2.....pn],(pi-1，pi)为矩阵Ai的行数和列数
输出:求完全括号话方案，使得计算矩阵A1A2A3...An所用标量乘法次数最少时的次数
"""
def MEMORIZATION_MATRIX_CHAIN(p):
    n = len(p) - 1
    m = [[float("inf") for i in range(n + 1)] for j in range(n + 1)]
    return LOOKUP_CHAIN(m,p,1,n)
def LOOKUP_CHAIN(m,p,i,j):
    if m[i][j]<float("inf"):
        return m[i][j]
    if i==j:
        m[i][j]=0
    else:
        for k in range(i,j):
            q=LOOKUP_CHAIN(m,p,i,k)+LOOKUP_CHAIN(m,p,k+1,j)+p[i-1]*p[k]*p[j]
            if q<m[i][j]:
                m[i][j]=q
    return m[i][j]

#构造最优解
def PRINT_OPTIMAL_PARENS(s,i,j):
    if i==j:
        print("A{0}".format(i),end="")
    else:
        print("(",end="")
        PRINT_OPTIMAL_PARENS(s,i,s[i][j])
        PRINT_OPTIMAL_PARENS(s,s[i][j]+1,j)
        print(")",end="")


m,s=MATRIX_CHAIN_ORDER([5,20,50,1,100])
print(m[1][4])
for i in range(5):
    for j in range(5):
        print(s[i][j],end=" ")
    print()
PRINT_OPTIMAL_PARENS(s,1,4)
