class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price
            if price > min_price and price-min_price > diff:
                diff = price-min_price
        return diff
