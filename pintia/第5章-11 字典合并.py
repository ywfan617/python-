def com(x):
    if type(x)==int:
        return x
    else:
        return ord(x)
def f():
    tmp1=eval(input())
    tmp2=eval(input())
    for i in tmp2:
        if i in tmp1:
            tmp1[i]+=tmp2[i]
        else:
            tmp1[i]=tmp2[i]
    return tmp1
if __name__=="__main__":
    res=f()
    print(res)
    b=sorted(res,key=com)
    print("{",end="")
    count=1
    for i in b:
        if count==1:
            print("{}:{}".format(i,res[i]),end="")
            count=0
        else:
            print(",{}:{}".format(i,res[i]),end="")
    print("}")