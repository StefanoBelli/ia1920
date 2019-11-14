from collections.abc import MutableSequence

class CircularLinkedList(MutableSequence):
    class Node:
        def __init__(self, val, nxt):
            self._val = val
            self._next = nxt

        @property
        def value(self):
            return self._val

        @property
        def next(self):
            return self._next

        @value.setter
        def value(self, v):
            self._val = v

        @next.setter
        def next(self, n):
            self._next = n


    def __init__(self, *args):
        self._head = self._tail = None

        for arg in args:
            self.append(arg)

    def __getitem__(self, idx):
        cur = self._head
        for _ in range(idx):
            cur = cur.next

        return cur.value

    def __delitem__(self, idx):
        if idx == 0 and len(self) == 1:
            self._tail = self._head = None
        elif idx == 0:
            self._head = self._head.next
            self._tail.next = self._head
        else:
            cur = self._head
            for _ in range(idx - 1):
                cur = cur.next

            cur.next = cur.next.next
        
    def __setitem__(self, idx, v):
        cur = self._head
        for _ in range(idx):
            cur = cur.next

        cur.value = v

    def __len__(self):
        if self._head == None and self._tail == None:
            return 0
        
        cur = self._head.next
        i = 1
        while cur != self._head:
            i += 1
            cur = cur.next

        return i

    def __iter__(self):
        self._cur = self._head
        self._final = False
        return self

    def __next__(self):
        if self._final:
            raise StopIteration

        if self._cur.next == self._head:
            self._final = True

        e = self._cur.value
        self._cur = self._cur.next

        return e

    def insert(self, idx, v):
        if idx == 0:
            self.appendHead(v)
        elif idx == len(self):
            self.append(v)
        else:
            cur = self._head
            for _ in range(idx - 1):
                cur = cur.next

            cur.next = CircularLinkedList.Node(v, cur.next)

    def append(self, v):
        if self._head == None and self._tail == None:
            self._head = CircularLinkedList.Node(v, None)
            self._tail = self._head
            self._tail.next = self._head
        else:
            new_node = CircularLinkedList.Node(v, self._head)
            self._tail.next = new_node
            self._tail = new_node

    def appendHead(self, v):
        if self._head == None and self._tail == None:
            self._head = CircularLinkedList.Node(v, None)
            self._tail = self._head
            self._tail.next = self._head
        else:
            self._head = CircularLinkedList.Node(v, self._head)
            self._tail.next = self._head
