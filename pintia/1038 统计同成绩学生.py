#自己写的程序有超时,对比网上的程序main3(),由于分数最高100，
# 因此可以直接创建一个100大小的列表，
# 存储分数的个数
def main():
    n=input()
    grades=list(map(int,input().split()))
    #print(grades)
    marks=list(map(int,input().split()))  # marks中存储的给出分数的个数
    #print(marks)
    for i in range(1,marks[0]+1):
        if i==1:
            print(grades.count(marks[i]),sep="",end="")
        else:
            print(" ",grades.count(marks[i]),sep="",end="")

def binary_search(grades,mark):
    length=len(grades)
    left=0
    right=length-1
    mid=(left+right)//2
    while left<=right:
        if mark<grades[mid]:
            right=mid-1
        elif mark>grades[mid]:
            left=mid+1
        else:
            return mid
        mid=(left+right)//2
    return -1

def main1():
    n = input()
    grades = list(map(int, input().split()))
    # print(grades)
    marks = list(map(int, input().split()))  # marks中存储的给出分数的个数
    # print(marks)
    grades.sort()
    for i in range(1, marks[0] + 1):
        count=0
        mid=binary_search(grades, marks[i])
        while mid>=0:
            count+=1
            grades.pop(mid)
            mid = binary_search(grades, marks[i])
        if i==1:
            print(count,end="")
        else:
            print(" ",count,sep="",end="")
main1()
def main3():
    n = eval(input())
    score = list(map(int, input().split()))
    grade = [0 for i in range(101)]
    for sc in score:
        grade[sc] += 1

    ans = []
    lst = list(map(int, input().split()))
    for sc in lst[1:]:
        ans.append(str(grade[sc]))
    print(' '.join(ans))