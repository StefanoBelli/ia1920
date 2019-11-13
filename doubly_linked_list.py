from collections.abc import MutableSequence

class DoublyLinkedList(MutableSequence):
    class Node:
        def __init__(self, value, prev, next):
            self._value = value
            self._prev = prev
            self._next = next

        @property
        def next(self):
            return self._next

        @property
        def prev(self):
            return self._prev

        @property
        def value(self):
            return self._value

        @next.setter
        def next(self, v):
            self._next = v

        @prev.setter
        def prev(self, v):
            self._prev = v

        @value.setter
        def value(self, v):
            self._value = v

    def __init__(self, *args):
        self._head = self._tail = None

        for arg in args:
            self.append(arg)

    def __delitem__(self, idx):
        if idx == 0:
            self._head = self._head.next
            self._head.prev = None
        else:
            cur = self._head
            for _ in range(idx):
                cur = cur.next

            cur.prev.next = cur.next

            if cur.next != None:
                cur.next.prev = cur.prev

    def __setitem__(self, idx, value):
        cur = self._head
        for _ in range(idx):
            cur = cur.next

        cur.value = value

    def __getitem__(self, idx):
        cur = self._head
        for _ in range(idx):
            cur = cur.next

        return cur.value

    def __len__(self):
        current = self._head
        l = 0

        while current:
            l += 1
            current = current.next

        return l

    def insert(self, idx, value):
        if idx == 0:
            self.appendHead(value)
        elif idx == len(self):
            self.append(value)
        else:
            new_node = DoublyLinkedList.Node(value, None, None)

            cur = self._head
            for _ in range(idx):
                cur = cur.next

            new_node.next = cur
            new_node.prev = cur.prev
            cur = new_node

            new_node.prev.next = cur
            new_node.next.prev = cur

    def append(self, value):
        new_node = DoublyLinkedList.Node(value, None, None)

        if self._head == None and self._tail == None:
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
            
    def appendHead(self, value):
        new_node = DoublyLinkedList.Node(value, None, None)

        if self._head == None and self._tail == None:
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
            self._head.next.prev = self._head
            self._head.prev = None
