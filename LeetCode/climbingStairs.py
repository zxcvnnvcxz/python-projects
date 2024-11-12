from math import sqrt

from Tools.scripts.smelly import check_library


def climbStairs(n:int) -> int:
    if n > 1:
        n += 1
        n = float(n)
        LHS = ((1 + sqrt(5)) / 2) ** n
        RHS = ((1 - sqrt(5)) / 2) ** n
        fibonacci = (LHS - RHS) / sqrt(5)

        return int(fibonacci)


def climbStairs1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev2 = 1
    prev1 = 1
    for i in range(2, n+1):
        cur_i = prev2 + prev1
        prev2 = prev1
        prev1 = cur_i

    return prev1

print(climbStairs1(3))
