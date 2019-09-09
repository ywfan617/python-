a,b,c=eval(input("请输入三个数:"))
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
print("这三个数的顺序是:",a,b,c)