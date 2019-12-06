class BinarySearchTree:
    class BinaryNode:
        def __init__(self, key, parent=None, left=None, right=None):
            self._right = right
            self._left = left
            self._key = key
            self._parent = parent

        @property
        def parent(self):
            return self._parent

        @property
        def right(self):
            return self._right

        @property
        def left(self):
            return self._left

        @property
        def key(self):
            return self._key

        @right.setter
        def right(self, v):
            self._right = v

        @left.setter
        def left(self, v):
            self._left = v

        @key.setter
        def key(self, v):
            self._key = v

        @parent.setter
        def parent(self, v):
            self._parent = v

    def __init__(self, *args):
        self._root = None

        for arg in args:
            self.insert(arg)

    def insert(self, key):
        if not self._root:
            self._root = BinarySearchTree.BinaryNode(key)
        else:
            cur = self._root
            nxt = cur
            while nxt:
                cur = nxt
                if key < cur.key:
                    nxt = cur.left
                else:
                    nxt = cur.right
            
            if key < cur.key:
                cur.left = BinarySearchTree.BinaryNode(key, cur)
            else:
                cur.right = BinarySearchTree.BinaryNode(key, cur)

    def search(self, key):
        node = self._node_lookup(key)
        if node:
            return node.key

        return None

    def min(self):
        return self._min(self._root)

    def max(self):
        return self._max(self._root)

    def successor(self, key):
        target = self._node_lookup(key)
        
        if not target:
            return None

        if target.right:
            return self._min(target.right)
        
        parent = target.parent
        while parent and target == parent.right:
            parent = parent.parent

        return parent.key

    def predecessor(self, key):
        target = self._node_lookup(key)

        if not target:
            return None

        if target.left:
            return self._max(target.left)
        
        parent = target.parent
        while parent and target == parent.left:
            parent = parent.parent

        return parent.key

    def _min(self, from_node):
        cur = from_node
        while cur.left:
            cur = cur.left

        return cur.key

    def _max(self, from_node):
        cur = from_node
        while cur.right:
            cur = cur.right

        return cur.key

    def _node_lookup(self, key):
        cur = self._root
        while cur:
            if key == cur.key:
                return cur

            if key < cur.key:
                cur = cur.left
            else:
                cur = cur.right

        return None
        
bst = BinarySearchTree(5,3,4,1,2)

bst.delete(3)
print(bst.search(3))