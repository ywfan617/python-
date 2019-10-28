def f():
    m,n=list(map(int,input().split()))
    res=[]
    for i in range(m,n+1):
        if i%(3*5*7)==0:
            res.append(i)
    return res
if __name__=="__main__":
    res=f()
    print(len(res))