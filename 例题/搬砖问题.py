#---问题: 有30块砖头，三个人搬走，男人每人搬三块，女人每人搬两块，小孩2人搬一块，
#         问，全部一次性搬走，共需要几个男人，几个女人，几个孩子？
import math
import time
#---穷举法
def moveBlock1(number):
    dict1=dict()
    count=0
    for man in range(1,math.ceil(number/3)+1):
        for women in range(1,math.ceil(number/2)+1):
            for children in range(2,number*2,2):
                if man*3+women*2+children/2==number:
                    count+=1
                    dict1["第"+str(count)+"种结果:"]=(man,women,children)
    return dict1
#---优化法
def moveBlock2(number):
    dict1=dict()
    count=0
    for man in range(1,math.ceil(number/3)):
        for women in range(1,math.ceil(number/2)):
            children=(number-(man*3+women*2))*2
            if children>0:
                count+=1
                dict1["第"+str(count)+"种结果:"]=(man,women,children)
    return dict1
def main():
    number=int(input("请输入需要搬运的专砖数:"))
    starttime=time.time()
    dict1=moveBlock1(number)
    endtime=time.time()
    print("计算过程花费了",(endtime-starttime))
    print("这次搬砖共需要:")
    for i in dict1.keys():
        print(i,"男人需要"+str(dict1[i][0])+"人", "女人需要"+str(dict1[i][1])+"人","小孩需要"+str(dict1[i][2])+"人")
    print("计算过程花费了", (endtime - starttime))
main()


