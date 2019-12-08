class Set:
	def __init__(self, tree, rank = 0):
		self._repr_node = tree.root()
		self._rank = rank

	@property
	def rank(self):
		return self._rank

	@property
	def repr_node(self):
		return self._repr_node

	@rank.setter
	def rank(self, v):
		self._rank = v

	@repr_node.setter
	def repr_node(self, v):
		self._repr_node = v

def make_set(x):
	x.repr_node.parent = x.repr_node
	x.rank = 0

def union(x, y):
	link(x, y)

def link(x, y):
	if x.rank > y.rank:
		x.repr_node.parent = y.repr_node.parent
	else:
		y.repr_node.parent = x.repr_node.parent

		if x.rank == y.rank:
			y.rank += 1