class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxsum=sum(accounts[0])
        for i in range(len(accounts)):
            newsum=sum(accounts[i])
            if newsum>maxsum:
                maxsum=newsum
        return maxsum