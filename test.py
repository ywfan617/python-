def plusOne(digits):
    lens=len(digits)
    digit=0
    count=0
    for i in range(lens-1,-1,-1):
        digit+=10**count*digits[i]
        count+=1
    digit+=1
    plusnums=[int(i) for i in str(digit)]
    return plusnums
res=plusOne([9,9,9])
print(res)