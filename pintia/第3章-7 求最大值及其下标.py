def f(nums):
    n=len(nums)
    maxv=nums[0]
    idnex=0
    for i in range(1,n):
        if nums[i]>maxv:
            maxv=nums[i]
            index=i
    return maxv,index
if __name__=="__main__":
    maxv,index=f([2,8,10,1,9,10])
    print(maxv,index)
