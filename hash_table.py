from dynamic_array import DynamicArray
from collections.abc import MutableMapping
import random
import pickle

# sucks but thats it
def _find_next_odd_prime(start):
	for num in range(start + 1, (4 * start) + 1):
		if num > 2:
			prime = True
			for i in range(2, num):
				if (num % i) == 0:
					prime = False
					break
			if prime:
				return num

	return False

class HashTable(MutableMapping):
	class HashElement:
		def __init__(self):
			self._deleted = False
			self._nil = True
			self._key = None
			self._value = None

		@property
		def deleted(self):
			return self._deleted

		@property
		def nil(self):
			return self._nil

		@property
		def key(self):
			return self._key
		
		@property
		def value(self):
			return self._value

		@deleted.setter
		def deleted(self, v):
			self._deleted = v

		@nil.setter
		def nil(self, v):
			self._nil = v

		@key.setter
		def key(self, v):
			self._key = v
		
		@value.setter
		def value(self, v):
			self._value = v

	def __init__(self):
		self._size = 0
		self._busy = 0
		self._arr = None

		self._extend_table(13)

	def __delitem__(self, key):
		k = self._process_key(key)

		for i in range(self._size):
			hsh = self._H(k, i)
			isnil =  self._arr[hsh].nil
			wasdel = self._arr[hsh].deleted

			if isnil or wasdel:
				return True
			
			if not isnil and not wasdel and self._arr[hsh].key == key:
				self._arr[hsh].deleted = True
				self._arr[hsh].isnil = True
				self._arr[hsh].key = None
				self._arr[hsh].value = None
				self._busy -= 1
				return True

		return False


	def __getitem__(self, key):
		k = self._process_key(key)

		for i in range(self._size):
			hsh = self._H(k, i)
			
			if self._arr[hsh].nil:
				return None

			if not self._arr[hsh].deleted and self._arr[hsh].key == key:
				return self._arr[hsh].value

		return None

	def __len__(self):
		j = 0
		for i in range(self._size):
			if not self._arr[i].deleted and not self._arr[i].nil:
				j += 1
		
		return j

	def __setitem__(self, key, value):
		if self._busy + 1 == self._size:
			self._extend_table(_find_next_odd_prime(self._size))
			self._rehash_all()

		k = self._process_key(key)

		for i in range(self._size):
			hsh = self._H(k, i)

			wasdel = self._arr[hsh].deleted
			isnil = self._arr[hsh].nil
			busykey = self._arr[hsh].key

			if not wasdel and not isnil and busykey == key:
				self._arr[hsh].value = value
				return True

			if wasdel or isnil:
				self._arr[hsh].key = key
				self._arr[hsh].value = value
				self._arr[hsh].deleted = False
				self._arr[hsh].nil = False
				self._busy += 1
				return True
		
		return False

	def __iter__(self):
		self._count = 0
		return self

	def __next__(self):
		for i in range(self._count, self._size):
			self._count = i + 1
			
			if not self._arr[i].deleted and not self._arr[i].nil:
				return (self._arr[i].key, self._arr[i].value)

		if self._count == self._size:
			raise StopIteration

	def _extend_table(self, size):
		if size > self._size:
			if not self._arr:
				self._arr = DynamicArray()

			for _ in range(size):
				self._arr.append(HashTable.HashElement())

			self._size = size

	def _process_key(self, key):
		if type(key) == str:
			r = 0
			for idx in range(0, len(key) - 1):
				r ^= 2 * ord(key[idx]) 
			
			return r

		if issubclass(type(key), object):
			r = 0
			for bs in pickle.dumps(key):
				r += bs
				
			return r
		
		return key

	def _rehash_all(self):
		to_rehash = []
		
		self._busy = 0
		for i in range(self._size):
			if not self._arr[i].deleted and not self._arr[i].nil:
				to_rehash.append((self._arr[i].key, self._arr[i].value))
			
			self._arr[i].deleted = False
			self._arr[i].nil = True
			self._arr[i].key = None
			self._arr[i].value = None
		
		for kv in to_rehash:
			self.__setitem__(kv[0], kv[1])

	# hash functions
	def _h1(self, k):
		return k % self._size

	def _h2(self, k):
		return 7 - (k % 7)

	def _H(self, k, i):
		return (self._h1(k) + self._h2(k) * i) % self._size
