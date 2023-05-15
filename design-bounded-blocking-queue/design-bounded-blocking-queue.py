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
            while self._capacity <= 0:
                self.cv.wait()
            self.queue.appendleft(element)
            self._capacity -= 1
            self.cv.notify_all()

    def dequeue(self) -> int:
        with self.cv:
            while not self.queue:
                self.cv.wait()
            val = self.queue.pop()
            self._capacity += 1
            self.cv.notify_all()
            
        return val
        
    def size(self) -> int:
        return len(self.queue)