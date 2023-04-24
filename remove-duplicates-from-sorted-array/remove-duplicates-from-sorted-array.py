class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        prev = nums[0]
        for n in nums[1:]:
            if n != prev:
                nums[k] = n
                k += 1
            prev = n

        return k