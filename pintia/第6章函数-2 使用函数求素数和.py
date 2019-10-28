import math
def prime(num):
    end=int(math.sqrt(num)+1)
    for i in range(2,end):
        if num%i==0:
            return False
    if num>1:
        return True
    else:
        return  False
def primesum(m,n):
    sums=0
    for i in range(m,n+1):
        if prime(i):
            prime(i)
            sums+=i
    return sums
if __name__ == '__main__':
    res=primesum(1,10)
    print(res)