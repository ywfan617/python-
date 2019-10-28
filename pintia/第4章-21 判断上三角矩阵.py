def f():
    t=int(input())  # 矩阵的个数
    for i in range(t):
        n=int(input())  # 一个方阵的行数
        maxtri=[]
        for j in range(n):
            maxtri.append(list(map(int,input().split())))
        if judge(maxtri,n):
            print("YES")
        else:
            print("NO")
def judge(maxtri,n):
    for i in range(1,n):
        for j in range(i):
            if maxtri[i][j]!=0:
                return False
    return  True
if __name__=="__main__":
    f()

