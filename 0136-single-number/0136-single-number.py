

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        for i, n in count.items():
            if n ==1:
                return i
        
        
        print(count)
            

            
            
        