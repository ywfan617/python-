def opr():
    first=int(input())
    operate=input()
    second=int(input())
    if operate=="+":
        print(first+second)
    elif operate=="-":
        print(first-second)
    elif operate=="*":
        print(first*second)
    else:
        if second==0:
            print("divided by zero")
        else:
            print("{:.2f}".format(first/second))
if __name__=="__main__":
    opr()