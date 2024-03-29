from operator import sub, mul
HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############


def num_sevens(x):
    """Returns the number of times 7 appears as a digit of x.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_sevens',
    ...       ['Assign', 'AugAssign'])
    True
    """
    if x == 0:
        return 0
    if x % 10 == 7:
        return 1 + num_sevens(x//10)
    return num_sevens(x//10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def _contains7(num):
        if (num == 0):
            return False
        if (num % 10 == 7):
            return True
        return _contains7(num//10)

    def _helper(idx, val, direction):
        if idx == n:
            return val

        if (idx % 7 == 0) or _contains7(idx):
            return _helper(idx+1,  val - direction, -direction)

        return _helper(idx+1,  val + direction, direction)

    return _helper(1,  1, 1)


def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    # coins = [1, 2, 4, 8, 16]

    def _helper(amount, kinds_of_coins):
        if amount == 0:
            return 1
        elif (amount < 0) or (kinds_of_coins <= 0):
            return 0

        return _helper(amount-kinds_of_coins, kinds_of_coins) + _helper(amount, kinds_of_coins//2)

    # 使用面值d + 不使用面值d
    return _helper(total, 2**6)


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def _helper(count, num):
        if num//10 == 0:
            return count
        if (num % 10) != (num//10 % 10):
            return _helper(count+(num % 10)-(num//10 % 10)-1, num//10)
        else:
            return _helper(count, num//10)
    return _helper(0, n)


###################
# Extra Questions #
###################

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"

    def _helper(n, start, end):
        if start <= end:
            return
        # 步骤一 将除了最低下的一个 移到 中间
        # 步骤二 将最低下的 移到 最后
        # 步骤三 将中间的 移到 最后
        mid = end-start
        _helper(n-1, start, mid)

        print_move(start, end)

        _helper(n-1, mid, end)
    return _helper(n, start, end)


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: f(f))(lambda f: lambda n: 1 if n == 1 else mul(n, f(f)(sub(n, 1))))
