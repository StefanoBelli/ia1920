from ctypes import py_object
from collections.abc import Collection

class dynamic_array(Collection):
    def __init__(self, *args):
        argl = len(args)
        if argl == 0 or argl == 1:
            self._cap = 2
        else:
            self._cap = argl << 1

        self._nelem = argl
        self._raw = (self._cap * py_object)()

        for i in range(argl):
            self._raw[i] = args[i]

    def __len__(self):
        return self._nelem

    def __iter__(self):
        self._counter = 0
        return self

    def __next__(self):
        if self._counter == self._nelem:
            raise StopIteration

        request = self._raw[self._counter]
        self._counter += 1
        return request

    def __getitem__(self, idx):
        return self._raw[idx]

    def __contains__(self, what):
        return what in self._raw

    def __str__(self):
        if self._nelem > 0:
            s = "[ "
            for i in self:
                s += "{}, ".format(i)

            s = s[:-2]
            s += " ]"

            return s

        return "[]"

    def __repr__(self):
        return self.__str__()

    def _resize(self, cap):
        _newraw = (cap * py_object)()

        lnr = len(_newraw)
        lr = len(self._raw)
        size = None

        if lnr > lr:
            size = lr
        else:
            size = lnr

        for i in range(size):
            _newraw[i] = self._raw[i]

        self._cap = cap
        self._raw = _newraw

    # @public
    def append(self, what):
        if self._nelem >= self._cap:
            self._resize(self._cap << 1)

        self._raw[self._nelem] = what
        self._nelem += 1

    # @public
    def remove(self, idx):
        if idx < 0 or idx >= self._nelem:
            raise IndexError("invalid index: contains {} items".format(self._nelem))

        for i in range(idx + 1, self._nelem):
            self._raw[i - 1] = self._raw[i]

        self._nelem -= 1

        if self._nelem < (self._cap / 2):
            self._resize(self._nelem + 1)

    # @public
    def get_capacity(self):
        return self._cap
