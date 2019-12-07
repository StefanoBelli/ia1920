from bt import BinaryTree

class BinaryMaxHeap:
    def __init__(self, *args):
        self._tree = BinaryTree()

        for arg in args:
            self.heap_insert(arg)

    def heap_insert(self, key):
        in_node = self._tree.tree_insert(key)

        while in_node.parent and in_node.parent.key < in_node.key:
            tmpkey = in_node.parent.key
            in_node.parent.key = in_node.key
            in_node.key = tmpkey
            in_node = in_node.parent

        return in_node

    def heap_delete(self):
        rootnode = self._tree.root()
        ret = rootnode.key
        self._tree.tree_delete(rootnode)
        self._heapify(rootnode)
        return ret

    def _heapify(self, node):
        l = node.left
        r = node.right
        largest = node

        if l and l.key > node.key:
            largest = l

        if r and r.key > largest.key:
            largest = r

        if largest != node:
            tmpkey = largest.key
            largest.key = node.key
            node.key = tmpkey
            self._heapify(largest)

    def __str__(self):
        return self._tree.__str__()

