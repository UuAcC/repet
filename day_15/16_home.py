# ---------------------------------------------------------------------------------------------------------------- 60258

# print(2022 * 2023)

# ---------------------------------------------------------------------------------------------------------------- 47220

# print(2023 * 2022 * 2021)

# ---------------------------------------------------------------------------------------------------------------- 58228
# from functools import lru_cache
#
#
# @lru_cache(None)
# def F(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n > 2 and n % 2 == 0:
#         return ((4 * n - F(n - 3)) / 8) * 10 // 10
#     if n > 2 and n % 2 == 1:
#         return ((4 * n - F(n - 1) + F(n - 2)) / 8) * 10 // 10
#
#
# print(F(52) - F(38))

# ---------------------------------------------------------------------------------------------------------------- 48437

# c = 0
# s = sum(range(237267892))
# if s % 3 != 0:
#     c += 1
# for x in range(237267893, 1134567005):
#     s += x
#     if s % 3 != 0:
#         c += 1
# print(c)

# ---------------------------------------------------------------------------------------------------------------- 48464

# print(len(range(765_432_010, 1_542_613_235, 3)))

# ----------------------------------------------------------------------------------------------------------------- 4657
# def F(n):
#     if n == 1:
#         return 1
#     else:
#         return 2 * G(n -1) + 5 * n
#
#
# def G(n):
#     if n == 1:
#         return 1
#     else:
#         return F(n - 1) + 2 * n
#
#
# print(F(4) + G(4))

# ---------------------------------------------------------------------------------------------------------------- 55633

# def F(n):
#     global left, right
#     r1 = right
#     l1 = left
#     while l1 % n != 0:
#         l1 += 1
#     while r1 % n != 0:
#         r1 -= 1
#     return len(range(r1, l1 + 1, n))
#
#
# right = 123456798
# left = 1234567885
# a3 = F(3)
# a5 = F(5)
# a15 = F(15)
# print(left - right + 1 - a3 - a5 + a15)

# ---------------------------------------------------------------------------------------------------------------- 58483

# def F(n):
#     if n > 1000000:
#         return n
#     else:
#         return n + F(2 * n)
#
#
# g1000 = F(1000)/1000
# print(len([1 for n in range(1, 2000) if F(n)/n == g1000]))

# ---------------------------------------------------------------------------------------------------------------- 58524

# def F(n):
#     if n > 1000000:
#         return n
#     else:
#         return n + F(2 * n)
#
#
# g = F(2000)/2000
# print(len([1 for n in range(1, 4000) if F(n)/n == g]))

# ---------------------------------------------------------------------------------------------------------------- 61396

# def F(n):
#     if n >= 2000:
#         return 2000
#     else:
#         if n % 2 == 1:
#             return n * F(n + 1)
#         else:
#             return n * (F(n + 1) / 2)
#
#
# print(F(1998)/F(2001))

# ---------------------------------------------------------------------------------------------------------------- 56516

# def F(a, b):
#     if b == 0:
#         return a
#     if a >= b:
#         return F(a - 1, b) + b
#     elif a < b and b > 0:
#         return F(a, b - 1) + a
#
#
# print(F(5, 3))

# c = 0
# x = 1048577
# for i in range(1, x):
#     if (x - 1) % i == 0:
#         c += 1
# print(c)

# ---------------------------------------------------------------------------------------------------------------- 40732

# def F(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 3 == 2:
#         return F(n - 1) + 1
#     elif n > 0 and n % 3 < 2:
#         return F((n - n % 3) // 3)
#
#
# i = 0
# while F(i) != 6:
#     i += 1
# print(i)

# ---------------------------------------------------------------------------------------------------------------- 39245

# c = 0
# for i in range(1, 901):
#     if sum([int(x) for x in bin(i)[2:]]) == 9:
#         c += 1
# print(c)

# ---------------------------------------------------------------------------------------------------------------- 33188

def F(n):
    if n == 0:
        return 0
    if n % 3 == 0 and n > 0:
        return n + F(n - 3)
    if n % 3 > 0:
        return n + F(n - (n % 3))


print(F(22))
