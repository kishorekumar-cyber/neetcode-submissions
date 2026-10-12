class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        l,r = 0,1
        maxf =0
        while r< len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxf = max(profit,maxf)
            else:
                l=r
            r+=1

        return maxf
                

        