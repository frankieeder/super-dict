class SetDict(dict):
    def __neg__(self):
        return {v: k for k, v in self.items()}

    def copy(self):
        return SetDict(self)

    def union(self, other, in_place=False):
        if in_place:
            self.update(other)
            return self
        else:
            new = self.copy()
            new.update(other)
            return new

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
        else:
            return SetDict({k: v for k, v in self.items() if k not in keys})

    def __sub__(self, other):
        return self.subtract(other, in_place=False)

    def intersect(self, other, in_place=False):
        keys = set(other)
        if in_place:
            for k in self.keys() - keys:
                self.pop(k)
            return self
        else:
            return SetDict({k: v for k, v in self.items() if k in keys})

    def __and__(self, other):
        return self.intersect(other, in_place=False)

    def xor(self, other, in_place=False):
        keys = set(other)
        intersection = self.intersect(keys)
        if in_place:
            self.union(other, in_place=True)
            self.subtract(intersection, in_place=True)
            return self
        else:
            return (self | other) - intersection

    def __xor__(self, other):
        return self.xor(other)
