raw=input().upper() #输入字符串
res=input().upper() #实际输出的字符串
diff=[] #缺少的字符
for i in raw:
    if i not in res and i not in diff:
        diff.append(i)
for i in diff:
    print(i,end="")