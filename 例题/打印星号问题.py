#左对齐
def printstars1(lines):
    for i in range(1,lines+1):
        print(i*"*")

#右对齐
def printstars2(lines):
    for i in range(1,lines+1):
        print((lines-i)*" ",end="")
        print(i*"*")

#右对齐
def printstars3(lines):
    for i in range(1,lines+1):
        for g in range(lines-i):
            print(" ",end="")
        for g in range(i):
            print("*",end="")
        print()

#正三角
def printstars4(lines):
    for i in range(1,lines+1):
        print((lines-i)*" ", end="")
        print((2*i-1 )* "*",end="")
        print()#每循环一次换一行

#倒三角
def printstars5(lines):
    for i in range(1,lines+1):
        print((i-1)*" ", end="")
        print((2*(lines-i)+1)* "*",end="")
        #print(int((count- i)/2) * " ", end=""）
        print()#每循环一次换一行

#右三角
def printstars6(lines):
    for i in range(1,int((lines-1)/2)+2):
        print(i*"*")
    for j in range(1,int((lines-1)/2)+1):
        print(int((lines-1)/2+1-j)*"*")

#左三角
def printstars7(lines):
    for i in range(1,int((lines-1)/2)+2):
        print((int((lines-1)/2+1)-i)*" ",end="")
        print(i*"*")
    for j in range(1,int((lines-1)/2+1)):
        print(j * " ", end="")
        print(int((lines-1)/2+1-j)*"*")

#主函数
def main():
     lines=int(input("请输入打印星号的行数:"))
     printstars7(lines)
main()
