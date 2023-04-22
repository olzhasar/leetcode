class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)

        good_index = length - 1

        for i in range(length - 2, -1, -1):
            if i + nums[i] >= good_index:
                good_index = i

        return good_index == 0
