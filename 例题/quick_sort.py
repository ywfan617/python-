"""
原址排序
"""
import random
#选取最后一个元素作为主元素
def partition1(lst,p,r):
    x=lst[r]
    i=p
    for j in range(p,r):
        if lst[j]<x:
            lst[i],lst[j]=lst[j],lst[i]
            i += 1
    lst[i],lst[r]=lst[r],lst[i]
    return i
def partition2(lst,p,r):
    x=lst[int((p+r)/2)]
    i=p
    k=int((p+r)/2)
    for j in range(p,r+1):
        if lst[j]<x :
            lst[i],lst[j]=lst[j],lst[i]
            if i==k:
                k=j
            i += 1
    lst[i],lst[k]=lst[k],lst[i]
    return i
#随机化版本
def partition3(lst,p,r):
    num=random.randint(p,r)
    x=lst[num]
    x,lst[r]=lst[r],x
    i=p
    for j in range(p,r+1):
        if lst[j]<x :
            lst[i],lst[j]=lst[j],lst[i]
            i += 1
    lst[i],lst[r]=lst[r],lst[i]
    return i
def quicksort(lst,q,r):
    if q<r:
        i=partition2(lst,q,r)
        quicksort(lst,q,i-1)
        quicksort(lst,i+1,r)
res=[1,5,5,6,9,2]
quicksort(res,0,5)
print(res)
