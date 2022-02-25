class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i - 1]

    def __len__(self):
        return 1 + len(self.rest)


s = Link(3, Link(4, Link(5)))
print(len(s))
print(s[1])


def link_expression(s):
    """Return a string that  would evaluate to s."""
    if s.rest is Link.empty:
        rest = ""
    else:
        rest = ", " + link_expression(s.rest)
    return 'Link({0}{1})'.format(s.first, rest)


print(link_expression(s))

Link.__repr__ = link_expression
print(s)

s_first = Link(s, Link(6))
print(s_first)


def extend_link(s, t):
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))


print(extend_link(s, s))

Link.__add__ = extend_link
print(s + s)


def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))


square = lambda x: x * x
print(map_link(square, s))


def filter_link(f, s):
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered


odd = lambda x: x % 2 == 1
print(map_link(square, filter_link(odd, s)))


def join_link(s, separator):
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_link(s.rest, separator)


print(join_link(s, ", "))


class Tree:
    def __init__(self, label, branches=()):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.label))

    def is_leaf(self):
        return not self.branches


def fib_tree(n):
    if n == 1:
        return Tree(0)
    elif n == 2:
        return Tree(1)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        return Tree(left.label + right.label, (left, right))


print(fib_tree(5))


def sum_labels(t):
    """Sum the labels of a Tree instance, which may be None."""
    return t.label + sum([sum_labels(b) for b in t.branches])


print(sum_labels(fib_tree(5)))


def memo(f):
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return memoized


fib_tree = memo(fib_tree)
big_fib_tree = fib_tree(35)
print(big_fib_tree.label)