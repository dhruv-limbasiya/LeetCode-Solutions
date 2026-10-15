class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy_price = prices[0]

        for i in range(len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                curent_profit = prices[i] - buy_price
                profit = max(profit, curent_profit)

        return profit        