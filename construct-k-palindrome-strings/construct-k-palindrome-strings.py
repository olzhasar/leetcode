class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        counter = Counter(s)
        
        min_items = 0
        max_items = 0
        
        for value in counter.values():
            if value % 2 == 1:
                min_items += 1
            max_items += value
                
        return min_items <= k <= max_items