def e(n):
    res=1
    for i in range(1,n+1):
        cur=1
        for j in range(1,i+1):
            cur*=j
        res+=1/cur
    return res
if __name__=="__main__":
    res=e(10)
    print("{:.8f}".format(res))