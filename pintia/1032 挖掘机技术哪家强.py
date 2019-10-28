n=int(input())  #参赛人数
res=dict()
for i in range(n):
    inf,grade=list(map(int,input().split()))
    if inf not in res:
        res[inf]=grade
    else:
        res[inf]+=grade
val=sorted(res,key=lambda x:res[x])
print(val[-1],res[val[-1]])
