class SetDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._view = self.keys  # TODO: Support other views, comparing by value() or items()

    def inverse(self):
        return self.__class__({v: k for k, v in self.items()})

    def __neg__(self):
        return self.inverse()

    def __invert__(self):
        return self.inverse()

    def intersect(self, other, in_place=False):
        if in_place:
            allowable_items = self._view() - set(other)
            for k in allowable_items:
                self.pop(k)
            return self
        return self.copy().intersect(other, in_place=True)

    def __and__(self, other):
        return self.intersect(other, in_place=False)

    def copy(self):
        return self.__class__(self)

    def union(self, other, in_place=False):
        if in_place:
            self.update(other)
            return self
        return self.copy().union(other, in_place=True)

    def __or__(self, other):
        return self.union(other, in_place=False)

    def __add__(self, other):
        return self.union(other, in_place=False)

    def subtract(self, other, in_place=False):
        keys = set(other)
        if in_place:
            for k in keys:
                if k in self:
                    self.pop(k)
            return self
        return self.copy().subtract(other, in_place=True)

    def __sub__(self, other):
        return self.subtract(other, in_place=False)

    def xor(self, other, in_place=False):
        keys = set(other)
        intersection = self.intersect(keys)
        if in_place:
            self.union(other, in_place=True)
            self.subtract(intersection, in_place=True)
            return self
        return self.copy().xor(other, in_place=True)

    def __xor__(self, other):
        return self.xor(other, in_place=False)
