def findContentChildren1(g, s):
    j=0
    g.sort()
    s.sort()
    count=len(g)
    # 以饼干为中心视角，看饼干能否满足小朋友
    for i in s:
        if j>=count:
            break
        if i>=g[j]:
            j+=1
    return j

def findContentChildren2(g,s) :
    g.sort()
    s.sort()
    gi = 0
    si = 0
    while gi < len(g) and si < len(s):
        if s[si] >= g[gi]:
            si += 1
            gi += 1
        else:
            si += 1
    return g
def findContentChildren3(g, s):
    j=0
    g.sort()
    s.sort()
    count=len(s)
    # 以小朋友为中心视角，看小朋友能否吃到饼干
    for i in g:
        flag=0
        while j<count :
            if s[j]>=i:
                flag=1
                j+=1
                break
            j+=1
        if flag==0:
            return False
    return True



res=findContentChildren3([1,2], [1,2,3])
print(res)
