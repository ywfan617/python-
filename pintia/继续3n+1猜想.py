def f():
    n=int(input())#输入数字的个数
    cov_nums=list()
    cri_nums=list()
    raw_nums=list(map(int,input().split()))#输入的数字
    raw_nums.sort(reverse=True)
    for i in raw_nums:
        while i!=1:
            if i%2==0:
                i/=2
            else:
                i=(3*i+1)/2
            if i!=1 and i not in cov_nums:
                cov_nums.append(i)
    for i in raw_nums:
        if i not in cov_nums:
            cri_nums.append(i)
    lennums=len(cri_nums)
    for i in range(lennums):
        print(cri_nums[i],end="")
        if i!=lennums-1:
            print(" ",end="")
f()
