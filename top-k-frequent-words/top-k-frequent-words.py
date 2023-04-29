import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        heap = []

        for word, q in count.items():
            heapq.heappush(heap, (-q, word))

        return [heapq.heappop(heap)[1] for _ in range(k)]