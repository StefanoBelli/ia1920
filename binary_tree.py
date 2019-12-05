import queue

class BinaryTree:
    class BinaryNode:
        def __init__(self, key, left=None, right=None):
            self._right = right
            self._left = left
            self._key = key

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

    def __init__(self, *args):
        self._root = None

        for arg in args:
            self.insert(args)
    
    def insert(self, elem):
        if self._root == None:
            self._root = BinaryTree.BinaryNode(elem)
        else:
            has_empty_child = self._bfs(None)
            if has_empty_child.left == None:
                has_empty_child.left = BinaryTree.BinaryNode(elem)
            elif has_empty_child.right == None:
                has_empty_child.right = BinaryTree.BinaryNode(elem)

    def root(self):
        return self._root

    def children(self, node):
        return [ node._left, node._right ]

    def is_leaf(self, node):
        return node.left == None and self.right == None

    def parent(self, node):
        return self._lookup(node)[0]
    
    def search(self, node):
        return self._lookup(node)[1]

    def _lookup(self, node):
        res = self._bfs(node)
        
        if not res:
            return None

        if res.left == node:
            return (res, res.left)
        
        return (res, res.right)

    def _bfs(self, node):
        q = queue.LifoQueue()
            
        cur = self._root
        q.put(cur)
        while not q.empty():
            cur = q.get()

            if cur.left == node or cur.right == node:
                return cur

            q.put(cur.left)
            q.put(cur.right)

        return None

BinaryTree(1,2,3,4,5,6,7)
