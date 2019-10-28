def f1():
    number=input()
    lennum=len(number)#获取数字的长度
    for i in range(lennum):
        if lennum-i==3:
            print(int(number[i])*"B",end="")
        if lennum-i==2:
            print(int(number[i])*"S",end="")
        if lennum-i==1:
            for i in range(1,int(number[i])+1):
                print(i,end="")
def f2():
    number=int(input())
    number_copy=number
    count=0
    res=list()
    while number_copy!=0:
        r=number_copy%10
        number_copy//=10
        count+=1
    print(count)
    for i in range(count):
        if count-i==3:
            cur=number//100
            print(cur*"B",end='')
        if count-i==2:
            cur=number//10%10
            print(cur*"S",end='')
        if count-i==1:
            cur = number%10
            for i in range(1,cur+1):
                print(i, end='')
f2()