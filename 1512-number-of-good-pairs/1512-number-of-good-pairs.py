class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        counter = {}
        
        for i in nums:
            counter[i] = counter.get(i,0)+1
        print(counter)
        
        count = 0
        
        for i in counter.values():
            count += (i*(i-1))/2
            
        
        return int(count)