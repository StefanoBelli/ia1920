import bt
import set
import hash_table
import random

b1 = bt.BinaryTree(1,2,3)
A = set.Set(b1)
set.make_set(A)

b2 = bt.BinaryTree(4,5,6)
B = set.Set(b2)
set.make_set(B)

set.union(A, B)

ht = hash_table.HashTable()

for i in range(12):
    ht[random.randint(0,65535)] = random.randint(1,10)


for kv in ht:
    print("{}:{}".format(kv[0], kv[1]))

print(len(ht))