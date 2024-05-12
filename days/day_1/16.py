# def f(n):
#     res = 1
#     while n > 1:
#         res *= n
#         n -= 1
#     return res
#
#
# print(f(2023) / f(2020))

# ---- ИЛИ ЖЕ ----------------------------------------------------------------------------------------------------------

# from sys import setrecursionlimit
#
#
# def f(n):
#     if n == 1:
#         return 1
#     return n * f(n - 1)
#
#
# setrecursionlimit(3000)
# print(f(2023) // f(2020))

