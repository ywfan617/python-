def f():
    count=int(input())
    i=0
    while i<count:
        a,b,c=list(map(int,input().split()))
        i += 1
        if a+b>c:
            print("Case #{}: true".format(i))
        else:
            print("Case #{}: false".format(i))
f()