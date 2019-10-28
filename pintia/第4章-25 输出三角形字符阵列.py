def f(n):
    start=65
    for i in range(n):
        for j in range(n-i):
            print(chr(start),end=" ")
            start+=1
        print()
if __name__=="__main__":
    f(5)
