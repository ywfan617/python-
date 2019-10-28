raw={}
des={}
count1=0
count2=0
for i in input():
    if i not in raw:
        raw[i]=1
    else:
        raw[i]+=1
for j in input():
    if j not in des:
        des[j]=1
    else:
        des[j]+=1
for m in des:
    if m in raw:
        raw[m]-=des[m]
    else:
        raw[m]=-des[m]
for n in raw:
    if raw[n]>=0:
        count1+=raw[n]
    else:
        count2+=raw[n]
if count2<0:
    print("No",-count2,end="")
else:
    print("Yes",count1,end="")

# 很重要：遍历数组的时候动态改变数组，不能用for语句，需要用while语句
# 法一：删想要的数组中的元素，最后结果是想要的数组的长度
# 法二：通过count计数想要数组中缺少的元素个数，输出count
def f():
    a = [i for i in input()]
    b = [i for i in input()]
    i = 0
    while i < len(b):
        if b[i] in a:
            a.remove(b[i])
            del b[i]
            i -= 1
        i += 1
    if len(b) == 0:
        print("%s %d" % ("Yes", len(a)), end="")
    else:
        print("%s %d" % ("No", len(b)), end="")
