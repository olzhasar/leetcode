class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        longest = 0

        for n in nums:
            if n - 1 in elements:
                continue

            current_num = n
            current_length = 1
            while current_num + 1 in elements:
                current_num += 1
                current_length += 1
            longest = max(longest, current_length)

        return longest