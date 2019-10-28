def f():
    n=int(input())
    maxtri=[]
    for i in range(n):
        maxtri.append(list(map(int,input().split())))
    sums=0
    for j in range(n-1):
        for k in range(n-1):
            if k!=n-j-1:
                sums+=maxtri[j][k]
    return sums
if __name__=="__main__":
    res=f()
    print(res)