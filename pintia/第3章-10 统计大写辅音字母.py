def f(strs):
    U=["A","E","I","O","U"]
    count=0
    for i in strs:
        if "A"<=i<="Z" and i not in U:
            count+=1
    return count
if __name__=="__main__":
    res=f("HELLO World!")
    print(res)


