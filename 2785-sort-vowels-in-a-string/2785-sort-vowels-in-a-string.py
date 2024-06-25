class Solution:
    def sortVowels(self, s: str) -> str:
        
        vowel = "AEIOUaeiou"
        
        vowel_list =[]
        index_list = []
        
        for i in range(len(s)):
            if s[i] in vowel:
                vowel_list.append(s[i])
                index_list.append(i)
        vowel_list.sort()
        
        result = list(s)
        
        for i in range(len(index_list)):
            result[index_list[i]] =  vowel_list[i]
            
        print(result)    
        
        print(vowel_list,index_list)
        
        return ''.join(result)
                
                
            
        