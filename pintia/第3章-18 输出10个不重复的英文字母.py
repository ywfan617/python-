def f(strs):
    count=0
    res=""
    for i in strs:
        if count<10 and "A"<=i.upper()<="Z":
            if i.upper() not in res and i.lower() not in res:
                res+=i
                count+=1
    if count!=10:
        print("not found")
    else:
        print(res)
if __name__=="__main__":
    f('poemp134')
    f("This is a test example")