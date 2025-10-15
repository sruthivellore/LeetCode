def bestTime(prices):
    profit = 0
    buy = prices[0]

    for p in prices:
        print(p)
        buy = min(buy, p)
        print(buy)
        profit = max(profit, p - buy)
        print(profit, p-buy)
    
    return profit

print(bestTime([1,3,5,2,12,6]))