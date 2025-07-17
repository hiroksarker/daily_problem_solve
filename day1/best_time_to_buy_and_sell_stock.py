# Find the maximum profit from buying and selling a stock once.
# Time complexity: O(n)
# Space complexity: O(1)

def max_profit(prices):
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    
    return max_profit

# What if we can make multiple transactions? A: Buy and sell whenever profitable:
def max_profit_multiple(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit

# What if we can only make k transactions?A: Use dynamic programming with buy/sell states:

def max_profit_k_transactions(prices, k):
    if k >= len(prices) // 2:
        return max_profit_multiple(prices)
    
    buy = [-prices[0]] * (k + 1)
    sell = [0] * (k + 1)
    
    for price in prices[1:]:
        for j in range(k, 0, -1):
            sell[j] = max(sell[j], buy[j] + price)
            buy[j] = max(buy[j], sell[j-1] - price)
    
    return sell[k]

# Example usage:
if __name__ == "__main__":
    stock_prices = [7, 1, 5, 3, 6, 4]
    print("Maximum profit:", max_profit(stock_prices))  # Output: Maximum profit: 5
    stock_prices = [7, 6, 4, 3, 1]
    print("Maximum profit:", max_profit(stock_prices))  # Output: Maximum profit: 0
    stock_prices = [1, 2, 3, 4, 5]
    print("Maximum profit:", max_profit_multiple(stock_prices))  # Output: Maximum profit: 4    
    stock_prices = [7, 6, 4, 3, 1]
    print("Maximum profit:", max_profit(stock_prices))  # Output: Maximum profit: 0
    stock_prices = [3, 2, 6, 5, 0, 3]
    k = 2
    print("Maximum profit:", max_profit_k_transactions(stock_prices, k))  # Output: Maximum profit: 7       