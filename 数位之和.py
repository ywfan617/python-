def sum_digit_position(number):
    sum = 0
    while number!=0:
        remainder=number%10
        sum+=remainder
        number=number//10
    return sum
a=sum_digit_position(154586)
print(a)