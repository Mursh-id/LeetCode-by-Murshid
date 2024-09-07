class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy_price = prices[0]
        
        current_profit = 0
        max_profit = 0
        
        for i in prices:
            
            if i<buy_price:
                buy_price = i
            else:
                current_profit =  i - buy_price 
                max_profit = max(current_profit,max_profit)
                
        return max_profit
                
                
                
            
        