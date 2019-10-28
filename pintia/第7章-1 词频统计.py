import re
def f(strs):
    index=strs.index("#")
    res=re.findall(r"\w{1,80}",strs[:index])
    word={}
    for i in res:
        if len(i)>15:
            i=i[:15]
        if i.lower() not in word:
            word[i.lower()]=1
        else:
            word[i.lower()]+=1
    key=sorted(word,key=lambda x:-word[x])
    length=len(key)
    print(length)
    count=length//10
    for i in range(count):
        print(word[key[i]],key[i])
if __name__ == '__main__':
    strs="""This is a test.
The word "this" is the word with the highest frequency.
Longlonglonglongword should be cut off, so is considered as the same as longlonglonglonee.  But this_8 is different than this, and this, and this...#
this line should be ignored."""
    f(strs)