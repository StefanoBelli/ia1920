class Vector2D:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __len__(self):
        return 2

    def __repr__(self):
        return "2DVector({},{})".format(self._x, self._y)

    def __str__(self):
        return "({},{})".format(self._x, self._y)

    def __getitem__(self, pos):
        if pos == 0:
            return self._x

        return self._y
    
    def __eq__(self, vec):
        return self._x == vec._x and self._y == vec._y

    def __lt__(self, vec):
        return self._x < vec._x and self._y < vec._y

    def __add__(self, vec):
        return Vector2D(self._x + vec._x, self._y + vec._y)

    def __iter__(self):
        self._niter = 0
        return self

    def __next__(self):
        if self._niter == 0:
            self._niter += 1
            return self._x
        elif self._niter == 1:
            self._niter += 1
            return self._y

        raise StopIteration

vec = Vector2D(2,3)
for component in vec:
    print(component)
for component in vec:
    print(component)
