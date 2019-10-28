def f1(nums1,nums2):
    set1=set(nums1)
    print(set1)
    set2=set(nums2)
    print(set2)
    res=set1^set2
    return res
def remove_repeat(nums):
    i=0
    while i<len(nums):
        j=i+1
        while j<len(nums):
            if nums[j]==nums[i]:
                nums.pop(j)
            else:
                j+=1
        i+=1
def f2(nums1,nums2):
    remove_repeat(nums1)
    remove_repeat(nums2)
    for i in nums1:
        if i not in nums2:
            print(i,end=" ")
    for j in nums2:
        if j not in nums1:
            print(j,end=" ")
if __name__=="__main__":
    nums1=[3,-5,2,8,0,3,5,-15,9,100]
    nums2=[6,4,8,2,6,-5,9,0,100,8,1]
    f2(nums1,nums2)