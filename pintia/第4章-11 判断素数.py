import math
def is_prime(num):
    end=int(math.sqrt(num))+1
    i=2
    while i<end:
        if num%i==0:
            return "No"
        i+=1
    return "Yes"
if __name__=="__main__":
    primes=[2,11,111]
    for i in primes:
        print(is_prime(i))