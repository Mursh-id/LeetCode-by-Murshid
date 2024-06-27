class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max_wealth = 0  # Use a different name to avoid shadowing the built-in max function

        for account in accounts:
            wealth = sum(account)
            if wealth > max_wealth:
                max_wealth = wealth

        return max_wealth
            
        