import bt
import set

b1 = bt.BinaryTree(1,2,3)
A = set.Set(b1)
set.make_set(A)

b2 = bt.BinaryTree(4,5,6)
B = set.Set(b2)
set.make_set(B)

set.union(A, B)