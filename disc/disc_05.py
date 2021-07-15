

# Tree ADT


from typing import Sequence


def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])


def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if (is_leaf(t)):
        return 0
    res = 0
    for b in branches(t):
        bh = height(b) + 1
        if res < bh:
            res = bh
    return res


def square_tree(t):
    if is_leaf(t):
        return tree(label(t)*label(t))
    return tree(label(t)*label(t), [square_tree(b) for b in branches(t)])


def find_path(tree, x):
    if is_leaf(tree) and label(tree) != x:
        return None
    else:
        path = [label(tree)]
        for b in branches(tree):
            res = find_path(b, x)
            if res:
                path += res
        return None if path[-1] != x else path


def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(2, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    while x > 0:
        lst.append(el)
        x = x - 1


def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    res = {}
    for v in s:
        k = fn(v)
        if k in res.keys():
            res[k].append(v)
        else:
            res[k] = [v]

    return res


def partition_options(total, biggest):
    """
    >>> partition_options(2, 2)
    [[2], [1, 1]]
    >>> partition_options(3, 3)
    [[3], [2, 1], [1, 1, 1]]
    >>> partition_options(4, 3)
    [[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
    """
    if total == 0:
        return [[]]
    elif total < 0 or biggest == 0:
        return []

    with_biggest = partition_options(total - biggest, biggest)
    without_biggest = partition_options(total, biggest - 1)
    return [[biggest]+b for b in with_biggest] + without_biggest


def min_elements(T, lst):
    """
    >>> min_elements(10, [4, 2, 1]) # 4 + 4 + 2
    3
    >>> min_elements(12, [9, 4, 1]) # 4 + 4 + 4
    3
    >>> min_elements(0, [1, 2, 3])
    0
    """


if __name__ == "__main__":
    t = tree(3, [tree(5, [tree(1)]), tree(2)])
    assert(height(t) == 2)

    numbers = tree(1, [tree(2, [tree(3), tree(4)]),
                       tree(5, [tree(6, [tree(7)]), tree(8)])])

    assert(height(numbers) == 3)
    print_tree(square_tree(numbers))

    t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])

    assert(find_path(t, 5) == [2, 7, 6, 5])
    assert(find_path(t, 3) == [2, 7, 3])
    assert(find_path(t, 10) == None)

    lst = [1, 2, 4, 2, 1]

    add_this_many(2, 5, lst)
    assert(lst == [1, 2, 4, 2, 1, 5, 5])

    add_this_many(2, 2, lst)
    assert(lst == [1, 2, 4, 2, 1, 5, 5, 2, 2])

    print(group_by([12, 23, 14, 45], lambda p: p // 10))
    print(group_by(range(-3, 4), lambda x: x * x))

    assert(partition_options(2, 2) == [[2], [1, 1]])
    assert(partition_options(3, 3) == [[3], [2, 1], [1, 1, 1]])
    assert(partition_options(4, 3) == [
           [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]])

    assert(min_elements(10, [4, 2, 1]) == 3)
    assert(min_elements(12, [9, 4, 1]) == 3)
    assert(min_elements(0, [1, 2, 3]) == 0)
