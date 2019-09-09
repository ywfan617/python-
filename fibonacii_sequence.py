import math
"""
input:n(一个正整数)
output:f(n)=f(n-1)+f(n-2);f(1)=1,f(2)=1
"""
#直接递归法，时间复杂度:O(2^n)
def fibonacii_sequence1(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacii_sequence1(n-2)+fibonacii_sequence1(n-1)
print(fibonacii_sequence1(10))
#DP法，时间复杂度:O(n)
def fibonacii_sequence2(n):
    #设置一张规划表，记录每次的计算
    res=[0]*(n+1)
    res[0]=0
    res[1]=1
    if n==0 :
        return 0
    if n==1:
        return 1
    for i in range(2,n+1):
        res[i]=res[i-1]+res[i-2]
    return res[i]
print(fibonacii_sequence2(10))
#公式法,时间复杂度:O(1),但是存在精度问题
def fibonacii_sequence3(n):
    return (1/math.sqrt(5))*(((1+math.sqrt(5))/2)**n-((1-math.sqrt(5))/2)**n)
print(fibonacii_sequence3(10))
#递推关系优化,时间复杂度:O(n),time_complexity,空间复杂度:O(1),space_complexity
def fibonacii_sequence4(n):
    last_but_one=0
    last_value=1
    for  i in range(2,n+1):
        current=last_but_one+last_value
        last_but_one=last_value
        last_value=current
    return current
print(fibonacii_sequence4(10))
#矩阵法求解动态规划
def list1_multiply_list1(list1,list2):
    m=len(list1)
    per=len(list1[0])
    n=len(list2)
    res=[[0 for i in range(m)]for j in range(n)]
    for i in range(m):
        for j in range(n):
            sum1=0
            for k in range(per):
                sum1=sum1+(list1[i][k]*list2[k][j])
            res[i][j]=sum1
    return res
def A_multipiy_A(n):
    res=[[1,1],[1,0]]

    if n==1:
        return res
    program=[]
    if n%2==0:
        cur = A_multipiy_A(n / 2)
        cur = list1_multiply_list1(cur,cur)
    if n%2!=0:
        cur=A_multipiy_A((n-1)/2)
        middle=list1_multiply_list1(cur,cur)
        cur=list1_multiply_list1(middle,res)
    return cur
def fibonacii_sequence5(n):
    if n==0:
        return 0
    else:
        return A_multipiy_A(n-1)[0][0]
print(fibonacii_sequence5(10))

