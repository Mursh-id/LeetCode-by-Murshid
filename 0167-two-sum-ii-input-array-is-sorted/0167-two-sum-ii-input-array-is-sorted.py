class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        pl = 0
        pr = len(numbers)-1
        res = []
        
        while pl < pr:
            if numbers[pl] + numbers[pr] ==target :
                return [pl+1,pr+1]
            
            elif numbers[pl] + numbers[pr] < target :
                pl +=1
                
            else:
                pr-=1
        