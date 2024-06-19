class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        
        hashS={}
        hashT={}
        for i in range (len(s)):
            hashS[s[i]] = i
            
        print(hashS)
        
        for i in range (len(t)):
            hashT[t[i]] = i
            
        print(hashT)
        
        sum = 0 ;
        
        for i in hashS:
            sum = sum+ abs(hashS[i]-hashT[i])
            
        print(sum)
        
        return sum
        