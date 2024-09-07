class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        sum_of_n = n*(n+1) // 2
        
        diff = sum_of_n
        
        for i in nums:
            diff = diff - i
            
        
        return diff
        
        
        