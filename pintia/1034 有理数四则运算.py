num1,num2=input().split()

# 求两个数的最大公因数
def yin(num1,num2):
    if num1>num2:
        num1,num2=num2,num1
    while num2%num1!=0:
        reminder=num2%num1
        num2=num1
        num1=reminder
    return num1
def bei(num1,num2):
    return num1*num2//yin(num1,num2)
def add(num1,num2):
    num1_z,num1_m=list(map(int,num1.split("/")))
    num2_z, num2_m = list(map(int, num2.split("/")))
    res_m=bei(num1_m,num2_m)
    res_z=res_m//num1_m*num1_z+res_m//num2_m*num2_z
    return str(res_z)+"/"+str(res_m)
def minus(num1,num2):
    num1_z, num1_m = list(map(int, num1.split("/")))
    num2_z, num2_m = list(map(int, num2.split("/")))
    res_m = bei(num1_m, num2_m)
    res_z = res_m//num1_m*num1_z-res_m//num2_m*num2_z
    return  str(res_z)+"/"+str(res_m)

def plus(num1,num2):
    num1_z, num1_m = list(map(int, num1.split("/")))
    num2_z, num2_m = list(map(int, num2.split("/")))
    res_z=num1_z*num2_z
    res_m=num1_m*num2_m
    return str(res_z)+"/"+str(res_m)
def div(num1,num2):
    num1_z, num1_m = list(map(int, num1.split("/")))
    num2_z, num2_m = list(map(int, num2.split("/")))
    if num2_m==0 or num2_z==0:
        return "Inf"
    else:
        res_z = num1_z * num2_m
        res_m = num1_m * num2_z
        if res_m < 0:
            return str(-res_z) + "/" + str(-res_m)
        else:
            return str(res_z)+"/"+str(res_m)

# 求最简真分数
def sim(num):
    num_z, num_m = list(map(int,num.split("/")))
    if num_z<0:
        res="("+"-"
        yinzi=yin(abs(num_z),num_m)
        num_z=abs(num_z)//yinzi
        num_m=num_m//yinzi
        if num_z>num_m:
            a=num_z//num_m
            b=num_z%num_m
            if b==0:
                return res + str(a) + ")"
            else:
                return res+str(a)+" "+str(b)+"/"+str(num_m)+")"
        elif num_z<num_m:
            return res+str(num_z)+"/"+str(num_m)+")"
        else:
            return res+str(1)+")"
    elif num_z>0:
        yinzi = yin(num_z, num_m)
        num_z = abs(num_z) // yinzi
        num_m = num_m // yinzi
        if num_z>num_m:
            a=num_z//num_m
            b=num_z%num_m
            if b==0:
                return str(a)
            else:
                return str(a)+" "+str(b)+"/"+str(num_m)
        elif num_z<num_m:
            return  str(num_z)+"/"+str(num_m)
        else:
            return str(1)
    else:
        return  str(0)
adds=add(num1,num2)
minuss=minus(num1,num2)
pluss=plus(num1,num2)
divs=div(num1,num2)

print(sim(num1),"+",sim(num2),"=",sim(adds),sep=" ")
print(sim(num1),"-",sim(num2),"=",sim(minuss),sep=" ")
print(sim(num1),"*",sim(num2),"=",sim(pluss),sep=" ")
if divs=="Inf":
    print(sim(num1), "/", sim(num2), "=", divs, sep=" ")
else:
    print(sim(num1),"/",sim(num2),"=",sim(divs),sep=" ")
