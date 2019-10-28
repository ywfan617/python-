#十分简单，不用关注
def output_square(n,a): #n,a的类型为字符串
    point=int(n)/2-int(n)//2
    if point>0:
        row=int(n)//2+1
    else:
        row=int(n)//2
    print(int(n)*a)
    for i in range(row-2):
        print(a," "*(int(n)-2),a,sep="")
    print(int(n) * a,end="")
def main():
    n,a=input().split()
    output_square(n,a)
main()
# a = input().split()
# a[0] = int(a[0])
# if a[0]%2!=0:
#     k = a[0]//2+1
# else:
#     k = a[0]//2
# for i in range(a[0]-1):
#     print(a[1],end="")
# print(a[1])
# for i in range(k-2):
#     print("%s%s%s"%(a[1]," "*(a[0]-2),a[1]))
# for i in range(a[0]):
#     print(a[1],end="")
