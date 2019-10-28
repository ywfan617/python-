def e(error):
    res=1
    i=1
    while True:
        cur=1
        for j in range(1,i+1):
            cur*=j
        res+=(1/cur)
        if 1/cur<error:
            return res
        i+=1
if __name__=="__main__":
    res=e(0.000000001)
    print("{:.6f}".format(res))
