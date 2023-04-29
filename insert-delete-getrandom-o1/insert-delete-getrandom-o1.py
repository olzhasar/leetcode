import random


class RandomizedSet:

    def __init__(self):
        self.store = set()
        

    def insert(self, val: int) -> bool:
        exists = val in self.store
        if not exists:
            self.store.add(val)
        return not exists

    def remove(self, val: int) -> bool:
        exists = val in self.store
        if exists:
            self.store.remove(val)
        return exists
        
    def getRandom(self) -> int:
        return random.choice(list(self.store))
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()