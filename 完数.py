"""
完数：真因子的和等于自己
"""
#判断一个数是否为完数
def is_perfect_number(number):
    number=int(number)
    factor_sum=0
    flag=False
    for i in range(1,number):
        if number%i==0:
            factor_sum+=i
    if factor_sum==number:
        flag=True
    return flag

#输出某个范围的完数
def total_perfect_number(num1,num2):
    res=list()
    for i in range(num1,num2+1):
        if is_perfect_number(i)==True:
            res.append(i)
    return res

num1,num2=eval(input("please input a range:"))
res=total_perfect_number(num1,num2)
print("{0}-{1}的完数有{2}".format(num1,num2,res))

# number=input("please input a digit:")
# res=is_perfect_number(number)
# if res==True:
#     print(number,"is a perfect number")
# else:
#     print(number,"is not a perfect number")

