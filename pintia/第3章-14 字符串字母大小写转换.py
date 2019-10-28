def chartrans(strs):
    res=""
    for i in strs:
        if "a"<=i<="z":
            res+=i.upper()
        elif "A"<=i<="Z":
            res+=i.lower()
        elif i=="#":
             continue
        else:
            res+=i
    return res
if __name__=="__main__":
    res=chartrans("Hello World! 123#")
    print(res)