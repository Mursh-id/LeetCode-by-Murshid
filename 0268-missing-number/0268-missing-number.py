class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        all_xor = 0
        
        for i in nums:
            all_xor = all_xor ^ i
            
        for i in range(1,len(nums)+1):
            all_xor = all_xor ^ i
            
            
            
        
        return all_xor
        
        
        