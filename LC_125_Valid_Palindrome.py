class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        s=s.lower()
        for i in s:
            if i.isalnum():
                word+=i
        if word==word[::-1]:
            return True
        else:
            return False
