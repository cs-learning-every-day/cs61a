from typing import Counter, Match


def multiply(m, n):
    if n == 0:
        return 0
    if n == 1:
        return m
    return m + multiply(m, n-1)


def rec(x, y):
    if y > 0:
        return x * rec(x, y-1)
    return 1


def hailstone(n):
    print(n)
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1+hailstone(n//2)
    else:
        return 1+hailstone(n*3+1)


def is_prime(n):
    return prime_helper(n, 2)


def prime_helper(n, factor):
    if (factor > 1) and (factor < n) and (n % factor == 0):
        return False
    elif factor*factor >= n:
        return True
    return prime_helper(n, factor+1)


def merge(n1, n2):

    # 3 4  --> 43
    def _helper1(k1, k2):
        if k1 == 0:
            return k2
        if k2 == 0:
            return k1
        if k1 > k2:
            return k1*10+k2
        return k1+k2*10

    def _helper2(k1, k2, count, result):
        if (k1 == 0 and k2 == 0):
            return result
        newNum = _helper1(k1 % 10, k2 % 10)
        result += newNum * (10**count)
        return _helper2(k1//10, k2//10, count+len(str(newNum)), result)
    return _helper2(n1, n2, 0, 0)


def make_func_repeater(f, x):
    def repeat(n):
        if x == 1:
            return f(n)
        else:
            return f(make_func_repeater(f, x-1)(n))
    return repeat


if __name__ == "__main__":
    print(multiply(5, 3))
    print(rec(3, 2))
    print()
    print(hailstone(10))
    print()
    print(is_prime(1))
    print(is_prime(7))
    print(is_prime(10))
    print(is_prime(3))
    print()
    print(merge(31, 42))
    print(merge(21, 0))
    print(merge(21, 31))

    incr_1 = make_func_repeater(lambda x: x + 1, 3)
    print(incr_1(2))
    print(incr_1(5))
