class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        try:
            nums=list(set(nums))
            nums.sort()
            return nums[-3]
        except:
            return max(nums)