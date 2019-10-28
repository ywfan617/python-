"""
设有n个活动的集合e={1，2，…，n}，其中每个活动都要求使用同一资源，如演讲会场等，
而在同一时间内只有一个活动能使用这一资源。
每个活动i都有一个要求使用该资源的起始时间si和一个结束时间fi,且si< fi。
如果选择了活动i，则它在半开时间区间[si，fi]内占用资源。
若区间[si，fi]与区间[sj，fj]不相交，则称活动i与活动j是相容的。也就是说，当si≥fi或sj≥fj时，
活动i与活动j相容。活动安排问题就是要在所给的活动集合中选出最大的相容活动子集合。
————————————————
"""
def activity_select(starts,finals):
    n=len(starts)
    intervue=list(zip(starts,finals))
    intervue.sort(key=lambda x:x[1])
    starts,finals=zip(*intervue)
    i=1
    j=0
    res=[(starts[0],finals[0])]
    while i<n and j<n:
        if starts[i]>finals[j]:
            res.append((starts[i],finals[i]))
            j=i
        i+=1
    print(starts, finals)
    return res

if __name__=="__main__":
    res=activity_select([1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12],[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    print(res)

