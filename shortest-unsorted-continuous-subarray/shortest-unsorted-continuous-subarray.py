class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_copy = sorted(nums)

        left = -1
        right = 0

        for i, n in enumerate(nums):
            if n != nums_copy[i]:
                if left == -1:
                    left = i
                right = i

        if left == -1:
            return 0
        return right - left + 1