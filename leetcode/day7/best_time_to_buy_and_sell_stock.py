# Iterating through the prices, keeping track of the minimum buying price, 
# and updating the profit whenever a higher selling price is encountered.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest = float('inf')  # Initialize lowest to infinity
        profit = 0

        for price in prices:
            if price < lowest:
                lowest = price  # Update lowest price
            elif price - lowest > profit:
                profit = price - lowest  # Update maximum profit
        
        return profit
        