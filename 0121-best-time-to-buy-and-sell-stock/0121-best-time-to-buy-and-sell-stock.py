class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        buy_price = prices[0]

        for i in range(len(prices)):
            current_price = prices[i]

            if current_price < buy_price:
                buy_price = current_price 
            else:
                profit = current_price - buy_price
                max_profit = max(max_profit, profit)

        return max_profit        