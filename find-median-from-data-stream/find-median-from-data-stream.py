import bisect


class MedianFinder:
    def __init__(self):
        self.values = []
        self.n = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.values, num)
        self.n += 1

    def findMedian(self) -> float:
        if self.n % 2 == 1:
            return self.values[self.n // 2]
        return (self.values[self.n // 2 - 1] + self.values[self.n // 2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()