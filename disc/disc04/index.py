import math

# n postive


def count_stair_ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_stair_ways(n-1)+count_stair_ways(n-2)

# n, k postive


def count_k(n, k):
    if n < 0:
        return 0
    if n == 0:
        return 1
    result = 0
    for i in range(1, k+1):
        result += count_k(n-i, k)
    return result


def even_weighted(s):
    return [s[i]*i for i in range(len(s)) if i % 2 == 0]


def max_product(s):
    if len(s) == 0:
        return 1
    if len(s) == 1:
        return s[0]
    idx = 2
    result = []
    for i in range(int(math.sqrt(len(s)))):
        result.append(s[0]*max_product(s[idx:]))
        idx += 1
    return max(result)


def check_hole_number(n):
    if (n < 100):
        return True
    low = n % 10
    middle = (n//10) % 10
    high = (n//100) % 10
    if (low <= middle) or (middle >= high):
        return False
    return check_hole_number(n//100)


def check_mountain_number(n):
    def helper(n, is_increase):
        if n < 10:
            return True
        if is_increase and (n % 10) < (n//10 % 10):
            return helper(n//10, True)
        return (n % 10) > (n//10 % 10) and helper(n//10, False)
    return helper(n, True)


if __name__ == "__main__":
    assert count_stair_ways(3) == 3
    assert count_k(3, 3) == 4
    assert count_k(4, 4) == 8
    assert count_k(10, 3) == 274
    assert count_k(300, 1) == 1

    assert even_weighted([1, 2, 3, 4, 5, 6]) == [0, 6, 20]

    assert max_product([10, 3, 1, 9, 2]) == 90
    assert max_product([5, 10, 5, 10, 5]) == 125
    assert max_product([]) == 1

    assert check_hole_number(123) == False
    assert check_hole_number(3245968) == False
    assert check_hole_number(3241968) == True

    assert check_mountain_number(103) == False
    assert check_mountain_number(153) == True
    assert check_mountain_number(123456) == True
    assert check_mountain_number(2345986) == True
