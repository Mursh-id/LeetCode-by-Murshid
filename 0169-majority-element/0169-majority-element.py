class Solution(object):
    def majorityElement(self, nums):
        count = Counter(nums)
        
        res = nums[0]
        
        for k,v in count.items():
            if v > len(nums)/2:
                res =k
    
        return res
        