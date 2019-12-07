from queue import SimpleQueue as Queue

class BinaryTree:
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
            self.tree_insert(arg)
            
    def tree_insert(self, key):
        if self._root == None:
            self._root = BinaryTree.BinaryNode(key)
            return self._root

        q = Queue()
        q.put(self._root)
        
        while not q.empty():
            cur_node = q.get()

            if cur_node.left == None:
                cur_node.left = BinaryTree.BinaryNode(key, cur_node)
                return cur_node.left
            elif cur_node.right == None:
                cur_node.right = BinaryTree.BinaryNode(key, cur_node)
                return cur_node.right

            if cur_node.left:
                q.put(cur_node.left)

            if cur_node.right:
                q.put(cur_node.right)

        return None
    
    def tree_delete(self, node):
        if not self._root:
            return None

        last_leaf_key = self._del_last_leaf()

        q = Queue()
        q.put(self._root)

        while not q.empty():
            cur_node = q.get()

            if node == cur_node:
                cur_node.key = last_leaf_key
                return

            if cur_node.left:
                q.put(cur_node.left)

            if cur_node.right:
                q.put(cur_node.right)

    def tree_search_bykey(self, key):
        if not self._root:
            return None

        nodes = []
        q = Queue()
        q.put(self._root)

        while not q.empty():
            cur_node = q.get()

            if cur_node.key == key:
                nodes.append(cur_node)

            if cur_node.left:
                q.put(cur_node.left)

            if cur_node.right:
                q.put(cur_node.right)

        return nodes

    def _del_last_leaf(self):
        if not self._root:
            return None

        parent = None
        node = self._root

        while node.left or node.right:
            parent = node
            if node.right:
                node = node.right
            elif node.left:
                node = node.left
        
        if parent:
            if parent.right:
                parent.right = None
            else:
                parent.left = None
            return node.key

    def root(self):
        return self._root

    def is_leaf(self, node):
        return not node.left and not node.right

    def is_root(self, node):
        return node == self._root
    
    def arity(self, node):
        if node.left and node.right:
            return 2
        
        if not node.left and node.right or node.left and not node.right:
            return 1

        return 0

    def leaves(self):
        if not self._root:
            return 0

        q = Queue()
        q.put(self._root)
        leaves_cnt = 0

        while not q.empty():
            cur = q.get()

            if self.arity(cur) == 0:
                leaves_cnt += 1

            if cur.left:
                q.put(cur.left)

            if cur.right:
                q.put(cur.right)

        return leaves_cnt
    
    def __len__(self):
        if not self._root:
            return 0

        q = Queue()
        q.put(self._root)

        nnodes = 0

        while not q.empty():
            cur = q.get()

            if cur.left:
                q.put(cur.left)
            
            if cur.right:
                q.put(cur.right)

            nnodes += 1

        return nnodes

    def __str__(self):
        if self._root and not self._root.left and not self._root.right:
            return "({})".format(self._root.key)

        s = ""
        q = Queue()
        q.put(self._root)

        while not q.empty():
            cur = q.get()

            if cur.left:
                s += "({}, {})".format(cur.key, cur.left.key)
                q.put(cur.left)
                
            if cur.right:
                s += "({}, {})".format(cur.key, cur.right.key)
                q.put(cur.right)

        return s
