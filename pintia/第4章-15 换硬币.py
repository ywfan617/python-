# 求解三元一次方程需要两个循环
def change(money):
    max5=money//5
    count=0
    for i in range(max5,0,-1):
        cur=money-5*i
        max2=cur//2
        for j in range(max2,0,-1):
            remainder=money-5*i-2*j
            if remainder>0:
                print("fen5:{}, fen2:{}, fen1:{}, total:{}".format(i,j,remainder,remainder+i+j))
                count+=1
    return count
def change2(money):
    count=0
    max5=money//5
    for i in range(1,max5+1):
        cur=(money-i*5)
        max2=cur//2
        for j in range(1,max2+1):
            remainder=cur-j*2
            if remainder>0:
                print("fen5:{}, fen2:{}, fen1:{}, total:{}".format(i, j, remainder, remainder + i + j))
                count += 1
    return count
if __name__=="__main__":
    res=change2(13)
    print("count={}".format(res))

