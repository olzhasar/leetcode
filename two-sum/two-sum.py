class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i, n in enumerate(nums):
            if n in sums:
                return [sums[n], i]
            sums[target - n] = i