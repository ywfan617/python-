#考点：字符串的压缩
day_list=["MON","TUE","WED","THU","FRI","SAT","SUN"]
str1=input()
#print(str1)
str2=input()
#print(str2)
str3=input()
#print(str3)
str4=input()
#print(str4)
zip1=list(zip(str1,str2))
zip2=list(zip(str3,str4))
#print(zip1)
#print(zip2)
lenzip1=len(zip1)
lenzip2=len(zip2)
first=1
for index in range(lenzip1):
    if first==1 and zip1[index][0]==zip1[index][1] and "A"<=zip1[index][0]<="G":
        char=zip1[index][0]
        res=ord(char)-ord("A")+1
        print(day_list[res-1],end='')
        print(" ",end="")
        first=2
        continue
    if first==2 and zip1[index][0]==zip1[index][1]:
        char=zip1[index][0]
        if "0"<=char<="9":
            print(0,char,sep="",end="")
            break
        if "A"<=char<="N":
            res=ord(char)-ord("A")+10
            print(res,end="")
            break
print(":",end="")
for index in range(lenzip2):
    if zip2[index][0]==zip2[index][1]and ("a"<=zip2[index][0]<="z" or "A"<=zip2[index][0]<="Z"):
        if 0<=index<=9:
            print(0,index,sep="",end="")
        else:
            print(index,end="")
        break
