class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)

        max_left = [0] * l
        max_right = [0] * l

        res = 0

        for i in range(1, l):
            max_left[i] = max(max_left[i - 1], height[i - 1])
            max_right[-1 - i] = max(max_right[-i], height[-i])

        for i in range(1, l - 1):
            val = min(max_left[i], max_right[i]) - height[i]
            if val > 0:
                res += val

        return res