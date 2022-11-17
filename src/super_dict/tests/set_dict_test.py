def test_by_keys():
    d1 = SetDict(a=1, b=2)
    d2 = SetDict(b=2, c=3)

    inverse_d1 = SetDict({1: 'a', 2: 'b'})
    assert d1.inverse() == inverse_d1
    assert -d1 == inverse_d1
    assert ~d1 == inverse_d1

    union = SetDict(a=1, b=2, c=3)
    assert d1.union(d2) == union
    assert d1.copy().union(d2, in_place=True) == union
    assert d1 + d2 == union
    assert d1 | d2 == union

    intersection = SetDict(b=2)
    assert d1.intersect(d2) == intersection
    assert d1.copy().intersect(d2, in_place=True) == intersection
    assert d1 & d2 == intersection

    subtraction_1 = SetDict(a=1)
    assert d1.subtract(d2) == subtraction_1
    assert d1.copy().subtract(d2, in_place=True) == subtraction_1
    assert d1 - d2 == subtraction_1

    subtraction_2 = SetDict(c=3)
    assert d2.subtract(d1) == subtraction_2
    assert d2.copy().subtract(d1, in_place=True) == subtraction_2
    assert d2 - d1 == subtraction_2

    xor = SetDict(a=1, c=3)
    assert d1.xor(d2) == xor
    assert d1.copy().xor(d2, in_place=True) == xor
    assert d1 ^ d2 == xor


if __name__ == '__main__':
    from super_dict import SetDict

    test_by_keys()
