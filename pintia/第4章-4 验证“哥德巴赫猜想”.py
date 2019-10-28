import math
def is_prime(num):
    end=int(math.sqrt(num))+1
    i=2
    while i<end:
        if num%i==0:
            return False
        i+=1
    return True
def certify1(n):
    end=n//2
    for i in range(2,end):
        if is_prime(i):
            if is_prime(n-i):
                return i,n-i
def certify2(n):
    nums=[0 if i%2==0 and i!=2 else 1 for i in range(n+1)]
    end = n // 2
    fin = int(math.sqrt(n)) + 1
    i=2
    primes=[]
    count=0
    while i<=n:
        if nums[i]!=0:
            count+=1
            primes.append(i)
        p=0
        while i*primes[p]<=n:
            nums[i*primes[p]]=0
            if i%primes[p]==0:
                break
            p+=1
        i+=1
    # for i in range(2,n+1):
    #     if nums[i]:
    #         print(i,end=" ")
    for i in primes:
        if n-i in primes:
            return i,n-i
if __name__=="__main__":
    even=100
    first,end=certify2(even)
    print("{}={}+{}".format(even,first,end))
