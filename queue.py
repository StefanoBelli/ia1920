import ctypes

class Queue:
    def __init__(self, maxsize):
        self._array = (ctypes.py_object * maxsize)()
        self._max = maxsize
        self._read = 0
        self._write = 0

    def enqueue(self, elem):
        next_write = (self._write + 1) % self._max

        if self._read == next_write:
            return False

        self._array[self._write] = elem
        self._write = next_write
        return True


    def dequeue(self):
        if self._read == self._write:
            return None

        e = self._array[self._read]
        self._read = (self._read + 1) % self._max
        return e

q = Queue(3)

print(q.enqueue(3))
print(q.enqueue(4))
