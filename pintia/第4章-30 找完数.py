def yinzi(num):
    res=[]
    for i in range(1,num):
        if num%i==0:
            res.append(i)
    return res
def is_wanshu(num):
    res=yinzi(num)
    if sum(res)==num:
        return True
    else:
        return False
def print_wanshu(num):
    res=yinzi(num)
    strs=str(res[0])
    for i in res[1:]:
        strs+="+"
        strs+=str(i)
    print("{}={}".format(num,strs))

def f(m,n):
    flag=0
    for i in range(m,n+1):
        if is_wanshu(i):
            print_wanshu(i)
            flag=1
    if flag==0:
        print("None")
if __name__=="__main__":
    f(2,30)