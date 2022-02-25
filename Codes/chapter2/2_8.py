def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))


def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)

    counted.call_count = 0  # 相当于静态变量
    return counted


fib = count(fib)
print(fib(19))
print(fib.call_count)


def count_frames(f):
    def counted(*args):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(*args)
        counted.open_count -= 1
        return result

    counted.open_count = 0
    counted.max_count = 0
    return counted


fib = count_frames(fib)
print(fib(19))
print(fib.open_count)
print(fib.max_count)


def memo(f):
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return memoized


counted_fib = count(fib)
fib = memo(counted_fib)

print(fib(19))
print(counted_fib.call_count)

print(fib(34))
print(counted_fib.call_count)


def exp(b, n):
    if n == 0:
        return 1
    return b * exp(b, n - 1)


def exp_iter(b, n):
    result = 1
    for _ in range(n):
        result *= b
    return result


def square(x):
    return x * x


def fast_exp(b, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return square(fast_exp(b, n / 2))
    else:
        return b * fast_exp(b, n - 1)


print(fast_exp(2, 100))
