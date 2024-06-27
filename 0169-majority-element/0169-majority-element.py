from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        count = Counter(nums)
        
        majority_count = len(nums) // 2
        
        for k, v in count.items():
            if v > majority_count:
                return k

        