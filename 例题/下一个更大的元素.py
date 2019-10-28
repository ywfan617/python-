"""
给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。

示例 1:

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
示例 2:

输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于num1中的数字2，第二个数组中的下一个较大数字是3。
    对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。
注意:

nums1和nums2中所有元素是唯一的。
nums1和nums2 的数组大小都不超过1000。
"""
#穷举法
def next_max1(nums1,nums2):
    res = list()
    for i in range(len(nums1)):
        index = nums2.index(nums1[i])
        flag = 0
        while index + 1 != len(nums2):
            if nums2[index + 1] > nums1[i]:
                res.append(nums2[index + 1])
                flag = 1
                break
            index += 1
        if flag == 0:
            res.append(-1)
    return res
"""栈①如果当前栈顶元素比 nums2[i] 小，栈顶出栈，重复①到栈顶比 nums2[i] 大或者栈为空。
②nums2[i] 入栈。
因为每一个元素只经历了入栈和出栈的操作，所以总复杂度为N
"""
def next_max2(nums1,nums2):
    stack=list()#建立一个空栈
    dict1=dict()#建立一个哈希表
    res=list()
    len2=len(nums2)
    len1=len(nums1)
    for i in range(len2):
        while (len(stack)!=0 and nums2[i]>stack[len(stack)-1]):
            dict1[stack.pop()]=nums2[i]
        stack.append(nums2[i])#元素进栈
    for j in nums1:
        if j in dict1.keys():
            res.append(dict1[j])
        else:
                res.append(-1)
    return res
res=next_max2([6,3,7],[6,3,7,4])
print(res)