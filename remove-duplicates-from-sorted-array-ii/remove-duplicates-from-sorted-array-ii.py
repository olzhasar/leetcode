class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        k = 1
        for i, n in enumerate(nums[1:]):
            if n == nums[i]:
                counter += 1
            else:
                counter = 1
            if counter <= 2:
                nums[k] = n
                k += 1
            prev = n

        return k