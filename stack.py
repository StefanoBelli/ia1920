from collections.abc import Collection

class Stack(Collection):
    def __init__(self):
        self._len = 0
        self._data = list()

    def push(self, elem):
        self._data.append(elem)
        self._len += 1

    def pop(self):
        self._len -= 1
        oldelem = self._data[self._len]

        del self._data[self._len]

        return oldelem

    def __getitem__(self, idx):
        return self._data[idx]

    def __contains__(self, elem):
        return elem in self._data

    def __len__(self):
        return self._len

    def __iter__(self):
        self._startiter = 0
        return self

    def __next__(self):
        if self._startiter == self._len:
            raise StopIteration

        elem = self._data[self._startiter]
        self._startiter += 1
        return elem
