def eat_peach(n):
    res=1
    for i in range(1,n):
        res=(res+1)*2
    return res
if __name__=="__main__":
    res=eat_peach(5)
    print(res)