def maxProfit(prices):
    n=len(prices)
    profit=0
    for i in range(1,n):
        if prices[i]>prices[i-1]:
            profit+=prices[i]-prices[i-1]
    return profit
res=maxProfit([7,6,4,3,1])
print(res)