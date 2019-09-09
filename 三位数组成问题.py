"""
有1，2，3，4 4个数字，能组成多少个互补相同且没有重复的三位数
输入：数字
输出：互补相同且没有重复的三位数字的个数
"""
def count_three_digit(list1):
    len1=len(list1)
    count=0
    numberlist=list()
    for i in range(len1):
        for j in range(len1):
            for k in range(len1):
                if list1[i]!=0 and i!=j and j!=k and i!=k:
                    count+=1
                    number=list1[i]*100+list1[j]*10+list1[k]
                    numberlist.append(number)
    return count,numberlist
count,numberlist=count_three_digit([0,1,2,3,4])
print(count)
print(numberlist)