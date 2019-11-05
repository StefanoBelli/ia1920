from ctypes import py_object
from collections.abc import Sequence

class readonly_array(Sequence):
    def __init__(self, *args):
        argl = len(args)
        if argl > 0:
            self._cap = argl
            self._nelem = argl
            self._raw = (self._cap * py_object)()

            for i in range(argl):
                self._raw[i] = args[i]
        else:
            self._cap = 0
            self._nelem = 0
            self._raw = None

    def __getitem__(self, idx):
        return self._raw[idx]

    def __len__(self):
        return self._nelem

    def __str__(self):
        if self._nelem > 0:
            s = "[ "
            for i in range(self._nelem):
                s += "{}, ".format(self._raw[i])

            s = s[:-2]
            s += " ]"

            return s

        return "[]"

    def __repr__(self):
        return self.__str__()

    # Provides:
    #  __contains__
    #  __iter__
    #  __reversed__
    #  index
    #  count