from collections import deque
import threading


class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._size = 0
        self.queue = deque()
        self.cv = threading.Condition()
        
    def enqueue(self, element: int) -> None:
        with self.cv:
            self.cv.wait_for(lambda: self._size < self._capacity)
            self.queue.appendleft(element)
            self._size += 1
            self.cv.notify()

    def dequeue(self) -> int:
        with self.cv:
            self.cv.wait_for(lambda: self._size > 0)
            val = self.queue.pop()
            self._size -= 1
            self.cv.notify()
            return val
        
    def size(self) -> int:
        return self._size