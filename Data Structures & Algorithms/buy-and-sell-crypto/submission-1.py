class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        ans = 0
        r = 1

        while r<len(prices):
            if prices[l] < prices[r]:
                curr_profit = prices[r] - prices[l]
                ans = max(ans, curr_profit)
            else:
                l = r
            r+=1
        
        return ans 