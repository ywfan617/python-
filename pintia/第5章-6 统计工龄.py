def work():
    n=int(input())
    ages=list(map(int,input().split()))
    work_ages={}
    for i in ages:
        if i not in work_ages:
            work_ages[i]=1
        else:
            work_ages[i]+=1
    return work_ages

if __name__=="__main__":
    work_ages=work()
    res=sorted(work_ages)
    for i in res:
        print("{}:{}".format(i,work_ages[i]))