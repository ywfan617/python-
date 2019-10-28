"""
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。
"""
def move1(num,val):
    len1=len(num)
    list1=[val]*len1
    j=0
    for i in range(len1):
        if num[i]!=val:
            list1[j]=num[i]
            j+=1
    return j
#设置两个指针，一个快的，一个慢点
def move2(num,val):
    len1=len(num)
    j=0
    for i in range(len1):
        if num[i]!=val:
            num[j]=num[i]
            j+=1
    return j
#交换元素法
def move3(num,val):
    len1=len(num)
    n=len1
    i=0
    while i<n:
        if num[i]==val:
            num[i]=num[n-1]
            n-=1
        else:
            i+=1
    return n
res=move3([0,1,2,2,3,0,4,2],2)
print(res)
