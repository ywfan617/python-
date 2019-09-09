
def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    d = {}
    print(d.items())
    for i, item in enumerate(nums):
        tmp = target - item
        for key, value in d.items():
            print(d.items())
            print(value)
            print(key)
            # if value == tmp:
            #     return [key, i]
        d[i] = item

print(twoSum([2,7],9))
d={}
for i,j in d.items():
    print(i,j)