def fibonacci(n):
    if n<1:
        return "Invalid"
    f0=1
    f1=1
    res=[]
    res.append(f0)
    if n==1:
        return res
    res.append(f1)
    i=3
    while i<=n:
        f=f0+f1
        f0=f1
        f1=f
        res.append(f)
        i+=1
    return res
if __name__=="__main__":
    n=5
    res=fibonacci(n)
    if res!="Invalid":
        count=0
        for i in range(n):
            print("{:11}".format(res[i]),end="")
            count+=1
            if count%5==0:
                print()
    else:
        print("Invalid")

