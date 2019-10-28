#方法一:
def digit_reserve1(number):
    number=int(number)
    res=0
    while number!=0:
        remainder=number%10
        res=10*res+remainder
        number=number//10
    return res

#方法二：利用字符串
def digit_reserve2(number):
    return number[::-1]
number=input("please input a digit:")
digitnumber=digit_reserve1(number)
print(digitnumber)

