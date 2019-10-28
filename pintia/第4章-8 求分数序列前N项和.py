def seqsum(n):
    above=2
    under=1
    first=above/under
    sums=first
    for i in range(2,n+1):
        wrap=above
        above=above+under
        under=wrap
        sums+=(above/under)
    return sums
if __name__=="__main__":
    n=20
    res=seqsum(n)
    print("{:.2f}".format(res))