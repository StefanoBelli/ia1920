from collections.abc import Collection
from ctypes import py_object as PyObject

class Queue(Collection):
    def __init__(self, m):
        self._array = (PyObject * m)()
        self._max = m
        self._write = 0

    def enqueue(self, elem):
        if self._write == self._max:
            return False

        self._array[self._write] = elem
        self._write += 1
        
        return True

    def dequeue(self):
        if self._write == 0:
            return None

        elem = self._array[0]
        self._write -= 1

        for i in range(self._write):
            self._array[i] = self._array[i+1]

        return elem

    def __len__(self):
        return self._write
    
    def __contains__(self, elem):
        return elem in self._array

    def __iter__(self):
        self._it = 0
        return self

    def __next__(self):
        if self._it == self._write:
            raise StopIteration

        e = self._array[self._it]
        self._it += 1
        return e
