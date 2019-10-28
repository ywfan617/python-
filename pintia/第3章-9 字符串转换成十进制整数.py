def f(strs):
    trans={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    strs=strs.upper()  # 返回值为大写字符的字符串
    # print(strs)
    flag=0  # 判断是否在第一个十六进制字符之前存在字符“-”
    first=1  # 判断是否为第一个16进制字符
    res=""
    for i in strs:
        if "0"<=i<="9" or "A"<=i<="F":
            first=0
            res+=i
        if i=="-" and first==1:
            flag=1
    n=len(res)
    num=0
    # print(res)
    for i in range(n):
        num+=16**i*trans[res[n-1-i]]
    if flag==1:
        num=-num
    return num
if __name__=="__main__":
    num=f("+Pxf4+-1!#")
    print(num)
