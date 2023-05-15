from collections import deque


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0, heights[0])]
        max_area = heights[0]

        for i in range(1, len(heights)):
            j = i

            while stack and stack[-1][1] > heights[i]:
                j, h = stack.pop()
                max_area = max(max_area, (i - j) * h)

            stack.append((j, heights[i]))

        l = len(heights)

        while stack:
            j, h = stack.pop()
            max_area = max(max_area, (l - j) * h)

        return max_area