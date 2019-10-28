import copy
def new_combo(raw, tmp, res):
    n = len(raw)
    for i in range(n):
        raw[0], raw[i] = raw[i], raw[0]
        tmp.append(raw[0])
        if n == 1:
            res.append(copy.deepcopy(tmp))
        new_combo(raw[1:], tmp,res)
        tmp.pop()
        raw[0], raw[i] = raw[i], raw[0]
def all_range(n):
    raw=[]
    res=[]
    for i in range(1,n+1):
        raw.append(i)
    new_combo(raw,[],res)
    return res

if __name__ == '__main__':
    res=all_range(4)
    res.sort()
    for i in res:
        for j in i:
            print(j,end="")
        print()



