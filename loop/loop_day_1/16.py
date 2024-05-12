from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 3:
        return 2
    elif (n > 2) and (n % 2 == 0):
        return f(n - 2) + f(n - 1) - n
    elif (n > 2) and (n % 2 == 1):
        return f(n - 1) - f(n - 2) + 2 * n


print(f(32))