import math
def is_prime(number):
    number=int(number)
    cycle=2
    if number==0 or number==1:
        return False
    while cycle<math.sqrt(number)+1:
        if number%cycle==0:
            return False
        cycle+=1
    return True
number=input("please input a number:")
res=is_prime(number)
if res==True :
    print(number,"is a prime")
else:
    print(number,"isn't a prime!")