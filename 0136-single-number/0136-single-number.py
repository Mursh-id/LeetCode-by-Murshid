class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        data = {}
        
        for i in range(len(nums)):
            if nums[i] in data:
                data[nums[i]] = data[nums[i]]+1
            else:
                data[nums[i]] = 1
                
        print(data)
        for key, value in data.items():
            if value == 1:
                return key

            
            
        