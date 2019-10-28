"""角古猜想：对于任何一个正整数，如果是奇数，则乘3加1，如果是偶数，则除以2，得到的结果再按照上述
规则重复处理，最终结果是1
"""
#打印角古猜想的过程
def jiaogu_guess(number):
    number=int(number)
    while number!=1:
        if number %2==0:
            print("{0}/2={1}".format(number, number / 2))
            number=number/2
        else:
            print("{0}*3+1={1}".format(number, number * 3 + 1))
            number=3*number+1
number=input("please input a positive digit:")
jiaogu_guess(number)
