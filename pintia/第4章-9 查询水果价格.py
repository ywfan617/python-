def fruit_price():
    fruits=["exit",3,2.5,4.1,10.2]
    print("[1] apple")
    print("[2] pear")
    print("[3] orange")
    print("[4] grape")
    print("[0] exit" )
    count = 0
    while True:
        if count==5:
            break
        choice = int(input())
        if 0<choice<5:
            print("price={:.2f}".format(fruits[choice]))
            count+=1
        elif choice>=5:
            count += 1
            print("price={}".format(0))
        else:
            break
if __name__=="__main__":
    fruit_price()