from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = sorted(Counter(arr).values())

        for i in range(1, len(occurences)):
            if occurences[i] == occurences[i - 1]:
                return False

        return True