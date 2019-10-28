def find_char(strs,m):
    length=len(strs)
    for i in range(length-1,-1,-1):
        if strs[i]==m:
            return i
    return -1
if __name__=="__main__":
    index=find_char("das","")
    if index>-1:
        print(index)
    else:
        print("Not Found")