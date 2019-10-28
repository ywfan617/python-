def f(strs):
    n=len(strs)
    res=""
    for i in range(n):
        if "A"<=strs[i]<="Z":
            res+=chr(90-(ord(strs[i])-65))
        else:
            res+=strs[i]
    return res
if __name__=="__main__":
    res=f("Only the 11 CAPItaL LeTtERS are replaced.")
    print(res)
