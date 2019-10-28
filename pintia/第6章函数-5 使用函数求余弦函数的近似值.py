def stage(num):
    mul=1
    if num==0:
        return mul
    else:
        for i in range(1,num+1):
            mul*=i
    return mul

def funcos(eps,x):
    i = 0
    count=0
    cosx=0
    while abs((((-1)**count)*x**i)/stage(i))>=eps:
        cosx+=(((-1)**count)*x**i)/stage(i)
        i+=2
        count+=1
    return cosx

if __name__ == '__main__':
    res=funcos(0.0001,-3.1)
    print("{:.4f}".format(res))