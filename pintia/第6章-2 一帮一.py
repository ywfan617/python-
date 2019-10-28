def f():
    n=int(input())
    student=[]
    for i in range(n):
        every=input().split()
        every.append(0)
        student.append(every)
    i=0
    j=n-1
    half=n//2
    while i<half:
        if int(student[i][0])^int(student[j][0]) and student[j][2]==0:
            student[i][2]=1
            student[j][2]=1
            print(student[i][1],student[j][1])
            i+=1
            j=n-1
        else:
            j-=1
if __name__=="__main__":
    f()