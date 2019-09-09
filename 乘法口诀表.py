def multiply_form(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("{1}*{0}={2}".format(i,j,i*j),end=" ")
        print()
multiply_form(10)