wrong_key=list(input())  # 错误字符列表
cin=input()  # 输入字符
flag=0  # 判断上档键能否使用
res=[]  # 存储能够输出的字符
if "+" in wrong_key:
    flag=1
#print(wrong_key)
#print(flag)
for i in cin:
    if "a"<=i<="z":
        if i.upper() not in wrong_key:
            res.append(i)
    elif "A"<=i<="Z":
        if i not in wrong_key and flag==0:
            res.append(i)
    else:
        if i.upper() not in wrong_key:
            res.append(i)
lenres = len(res)
if res==0:
    print()
else:
    for i in res:
        print(i,end="")


