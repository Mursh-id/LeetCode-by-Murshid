class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        sum_of_n = n*(n+1) // 2
        
        sum_of_nums = sum(nums) 
        
        return sum_of_n - sum_of_nums
        
        
        