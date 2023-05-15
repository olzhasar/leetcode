from collections import deque


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        i = 0

        while i < len(heights):
            j = i

            while stack and stack[-1][1] > heights[i]:
                j, h = stack.pop()
                max_area = max(max_area, (i - j) * h)

            stack.append((j, heights[i]))

            i += 1

        while stack:
            j, h = stack.pop()
            max_area = max(max_area, (i - j) * h)

        return max_area