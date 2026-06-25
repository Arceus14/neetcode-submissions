class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) > 2:
            l = prices[0]
            r = prices[1]
            max_profit = 0
            for i in range(len(prices)-2):
                profit = r - l
                if profit <= 0:
                    l = prices[i+1]
                    r = prices[i+2]
                else:
                    r = prices[i+2]
                max_profit = max(r - l, profit, max_profit)
            return max_profit
        elif len(prices) == 2:
            return max(0, prices[1] - prices[0])
        else:
            return 0

