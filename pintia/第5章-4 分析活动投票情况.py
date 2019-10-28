def f():
    votes=set(eval(input()))
    base={6,7,8,9,10}
    res=base-votes
    return res
if __name__=="__main__":
    res=f()
    res=sorted(res)
    print(res)