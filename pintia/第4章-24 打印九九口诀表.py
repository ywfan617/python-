def mul_table(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("{}*{}={:<4}".format(j,i,i*j),end="")
        print()
if __name__=="__main__":
    mul_table(8)