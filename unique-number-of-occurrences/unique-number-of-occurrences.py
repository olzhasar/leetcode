from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = Counter(arr)
        existing = set()

        for val in occurences.values():
            if val in existing:
                return False
            existing.add(val)

        return True