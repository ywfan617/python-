# 将列表转换为矩阵，矩阵的行数为m行
def f(nums,m):
    length=len(nums)
    n=length//m
    maxtri=[[]for i in range(m)]
    j=0
    for i in range(length):
        maxtri[j].append(nums[i])
        if (i+1)%n==0:
            j+=1
    T=[[]for i in range(n)]
    new_j=0
    for g in range(n):
        for h in range(m):
            T[new_j].append(maxtri[h][g])
        new_j+=1
    return maxtri,T
if __name__=="__main__":
    nums=[1,2,3,4,5,6,7,8,9,10]
    raw,T=f(nums,2)
    print(raw)
    print(T)
