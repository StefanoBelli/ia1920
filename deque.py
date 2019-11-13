from linked_list import LinkedList
from collections.abc import Collection

class Deque(Collection):
    def __init__(self):
        self._data = LinkedList()

    def tail(self, elem):
        self._data.append(elem)

    def head(self, elem):
        self._data.insert(0, elem)

    def tailRemove(self):
        del self._data[len(self) - 1]

    def headRemove(self):
        del self._data[0]

    def __contains__(self, elem):
        return elem in self._data

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        self._itcnt = 0
        return self

    def __next__(self):
        if self._itcnt == len(self):
            raise StopIteration

        elem = self._data[self._itcnt]

        self._itcnt += 1

        return elem

    def __getitem__(self, idx):
        return self._data[idx]

