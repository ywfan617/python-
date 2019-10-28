sentence=input().lower()
chars=dict()
for i in sentence:
    if "a"<=i<="z":
        if i not in chars:
            chars[i]=1
        else:
            chars[i]+=1
char_sort=sorted(chars,key=lambda x:(chars[x],-ord(x)),reverse=True)
print(char_sort[0],chars[char_sort[0]],sep=" ")
