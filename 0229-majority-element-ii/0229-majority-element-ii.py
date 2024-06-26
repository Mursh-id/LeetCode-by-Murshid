class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)/3
        count = Counter(nums)
        res = []
        
        for k,v in count.items():
            if v > n :
                res.append(k)
        
        
        
        print(res)
        
        return res
        