def fib(n):
    f0=1
    f1=1
    for i in range(2,n+1):
        f=f0+f1
        f0=f1
        f1=f
    return f
def PrintFN(m,n):
    res=[]
    f0=1
    f1=1
    while True:
        f = f0 + f1
        f0 = f1
        f1 = f
        if m<=f<=n:
            res.append(f)
        if f>n:
            break
    return res

if __name__ == '__main__':
    res=fib(6)
    res=PrintFN(20,100)
    print(res)