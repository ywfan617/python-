#注意钱不够的时候的判断，需要绝对值，输出带上符号
def main():
    p,a=input().split()
    p=list(map(int,p.split(".")))  # 应付的钱
    a=list(map(int,a.split(".")))  # 实付的钱
    yinfu=p[0]*17*29+p[1]*29+p[2]
    shifu=a[0]*17*29+a[1]*29+a[2]
    diff=shifu-yinfu
    flag=0
    if diff<0:
        flag=1
        diff=-diff
    Galleon=diff//29//17
    Sickle=diff//29%17
    Knut=diff%29
    if flag==0:
        print(Galleon,Sickle,Knut,sep=".")
    else:
        print("-",end="")
        print(Galleon, Sickle, Knut, sep=".")
main()