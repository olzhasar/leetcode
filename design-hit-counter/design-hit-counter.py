from collections import deque


class HitCounter:
    def __init__(self):
        self.store = deque()

    def hit(self, timestamp: int) -> None:
        if self.store and self.store[-1][0] == timestamp:
            self.store[-1] = (timestamp, self.store[-1][1] + 1)
        else:
            self.store.append((timestamp, 1))

    def getHits(self, timestamp: int) -> int:
        print(self.store)

        while self.store and self.store[0][0] <= timestamp - 300:
            self.store.popleft()

        return sum(val[1] for val in self.store)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)