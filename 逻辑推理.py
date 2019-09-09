"""
有A,B,C,D四罪犯嫌疑人被捉，A说：不是我，B说：是C,C说：是D,D说：C骗人,
其中1人是犯罪嫌疑人，其中三人说了真话，一人说了假话，要求找出犯罪嫌疑人
"""
#crimal=input("please input your guess that who is the crimal(A,B,C,D)")
string="ABCD"

for crimal in string:
    count=0
    if crimal !="A":
        count+=1
    if crimal =="C":
        count+=1
    if crimal =="D":
        count+=1
    if crimal !="D":
        count+=1
    if count==3:
        print("{0} is the crimal".format(crimal))


