def char_tran(strs):
    strnum=""
    for i in strs:
        if "0"<=i<="9":
            strnum+=i
    if strnum=="":
        return 0
    else:
        return int(strnum)
if __name__=="__main__":
    res=char_tran("freeje85ep")
    print(res)