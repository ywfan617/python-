n=int(input())
w=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
m=["1","0","X","9","8","7","6","5","4","3","2"]
res=[]
count=0
for i in range(n):
    card = input()
    sumnum = 0
    flag=0
    for i in range(17):
        if "0"<=card[i]<="9":
            sumnum+=int(card[i])*w[i]
        else:
            flag=1
            break
    if flag==1:
        res.append(card)
    else:
        ver=sumnum%11
        if m[ver]!=card[-1]:
            res.append(card)
        else:
            count+=1
print(count)
if len(res)==0:
    print("All passed")
else:
    for i in res:
        print(i)
