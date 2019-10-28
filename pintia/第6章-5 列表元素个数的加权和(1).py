def f(array,weight):
    sum_weight=0
    for i in array:
        if type(i)==list:
            sum_weight+=f(i,weight+1)
        else:
            sum_weight+=weight

    return sum_weight
if __name__ == '__main__':
    array=[1,2,[3,4,[5,6],7],8]
    res=f(array,1)
    print(res)