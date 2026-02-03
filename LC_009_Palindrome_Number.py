class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num = x
        d = 0
        while num>0:
            n = num %10
            d = d*10 + n
            num = num//10
        if x == d:
            return True
        else: 
            return False