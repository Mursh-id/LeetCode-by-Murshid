class Solution:
    def sortVowels(self, s: str) -> str:
        vowel = "AEIOUaeiou" #to check for vowels in s
        vowel_list =[]  # to store the vowels
        index_list = []  # to store the index of vowels
        
        for i in range(len(s)):  # extracting all the vowels and their indexes
            if s[i] in vowel:
                vowel_list.append(s[i])
                index_list.append(i)
        vowel_list.sort()   # sort the vowel list 
        
        result = list(s) # convert the input string to list and store in variable
        
        for i in range(len(index_list)):
            result[index_list[i]] =  vowel_list[i]  # replace the 
            
        print(result)    
        print(vowel_list,index_list)
        
        return ''.join(result)
                
                
            
        