def dominantIndex(nums):
    maxval=max(nums)
    position=nums.index(maxval)
    nums.remove(maxval)
    for i in nums:
        if i*2>maxval:
            return -1
    return position
res=dominantIndex([3, 6, 1, 0])
print(res)
