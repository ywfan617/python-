def water_flower(n):
    start=10**(n-1)
    end=10**n
    for i in range(start,end):
        stri=str(i)
        sums=0
        for j in stri:
            sums+=int(j)**n
        if sums==i:
            print(i)
water_flower(4)