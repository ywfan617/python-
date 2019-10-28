def f(array):
    sums=0
    itertype=[list,tuple,set]
    for i in array:
        if type(i)==int or type(i)==float:
            sums+=i
        else:
            if type(i) in itertype:
                sums+=f(i)
    return sums
if __name__ == '__main__':
    array=[11,2,[3,7],(68,-1),"123",9]
    res=f(array)
    print(res)
