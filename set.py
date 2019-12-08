class _SetNode:
	def __init__(self, elem, parent, rank):
		self._elem = elem
		self._parent = parent
		self._rank = rank

	@property
	def parent(self):
		return self._parent

	@property
	def rank(self):
		return self._rank

	@property
	def elem(self):
		return self._elem

	@parent.setter
	def parent(self, v):
		self._parent = v

	@rank.setter
	def rank(self, v):
		self._rank = v

	@elem.setter
	def elem(self, v):
		self._elem = v

def make_set(elem) -> _SetNode:
	s = _SetNode(elem, None, 0)
	s.parent = s

	return s

def union(x, y) -> _SetNode:
	link(x, y)

def link(x, y) -> _SetNode:
	if x.rank > y.rank:
		x.parent = y.parent
	else:
		y.parent = x.parent

		if x.rank == y.rank:
			y.rank += 1