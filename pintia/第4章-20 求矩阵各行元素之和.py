def f():
    m,n=list(map(int,input().split()))
    maxtri=[]
    for i in range(m):
        maxtri.append(list(map(int,input().split())))
    for i in range(m):
        sums=0
        for j in range(n):
            sums+=maxtri[i][j]
        print(sums)
if __name__=="__main__":
    f()
