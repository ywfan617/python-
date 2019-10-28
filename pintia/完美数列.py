# N,p=list(map(int,input().split()))
# nums=list(map(int,input().split()))
#
# nums.sort()
# for length in range(N,0,-1):
#     for j in range(0,N-length+1):
#         flag=0
#         if nums[j]*p>=nums[j+length-1]:
#             print(length)
#             flag=1
#             break
#     if flag==1:
#         break


def f():
    N, p = [int(i) for i in input().split()]
    A = sorted([int(i) for i in input().split()])
    maxlen = 0
    for i in range(N):  # 一层循环
        for j in range(i + maxlen, N):  # 二层循环开始，但是要进行跨越
            if A[i] * p < A[j]:  # 探测数列的结尾点
                maxlen = j-i  # 易错点：条件判断未必执行
                break
            maxlen += 1  # 查找的数列长度

    print(maxlen)
f()