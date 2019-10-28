def fibonacci(n):
    f0=1
    f1=1
    val=f1
    while True:
        if val>n:
            return val
        val=f0+f1
        f0=f1
        f1=val
if __name__=="__main__":
    res=fibonacci(10)
    print(res)

