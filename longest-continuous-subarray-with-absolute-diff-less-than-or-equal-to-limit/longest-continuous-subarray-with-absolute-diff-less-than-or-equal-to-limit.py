from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = deque()
        max_queue = deque()

        longest = 1
        l = r = 0

        while r < len(nums):
            while min_queue and nums[min_queue[-1]] > nums[r]:
                min_queue.pop()
            min_queue.append(r)

            while max_queue and nums[max_queue[-1]] < nums[r]:
                max_queue.pop()
            max_queue.append(r)

            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                l += 1
                if max_queue[0] < l:
                    max_queue.popleft()
                if min_queue[0] < l:
                    min_queue.popleft()

            longest = max(longest, r - l + 1)

            r += 1

        return longest