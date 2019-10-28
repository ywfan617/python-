def output_uppperchar(strs):
    res=""
    for i in strs:
        if "A"<=i<="Z" and i not in res:
            res+=i
    if res=="":
        res="Not Found"
    return res
if __name__=="__main__":
    res=output_uppperchar("FONTNAME and FILENAME")
    print(res)