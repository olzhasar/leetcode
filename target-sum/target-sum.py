import functools


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)

        @functools.cache
        def num_ways(start, target):
            nonlocal length

            if start == length - 1:
                if abs(target) == abs(nums[start]):
                    if target == 0:
                        return 2
                    return 1
                return 0

            return num_ways(start + 1, target + nums[start]) + num_ways(start + 1, target - nums[start])

        return num_ways(0, target)