# 鞍点是唯一的
def f():
    n=int(input())
    maxtri=[]
    for i in range(n):
        maxtri.append(list(map(int,input().split())))
    for i in range(n):
        maxpos=0
        for j in range(1,n):
            if maxtri[i][j]>maxtri[i][maxpos]:
                maxpos=j
        #print("第{}行的最大值的下标为{}".format(i,maxpos))
        minpos = 0
        for k in range(1,n):
            if maxtri[minpos][maxpos]>maxtri[k][maxpos]:
                minpos=k
        #print("第{}列的最小值的下标为{}".format(maxpos,minpos))
        if i==minpos:
            return (minpos,maxpos)
    return None
if __name__=="__main__":
    res=f()
    print(res)