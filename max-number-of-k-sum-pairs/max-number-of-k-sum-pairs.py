from collections import defaultdict


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0
        r = len(nums) - 1

        count = 0

        while l < r:
            s = nums[l] + nums[r]

            if s == k:
                count += 1
                l += 1
                r -= 1
            elif s > k:
                r -= 1
            else:
                l += 1

        return count