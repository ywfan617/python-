"""
编写程序找出1-100之间所有的孪生素数
孪生素数：二者都是素数，
时间复杂度是O(n^2)
"""
import math
def twinprime(num1,num2):
    lastprime=0
    list1=list()
    for i in range(num1,num2+1):
        flag=1
        for j in range(2,int(math.sqrt(i))+1):
            if  i%j==0 :
                flag=0
                break
        if i==0 or i==1:
            flag=0
        if flag==1:
            if(i-lastprime==2) and lastprime!=0:
                list1.append((lastprime,i))
            lastprime=i
    return list1
list1=twinprime(1,100)
for i in list1:
    print(i)



