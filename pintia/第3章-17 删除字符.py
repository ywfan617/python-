def remove_char(strs,c):
    res=""
    for i in strs:
        if i.upper()!=c.upper():
            res+=i
    return res
if __name__=="__main__":
    res=remove_char(" Bee","E")
    print(res)
