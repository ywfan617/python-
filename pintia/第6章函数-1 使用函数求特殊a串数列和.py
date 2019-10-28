def fn(a,n):
    sums=0
    for i in range(1,n+1):
        sums+=int((str(a)*i))
    return sums
if __name__ == '__main__':
    res=fn(2,3)
    print(res)