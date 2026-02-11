class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        l=Counter(s)
        for i in l:
            if l[i]==1:
                return s.find(i)
        return -1