# Last updated: 8/15/2026, 3:05:32 PM
class Solution:
    def finalPrices(self, prices):
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    prices[i]=prices[i]-prices[j]
                    break
        return prices

        