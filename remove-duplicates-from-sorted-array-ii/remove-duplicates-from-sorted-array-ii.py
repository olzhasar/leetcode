class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        k = 1
        prev = nums[0]
        for n in nums[1:]:
            if n == prev:
                counter += 1
            else:
                counter = 1
            if counter <= 2:
                nums[k] = n
                k += 1
            prev = n

        return k