import math
def is_prime(num):
    end=int(math.sqrt(num))+1
    i=2
    while i<end:
        if num%i==0:
            return False
        i+=1
    return True
def prime(m,n):
    count=0
    sums=0
    for i in range(m,n+1):
        if is_prime(i):
            sums+=i
            count+=1
    return count, sums
if __name__=="__main__":
    count,sums=prime(10,31)
    print(count,sums,sep=" ")