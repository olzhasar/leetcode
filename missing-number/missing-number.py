class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = 0
        for i, n in enumerate(nums):
            num = num ^ n ^ (i + 1)
        return num