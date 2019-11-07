from collections.abc import MutableSequence, Sequence, Set

def greater_than(a, b):
    return a > b

def greater_or_equal_than(a, b):
    return a >= b

class LinkedList(MutableSequence):
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

    @staticmethod
    def compat(container):
        return issubclass(type(container), Sequence) \
                or issubclass(type(container), Set)
            
    def __init__(self, *args):
        self._head = None
        self._tail = None
        self._len = 0

        if len(args) == 1 and LinkedList.compat(args[0]):
            args = args[0]
        
        for arg in args:
            self.append(arg)
            
    def __len__(self):
        return self._len

    def __delitem__(self, idx):
        self.__check_idx_raise_iffail(idx, greater_or_equal_than)

        if self._len == 0:
            return False

        if idx == 0:
            deleted = self._head
            self._head = self._head.next
            deleted.next = None
        else:
            cur = self._head
            for _ in range(idx - 1):
                cur = cur.next
            deleted = cur.next
            cur.next = cur.next.next
            deleted.next = None

        self._len -= 1
        return True

    def __getitem__(self, idx):
        self.__check_idx_raise_iffail(idx, greater_or_equal_than)

        if self._len == 0:
            raise IndexError("empty list")

        to = self._head
        for _ in range(idx):
            to = to.next

        return to.value

    def __setitem__(self, idx, value):
        self.__check_idx_raise_iffail(idx, greater_or_equal_than)

        if self._len == 0:
            raise IndexError("empty list")

        to = self._head
        for _ in range(idx):
            to = to.next

        to.value = value

    def insert(self, idx, value):
        self.__check_idx_raise_iffail(idx, greater_than)

        if self._len == 0:
            self.append(value)
            return

        new_node = LinkedList.Node(value, None)
        
        actual_head = self._head

        if idx >= 1:
            for _ in range(idx - 1):
                actual_head = actual_head.next

            oldnext = actual_head.next
            actual_head.next = new_node
            actual_head.next.next = oldnext
            
            if oldnext == None:
                self._tail = actual_head.next

        elif idx == 0:
            old = self._head
            self._head = new_node
            self._head.next = old

        self._len += 1

    def __str__(self):
        if self._len == 0:
            return "[]"
        
        s = "[ "
        cur = self._head
        while cur:
            s += "{}, ".format(cur.value)
            cur = cur.next
        s = s[:-2]
        s += " ]"

        return s

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        self.__itercurrent = self._head
        return self

    def __next__(self):
        if self.__itercurrent == None:
            raise StopIteration

        val = self.__itercurrent.value
        self.__itercurrent = self.__itercurrent.next
        return val

    # tail-append
    def append(self, value):
        new_node = LinkedList.Node(value, None)

        if self._len == 0:
            self._head = self._tail = new_node
        else:
            self._tail.next = self._tail = new_node

        self._len += 1

    def __check_idx_raise_iffail(self, idx, comparsion_cb):
        if idx < 0 or comparsion_cb(idx, self._len):
            raise IndexError("could not create [ idx = {}, len = {} ]".format(idx, self._len))
