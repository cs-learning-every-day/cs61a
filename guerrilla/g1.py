

def map_mut(f, L):
    L[:] = [f(x) for x in L]


def paths(m, n):
    def _helper(i, j):
        if i < 0 or j > n:
            return 0
        if i == 0 and j == n-1:
            return 1
        return _helper(i-1, j)+_helper(i, j+1)

    return _helper(m-1, 0)


def merge(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return s1 or s2  # [] or [1,2,3]   --> [1,2,3]
    if s1[0] < s2[0]:
        return [s1[0]]+merge(s1[1:], s2)
    else:
        return [s2[0]]+merge(s1, s2[1:])


def mario_number(level):
    if len(level) == 0 or level[0] == 'P':
        return 0
    if len(level) == 1:
        return 1
    if(level[1] == 'P'):
        return mario_number(level[2:])  # jump
    else:
        # jump or step
        return mario_number(level[1:]) + mario_number(level[2:])


if __name__ == "__main__":
    L = [1, 2, 3, 4]
    map_mut(lambda x: x**2, L)
    assert L == [1, 4, 9, 16]

    assert paths(2, 2) == 2
    assert paths(117, 1) == 1

    assert merge([1, 3], [2, 4]) == [1, 2, 3, 4]
    assert merge([1, 2], []) == [1, 2]

    assert mario_number('-P-P-') == 1
    assert mario_number('-P-P-') == 1
    assert mario_number('--P-P-') == 1
    assert mario_number('---P-P-') == 2
    assert mario_number('-P-PP-') == 0
    assert mario_number('----') == 3
    assert mario_number('----P----') == 9
    assert mario_number('---P----P-P---P--P-P----P-----P-') == 180
