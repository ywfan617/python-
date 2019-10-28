"""易错点总结：*******:
1.程序的模块性
2.循环边界的判断，很重要
3.思考事物的思维方式
4.
"""
def merge_sort(raw_seq,mid_seq):
    n=[[i] for i in raw_seq]
    flag=0
    while len(n)>1:
        middle = []
        for i in range(0,len(n),2):
            try:
                n[i].extend(n[i+1])
                middle.append(n[i])
            except:
                middle.append(n[i])
        for i in middle:
            i.sort()
        n=middle
        res=[]
        for i in n:
            for j in i:
                res.append(j)
        if res==mid_seq:
            flag=1
        if flag==1:   # 逻辑错误输出：执行完上面的if便执行下面的if
            return res

def insert_sort(raw_seq,mid_seq):
    n=len(raw_seq)
    flag = 0
    for i in range(1,n):
        position=i
        for j in range(i-1,-1,-1):
            if raw_seq[i]<raw_seq[j]:
                position-=1
            else:  # else两行可以省略，我们的关键是找到位置
                break
        entry = raw_seq.pop(i)
        raw_seq.insert(position, entry)
        if flag == 1:
            return raw_seq
        if raw_seq==mid_seq:
            flag=1
    return False

def main():
    n = int(input())
    raw_seq = list(map(int, input().split()))
    raw_seq_copy = raw_seq.copy()
    mid_seq = list(map(int, input().split()))
    res=insert_sort(raw_seq,mid_seq)
    if res!=False:
        print("Insertion Sort")
        for i in range(n-1):
            print(res[i],end=" ")
        print(res[n-1])
    else:
        res = merge_sort(raw_seq_copy, mid_seq)
        print("Merge Sort")
        for i in range(n-1):
            print(res[i],end=" ")
        print(res[n-1])

main()