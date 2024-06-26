

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = defaultdict(int)  
        
        # Count occurrences of each number
        for n in nums:
            res[n] += 1  
        
       
        print(res)  
        
        for i in res:
            if res[i] == 1:
                return i
            

            
            
        