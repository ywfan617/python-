def square3_table(n):
    for i in range(n+1):
        print("pow(3,{})={}".format(i,pow(3,i)))
if __name__=="__main__":
    square3_table(5)