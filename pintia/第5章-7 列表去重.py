def remove_repeat(nums):
    i=0
    while i<len(nums):
        j=i+1
        while j<len(nums):
            if nums[i]==nums[j]:
                nums.pop(j)
            j+=1
        i+=1
if __name__=="__main__":
    nums=[4,7,5,6,8,6,9,5]
    print(nums)
    remove_repeat(nums)
    print(nums)