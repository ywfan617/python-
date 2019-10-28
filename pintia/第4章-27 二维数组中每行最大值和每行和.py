import math
def maxtri(nums):
    length=len(nums)
    n=int(math.sqrt(length))
    maxtri_num=[[0 for j in range(n+2)]for i in range(n)]
    j=0
    k=0
    maxval=float("-inf")
    sums=0
    for i in range(length):
        maxtri_num[j][k]=nums[i]
        sums+=nums[i]
        k += 1
        if maxval<nums[i]:
            maxval=nums[i]
        if (i+1)%n==0:
            maxtri_num[j][k]=maxval
            maxtri_num[j][k+1]=sums
            j+=1
            k=0
            maxval=float("-inf")
            sums=0
    return maxtri_num
if __name__=="__main__":
    res=maxtri([3,6,5,9,8,2,1,4,5])
    print(res)