def insertion_sort1(a):
    lens=len(a)
    for i in range(1,lens):
        current=a[i]
        position=i#set a flag
        while position>0 and current<a[position-1]:
            a[position] = a[position - 1]
            position-=1
        a[position]=current

def insertion_sort2(a):
    lens=len(a)
    for i in range(1,lens):
        current=a[i]
        position=i
        for h in range(position,0,-1):
            if current<a[position-1]:
                a[position]=a[position-1]
                position-=1

        # for g in range(i,position,-1):
        #     a[g]=a[g-1]
        a[position]=current

c=[1,5,6,9,12,2,3,7,14]
insertion_sort1(c)
print(c)




