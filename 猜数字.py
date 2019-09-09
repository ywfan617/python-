import random
num1,num2=eval(input("please input the range between two numbers"))
res_number=random.randrange(num1,num2+1)
number=int(input("the number your guess:"))
count=1
while True:
    if number<res_number:
        num1=number
        print("the number is between{}-{}".format(num1,num2))
        number = int(input("the number your guess:"))
        count+=1
    elif number>res_number:
        num2=number
        print("the number is between{}-{}".format(num1,num2))
        number = int(input("the number your guess:"))
        count+=1
    else:
        print("you guess right!")
        break
print(count)