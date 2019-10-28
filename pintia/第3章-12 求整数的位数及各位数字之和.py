def f(num):
    num=str(num)
    n=len(num)
    sums=sum(map(int,num))
    return n, sums
if __name__=="__main__":
    n,sums=f(567)
    print(n,sums)