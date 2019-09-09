import random
import time
def poition_counts(numbers):
    count=0
    for i in range(numbers):
        x,y=random.random(),random.random()
        if (x*x+y*y)<=1:
            count+=1
    return count
def main():
    a=time.time()
    numbers=eval(input("please input the number of points:"))
    counts=poition_counts(numbers)
    pi=4*counts/numbers
    b=time.time()
    print(pi)
    print("The process spends {}s".format(b-a))
main()

