from ctypes import py_object as PyObject

class Queue:
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
        for i in range(0, self._write - 1):
            self._array[i] = self._array[i+1]

        self._write -= 1
        return elem

    def __len__(self):
        return self._write
