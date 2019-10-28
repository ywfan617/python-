def factor(m,n):
    # 辗转相除法
    if m<n:
        m,n=n,m
    while m%n!=0:
        remainder=m%n
        m=n
        n=remainder
    return n
if __name__=="__main__":
    m,n=511,292
    res=factor(m,n)
    print(res,m*n//res)