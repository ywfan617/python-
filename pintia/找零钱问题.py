"""
[找零钱问题]假如老板要找给我99分钱，
他有上面的面值分别为25，10，5，1的硬币数，
为了找给我最少的硬币数，那么他是不是该这样找呢，
先看看该找多少个25分的，诶99／25＝3，好像是3个，要是4个的话，
我们还得再给老板一个1分的，我不干，那么老板只能给我3个25分的拉，由于还少给我24，
所以还得给我2个10分的和4个1分。
————————————————
"""
def charge(prices,counts,need):  # prices中为零钱的种类，need为需要找的零钱
    n=len(prices)
    countpart=list(zip(prices,counts))
    countpart.sort(key=lambda x:x[0],reverse=True)
    prices,counts=zip(*countpart)
    res=[]
    for i in range(n):
        count=need//prices[i]
        if count>counts[i]:
            count=counts[i]
        res.append(count)
        need=need-prices[i]*count
    return  res
if __name__=="__main__":
    res=charge([25, 10, 5, 1],[2,5,1,30],99)
    print(res)