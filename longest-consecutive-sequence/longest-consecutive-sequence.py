class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        elements = set(nums)
        longest = 1

        for n in nums:
            if n - 1 in elements:
                continue

            current_length = 1
            i = n
            while True:
                if i + 1 in elements:
                    current_length += 1
                    longest = max(longest, current_length)
                    i += 1
                else:
                    break

        return longest