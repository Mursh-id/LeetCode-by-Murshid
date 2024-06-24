class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ""
        for i in s:
            if i.isalnum():
                k+=i.lower()
        print(k)
        return k == k[::-1]
        