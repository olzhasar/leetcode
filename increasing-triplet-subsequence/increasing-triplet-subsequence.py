class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        mins, maxs = [float("inf")] * n, [float("-inf")] * n
        min_so_far, max_so_far = nums[0], nums[n - 1]

        for i in range(n):
            min_so_far = min(min_so_far, nums[i])
            mins[i] = min_so_far
            max_so_far = max(max_so_far, nums[n - 1 - i])
            maxs[n - 1 - i] = max_so_far

        for i in range(1, n - 1):
            if mins[i - 1] < nums[i] < maxs[i + 1]:
                return True

        return False