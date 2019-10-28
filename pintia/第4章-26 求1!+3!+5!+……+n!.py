def stage(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res
def f(n):
    sums=0
    for i in range(1,n+1):
        if i%2!=0:
            sums+=stage(i)
    return n,sums
if __name__=="__main__":
    for i in range(1,5+1):
        res=stage(i)
        print(res)
    n,s=f(5)
    print("n={},s={}".format(n,s))