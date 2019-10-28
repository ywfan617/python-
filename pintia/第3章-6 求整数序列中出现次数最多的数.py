def f(nums):
    nums.sort(key=lambda x:nums.count(x),reverse=True)
    return nums[0],nums.count(nums[0])
if __name__=="__main__":
    char,count=f([1,2,4,5,1,2,5,41,2,5,64,1])
    print(char,count)