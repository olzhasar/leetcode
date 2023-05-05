from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = Counter(arr).values()
        existing = set()

        for val in occurences:
            if val in existing:
                return False
            existing.add(val)

        return True