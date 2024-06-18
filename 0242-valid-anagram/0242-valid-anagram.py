class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False
        
        countS = {}
        
        for i in s:
            countS[i] = countS.get(i,0)+1
            
        print(countS)
        
        for i in t:
            if i in countS:
                countS[i]= countS[i]-1
                if countS[i] < 0 :
                    return False
            else:
                return False
            
        return True
        