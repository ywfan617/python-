def f():
    nums={}
    inputnums=eval(input())
    target=int(input())
    n=len(inputnums)
    for i in range(n):
        if inputnums[i] in nums:
            nums[inputnums[i]].append(i)
        else:
            nums[inputnums[i]]=[i]
    print(nums)
    for i in nums:
        remainder=target-i
        if remainder in nums:
            if remainder!=i:
                return nums[i][0],nums[remainder][0]
            else:
                count=len(nums[i])
                if count>1:
                    return nums[i][0],nums[i][1]
    return None
if __name__=="__main__":
    res=f()
    if res==None:
        print("no answer")
    else:
        print(res[0],res[1])
