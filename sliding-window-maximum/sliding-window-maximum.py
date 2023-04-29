from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()

        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

        result = [nums[queue[0]]]

        for i in range(k, len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            if queue and queue[0] <= i - k:
                queue.popleft()

            queue.append(i)
            result.append(nums[queue[0]])

        return result