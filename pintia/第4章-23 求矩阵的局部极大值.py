def f():
    m,n=list(map(int,input().split()))
    maxtri=[]
    flag=0  # 标记有没有局部最大值
    for i in range(m):
        maxtri.append(list(map(int,input().split())))
    for i in range(1,m-1):
        for j in range(1,n-1):
            if maxtri[i][j]>maxtri[i-1][j] and maxtri[i][j]>maxtri[i][j-1]\
                and maxtri[i][j] > maxtri[i+1][j]\
                and maxtri[i][j]>maxtri[i][j+1]:
                print(maxtri[i][j],i+1,j+1,sep=" ")
                flag=1
    if flag==0:
        print("None",m,n,sep=" ")
if __name__=="__main__":
    f()