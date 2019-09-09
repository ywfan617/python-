def func1(year):
    res=0
    if year>0 and ((year%4==0 and year%100!=0) or year%400==0):
        res=1
    return res

def func2(lst):
    res=[0]*4
    for i in lst:
        if 0<=i<=18:
            res[0]+=1
        elif 19<=i<=35:
            res[1]+=1
        elif 36<=i<=60:
            res[2]+=1
        elif i>=61:
            res[3]+=1
        else:
            return -1
    return res


if __name__ == "__main__":
    pass