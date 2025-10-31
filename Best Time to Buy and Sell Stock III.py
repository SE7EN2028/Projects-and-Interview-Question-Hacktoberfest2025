def maxProfit(prices):
    profit = 0
    memo = {}

    def helper(i,buy,c):
        if (i>=len(prices) or c==2):
            return 0
        if (i,buy,c) in memo:
            return memo[(i,buy,c)]

        if buy:
            profit = max(-prices[i]+helper(i+1,not buy,c),helper(i+1,buy,c))
        else:
            profit = max(prices[i]+helper(i+1,not buy,c+1),helper(i+1,buy,c))
        memo[(i,buy,c)] = profit
        return profit
    return helper(0,True,0)
