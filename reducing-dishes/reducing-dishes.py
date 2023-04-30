class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        max_possible = float("-inf")

        for start in range(len(satisfaction)):
            current = 0
            for i, s in enumerate(satisfaction[start:]):
                current += (i + 1) * s
            if current < max_possible:
                break
            max_possible = current

        return max(max_possible, 0)