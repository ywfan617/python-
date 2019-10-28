#递归版本
"""
输入:序列X,序列Y
输出:序列X和序列Y的一个最长公共子序列的长度
时间复杂度:指数阶的，因为重复计算了大量的子问题，而实际只需要计算M*n个子问题
"""

def RECURSIVE_LCS(X,Y):
    m=len(X)
    n=len(Y)
    if m==0 or n==0:
        return 0
    else:
        if X[m-1]==Y[n-1]:
            return RECURSIVE_LCS(X[:m-1],Y[:n-1])+1
        else:
            return max(RECURSIVE_LCS(X[:m-1],Y),RECURSIVE_LCS(X,Y[:n-1]))
#DP版本
"""
输入：X=[x1,x2,x3,x4....xn]
      Y=[y1,y2,y3,y4.......xm]
输出:c,b
算法:定义c[i,j]表示Xi和Yj的LCS长度，根据LCS问题的最优子结构性质，可得到如下公式:
 c[i,j]=  0                  若i=0或j=0
          c[i-1,j-1]+1       若i!=0 且 就j!=0 且 xi=yj
          max{c[i-1,j],c[i,j-1]}若i!=0且j!=0 且 xi!=yi
时间复杂度:Θ(n^2)
空间复杂度:O(mn)
变种:求一个序列的最长单调递增序列
"""
def LCS_LENGTH(X,Y):
    m=len(X)
    n=len(Y)
    c=[[0 for j in range(n+1)] for i in range(m+1)]
    b=[[" " for j in range(n+1)] for i in range(m+1)]
    for i in range(1,m+1):
        c[i][0]=0
    for j in range(n+1):
        c[0][j]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]:
                c[i][j]=c[i-1][j-1]+1
                b[i][j]="↖"
            else:
                if c[i-1][j]>c[i][j-1]:
                    c[i][j]=c[i-1][j]
                    b[i][j]="↑"
                else :
                    c[i][j]=c[i][j-1]
                    b[i][j]="←"
    return c,b

#备忘录版本
"""
输入:序列X,序列Y
输出:序列X和序列Y的一个最长公共子序列的长度
时间复杂度:O(m*n)
空间复杂度:O(m*n)
"""
def MEMORIZATION_LCS(X,Y):
    m=len(X)
    n=len(Y)
    c = [[float("inf") for j in range(n + 1)] for i in range(m + 1)]
    return LOOKUP(c,X,Y,m,n)
def LOOKUP(c,X,Y,i,j):
    if c[i][j]<float("inf"):
        return c[i][j]
    if i==0 or j==0:
        c[i][j]=0
    else:
        if X[i-1]==Y[j-1]:
            return LOOKUP(c,X,Y,i-1,j-1)+1
        else:
            c[i][j]= max(LOOKUP(c,X,Y,i-1,j),LOOKUP(c,X,Y,i,j-1))
    return c[i][j]


"""
构造LCS,
时间复杂度:O(m+n),因为每次都用i和j都会减少1
"""
def PRINT_LCS(b,X,Y,i,j):
    if i==0 or j==0:
        return
    if b[i][j]=="↖":
        PRINT_LCS(b,X,Y,i-1,j-1)
        print(X[i-1],end="")
    if b[i][j]=="↑":
        PRINT_LCS(b,X,Y,i-1,j)
    if b[i][j]=="←":
        PRINT_LCS(b,X,Y,i,j-1)


X=[1,2,5,3,8,9]
Y=[1,2,3,5,8,9]
m=len(X)
n=len(Y)
print(RECURSIVE_LCS([1,2,3],[0,1,2]))
c,b=LCS_LENGTH(X,Y)
# for i in range(8):
#     for j in range(7):
#         print(c[i][j],end=" ")
#     print()
# for i in range(8):
#     for j in range(7):
#         print(b[i][j],end="")
#     print()
PRINT_LCS(b,X,Y,m,n)
print()
print(MEMORIZATION_LCS(X,Y))