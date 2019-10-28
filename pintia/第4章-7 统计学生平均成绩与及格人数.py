def grades(grades,n):
    count=0
    sums=0
    for i in grades:
        if i>=60:
            count+=1
        sums+=i
    avg=sums/n
    return avg,count
if __name__=="__main__":
    marks=[77,54,92,73,60]
    n=len(marks)
    avg,count=grades(marks,n)
    print("average={}".format(avg))
    print("count={}".format(count))
