import random


class RandomizedSet:
    def __init__(self):
        self.values = []
        self.indexes = {}
        self.k = 0
        
    def insert(self, val: int) -> bool:
        exists = val in self.indexes
        if not exists:
            self.values.append(val)
            self.indexes[val] = self.k
            self.k += 1
        return not exists

    def remove(self, val: int) -> bool:
        exists = val in self.indexes
        if exists:
            self.indexes[self.values[-1]] = self.indexes[val]
            self.values[self.indexes[val]] = self.values[-1]
            del self.indexes[val]
            self.values.pop()
            self.k -= 1
        return exists
        
    def getRandom(self) -> int:
        return random.choice(self.values)
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()