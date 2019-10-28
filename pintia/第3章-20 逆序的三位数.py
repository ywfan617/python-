def reverse_num(num):
    res=0
    while num!=0:
        remain=num%10
        res=10*res+remain
        num//=10
    return res
if __name__=="__main__":
    res=reverse_num(700)
    print(res)