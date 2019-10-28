def words(strs):
    count=0
    flag=0
    for i in strs:
        if flag==0 and i!=" ":
            count+=1
            flag=1
        elif i==" " and flag==1:
            flag=0
    return count
if __name__=="__main__":
    count=words("Let's go to room 209.")
    print(count)
