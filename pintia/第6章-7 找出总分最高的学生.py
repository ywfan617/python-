def f():
    students=[]
    n=int(input())
    for i in range(n):
        students.append(input().split())
    students.sort(key=lambda x:int(x[2])+int(x[3])+int(x[4]),reverse=True)
    return students[0][1],students[0][0],int(students[0][2])+int(students[0][3])+int(students[0][4])
if __name__ == '__main__':
    name,id,total=f()
    print(name,id,total)


