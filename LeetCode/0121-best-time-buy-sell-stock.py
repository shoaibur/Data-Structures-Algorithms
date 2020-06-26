def maxProfit(prices):
    if len(prices) <= 1: return 0
    min_price = prices[0]
    max_profit = 0
    for curr_price in prices[1:]:
        curr_profit = curr_price - min_price
        max_profit = max(max_profit, curr_profit)
        min_price = min(min_price, curr_price)
    return max_profit
