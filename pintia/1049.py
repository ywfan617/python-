def f1():
    n=int(input())
    nums=list(map(float,input().split()))
    sums=0
    for i in range(n):
        for j in range(i+1,n+1):
            sums+=sum(nums[i:j])
    print("{:.2f}".format(sums))
def f2():
    n = int(input())
    nums = list(map(float, input().split()))
    sums = 0
    for i in range(n):
        sums+=((n-i)+i*(n-i))*nums[i]
    print("{:.2f}".format(sums))
f2()