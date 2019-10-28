#利用牛顿迭代法求解一个数的平方根
def solution_square_root(number):
    number=int(number)
    x0=number/2
    x1=x0+number/x0
    count=0
    while abs(x1-x0)>10**-8:
        x0=x1
        x1=0.5*(x0+number/x0)
        count+=1
    return x1,count
number=input("please input a digit:")
res,count=solution_square_root(number)
print(res)
print("迭代次数:",count)