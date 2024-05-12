# ------------------------------------------------------------------------------------------------------ first on lesson

# from fnmatch import fnmatch
# for x in range(1991, 10 ** 8, 1991):
#     if fnmatch(str(x), '3?1*57'):
#         print(x, x // 1991)

# ----------------------------------------------------------------------------------------------------- second on lesson

# def M(n):
#     sq = int(n ** 0.5) + 1
#     for a in range(2, sq):
#         if n % a == 0:
#             if n // a != a:
#                 return a + n // a
#     return 0
#
#
# n = 452022
# k = 0
# while k < 5:
#     m = M(n)
#     if m % 7 == 3:
#         print(n, m)
#         k += 1
#     n += 1

# -------------------------------------------------------------- 40741 --------------------------------- third on lesson

def M(n):
    d = []
    sq = int(n ** 0.5) + 1
    for a in range(2, sq):
        if n % a == 0:
            d.append(a)
            if n // a != a:
                d.append(n // a)
    d.sort()
    if len(d) >= 2:
        return d[-1] + d[-2]
    return 0


n = 10_000_001
k = 0
while k < 5:
    m = M(n)
    if 0 < m < 10000:
        print(n, m)
        k += 1
    n += 1
