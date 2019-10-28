def select(n):
    monkey=[i for i in range(1,n+1)]
    n=len(monkey)
    i=0
    count=0
    while True:
        count+=1
        if count==3:
            monkey.pop(i)
            count=0
        else:
            i += 1
        if i==len(monkey):
            i=0
        if len(monkey)==1:
            return monkey[i]
if __name__=="__main__":
    res=select(11)
    print(res)