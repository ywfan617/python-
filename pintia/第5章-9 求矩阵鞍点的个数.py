def f():
    n=int(input())
    maxtri=[]
    count=0
    for i in range(n):
        maxtri.append(list(map(int,input().split())))
    for i in range(n):
        maxpos=0
        for j in range(1,n):
            if maxtri[i][j]>maxtri[i][maxpos]:
                maxpos=j
        for k in range(n):
            if maxtri[i][k]==maxtri[i][maxpos]:
                minpos=0
                for m in range(1,n):
                    if maxtri[m][k]<maxtri[minpos][k]:
                        minpos=m
                if maxtri[i][k]==maxtri[minpos][k]:
                    count+=1
    return count

if __name__=="__main__":
    res=f()
    print(res)