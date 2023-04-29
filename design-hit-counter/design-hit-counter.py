from collections import defaultdict


class HitCounter:

    def __init__(self):
        self.store = defaultdict(lambda: 0)

    def hit(self, timestamp: int) -> None:
        self.store[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        start = timestamp - 299
        
        count = 0
        for i in range(start, timestamp + 1):
            count += self.store[i]

        return count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)