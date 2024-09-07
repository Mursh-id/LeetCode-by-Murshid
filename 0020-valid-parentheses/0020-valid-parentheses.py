class Solution:
    def isValid(self, s: str) -> bool:
        
        data = {
            "(" : ")",
            "{":"}",
            "[" : "]",
        }
        
        stack = []
        
        for i in s:
            if i in data:
                stack.append(data[i])
            elif stack and stack[-1] == i:
                stack.pop()
            else:
                return False
                
                
                
                
        return len(stack) == 0
            
        