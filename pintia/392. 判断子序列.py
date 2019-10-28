def isSubsequence(s,t):
    i=0
    n=len(t)
    for char in s:
        flag=0
        while i<n:
            if t[i]==char:
                flag=1
                i+=1
                break
            else:
                i+=1
        if flag==0:
            return False
    return True
# 字符串切片的利用
def isSubsequence2(s,t):
    for i in s:
        pos=t.find(i)
        if pos>=0:
            t=t[pos+1:]
        else:
            return False
    return True
res=isSubsequence("333","3")
print(res)