# ---------------------------------------------------------------------------------------------------------------- 59818

# def dels(x):
#     d = 0
#     for i in range(1, x + 1):
#         if x % i == 0:
#             d +=1
#     return d
#
#
# def krat_2(x):
#     y = x
#     while y % 2 == 0:
#         y //= 2
#     return True if y == 1 else False
#
#
# from fnmatch import fnmatch
# for x in range(0, 10 ** 9, 31*2031):
#     if fnmatch(str(x), '*31*65?'):
#         delss = dels(x)
#         if krat_2(delss):
#             print(x, x // 2031)

# ---------------------------------------------------------------------------------------------------------------- 35483

# def is_prime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# for x in range(35_000_000, 40_000_001):
#     y = x
#     while y % 2 == 0:
#         y //= 2
#     p = int(y ** 0.25)
#     if p ** 4 == y and is_prime(p):
#         print(x)

# ---------------------------------------------------------------------------------------------------------------- 33197

for x in range(1000000, 2000001):
    sq = int(x ** 0.5) + 1
    d = []
    for i in range(1, sq):
        if x % i == 0:
            d.append(x // i - i)
    res = list(filter(lambda z: z <= 100, d))
    if len(res) >= 3:
        print(x)
