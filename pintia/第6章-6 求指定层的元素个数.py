def f(array,aspect,level):
    length=0
    if aspect==level:
        length+=len(array)
    else:
        for i in array:
            if type(i)==list:
                length+=f(i,aspect,level+1)
    return length
if __name__ == '__main__':
    array=[1,2,[3,4,[5,6],7],[8,9,[1,2,3,4,5]]]
    res=f(array,3,1)
    print(res)