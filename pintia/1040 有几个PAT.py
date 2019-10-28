import re

def f1(strs):
    count = 0
    lens=len(strs)
    position=lens
    stack=[0]
    top=0
    for i in range(lens-1,-1,-1):
        if strs[i]=="P":
            count=stack[top]
            for j in range(i+1,position):
                if strs[j]=="A":
                    count+=strs[j+1:].count("T")
            top+=1
            stack.append(count)
            position=i
    return sum(stack)
def f2(strs):
    lens = len(strs)
    t=0
    a=0
    count=0
    for i in range(lens - 1, -1, -1):
        if strs[i]=="P":
            count+=a
        if strs[i]=="A":
            a+=t
        if strs[i]=="T":
            t+=1
    return count
raw=input()
print(f2(raw))