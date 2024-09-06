class Solution:
    def jump(self, nums: List[int]) -> int:
        
        total_jumps = 0
        destination = len(nums)-1  # the destination to reach
        coverage = 0               #this is how far i can go
        last_jump_index = 0        # this is where i could go
        
        if len(nums) == 1:
            return 0
        
        for i in range(len(nums)):
            coverage = max(coverage, nums[i]+i)
            
            
            
            if i == last_jump_index:
                total_jumps+=1
                last_jump_index = coverage
                
                if coverage>=destination:
                    return total_jumps
                
            
                
                
        # return total_jumps
                
        