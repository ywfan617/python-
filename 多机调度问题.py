"""
多机调度问题1:机器是完全相同的，不同的作业处理时间是独立的
输入:处理机的个数m,作业的个数n,每个作业需要处理的时间总集合T(列表[t1,t2,t3......tn])
输出：处理这批作业最少需要的时间
"""
def schedule1(m,n,T):
    T=sorted(T,reverse=True)#将作业按照非递增顺序排序
    pro=[0]*m
    leasttime=T[0]
    if n>m:
        for i in range(m):
            pro[i]=T[i]
        for j in range(m,n):
            mins=min(pro)
            min_pos=pro.index(mins)
            # mins=pro[0]
            # min_pos=0
            # for k in range(1,m):
            #     if pro[k]<mins:
            #         mins=pro[k]
            #         min_pos=k
            pro[min_pos]+=T[j]
            # if leasttime<pro[min_pos]:
            #     leasttime=pro[min_pos]
        leasttime=max(pro)
    return leasttime
print(schedule1(3,7,[2,14,4,16,6,5,3]))
"""
多线程问题2 :任务是完全相同的，每个服务器的执行时间是独立的
输入:任务的个数n,机器的个数m，每个机器处理任务的时间总集合T[t1,t2,t3.....tm]
输出:处理任务最短的时间
"""
def schedule2(m,n,T):
    T = sorted(T)  # 将处理器执行作业按照非递减顺序排序
    pro = [0] * m
    dotime_and_needtime=[0]*m
    leasttime = 0
    for i in range(n):
        for j in range(m):
            dotime_and_needtime[j]=pro[j]+T[j]
        mins=min(dotime_and_needtime)
        mins_index=dotime_and_needtime.index(mins)
        pro[mins_index]=mins
    return max(pro)
print(schedule2(2,6,[7,10]))
