class Solution:

    def __init__(self, w: List[int]):
        self.ranges = []
        self.l = 0
        
        prev = 0
        for weight in w:
            self.ranges.append((prev + 1, prev + weight))
            self.l += 1
            prev = prev + weight

    def pickIndex(self) -> int:
        val = random.randint(self.ranges[0][0], self.ranges[-1][1])
        
        l, r = 0, self.l - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if val < self.ranges[m][0]:
                r = m - 1
            elif val > self.ranges[m][1]:
                l = m + 1
            else:
                return m

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()