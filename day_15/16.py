# ---------------------------------------------------------------------------------------------------------------- 55603

# from math import gcd
#
# ans = 0
# for i in range(123456795, 1234567889):
#     if gcd(i, 14) == 1:
#         ans += 1
# print(ans)

# left = 123456795
# right = 1234567888
# l1 = left
# r1 = right
# while l1 % 2 != 0:
#     l1 += 1
# while r1 % 2 != 0:
#     r1 -= 1
# a2 = len(range(l1, r1 + 1, 2))
# l1 = left
# r1 = right
# while l1 % 7 != 0:
#     l1 += 1
# while r1 % 7 != 0:
#     r1 -= 1
# a7 = len(range(l1, r1 + 1, 7))
# l1 = left
# r1 = right
# while l1 % 14 != 0:
#     l1 += 1
# while r1 % 14 != 0:
#     r1 -= 1
# a14 = len(range(l1, r1 + 1, 14))
#
# print(right - left + 1 - a2 - a7 + a14)

# -------------------------------------------------------------------------------------------------------------- ПОЛЯКОВ

# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n):
#     if n < 3:
#         return 1
#     if n % 2 == 0:
#         return g(n) + f(n - 1)
#     else:
#         return f(n - 2) - 2 * g(n + 1)
#
#
# def g(n):
#     if n < 3:
#         return 1
#     if n % 2 == 0:
#         return f(n - 3) + f(n - 2)
#     else:
#         return f(n + 1) - g(n - 1)
#
#
# print(g(120))

# ---------------------------------------------------------------------------------------------------------------- 59694

f = [0] * 2025
for i in range(11):
    f[i] = i
for i in range(11, 2025):
    f[i] = i + f[i - 1]
print(f[2024] - f[2021])
