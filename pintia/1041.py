n=int(input())
students={}
for i in range(n):
    card,test,real=input().split()
    students[test]=[card,real]
m=input()
quary=input().split()
for i in quary:
    print(students[i][0],students[i][1],sep=" ")
