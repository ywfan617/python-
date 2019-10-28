# 三角形的判断条件只需要满足最小的两边之和大于第三边即可
def f():
    a,b,c=list(sorted(list(map(int,input().split()))))
    print(a,b,c)
    if a+b>c:
        print("yes")
    else:
        print("no")
if __name__=="__main__":
    f()

