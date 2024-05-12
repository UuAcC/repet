# ---------------------------------------------------------------------------------------------------------------- 27855

# def M(n):
#     d = []
#     for x in range(2, n + 1):
#         if n % x == 0 and x % 2 == 0:
#             d.append(x)
#             if len(d) > 6:
#                 break
#     d.sort()
#     return d
#
#
# for a in range(95632, 95701):
#     res = M(a)
#     if len(res) == 6:
#         print(*res)

# ---------------------------------------------------------------------------------------------------------------- 27856

# def M(n):
#     d = []
#     for x in range(1, n + 1):
#         if n % x == 0 and x % 2 == 1:
#             d.append(x)
#             if len(d) > 6:
#                 break
#     d.sort()
#     return d
#
#
# for a in range(95632, 95651):
#     res = M(a)
#     if len(res) == 6:
#         print(*res)

# ---------------------------------------------------------------------------------------------------------------- 27858

# def M(n):
#     d = 0
#     for x in range(1, n + 1):
#         if n % x == 0:
#             d += 1
#     return d
#
#
# dikt = {}
# for a in range(120115, 120201):
#     d = M(a)
#     dikt[a] = d
# m = max(dikt.values())
# print(m, max(filter(lambda y: dikt[y] == m, dikt.keys())))

# ---------------------------------------------------------------------------------------------------------------- 28121

# def M(n):
#     for x in range(2, n):
#         if n % x == 0:
#             return False
#     return True
#
#
# res = []
# for a in range(2422000, 2422081):
#     if M(a):
#         res.append(a)
# for num, elem in enumerate(res):
#     print(num + 1, elem)

# ---------------------------------------------------------------------------------------------------------------- 28122

# def M(n):
#     d = []
#     for x in range(1, n + 1):
#         if n % x == 0:
#             d.append(x)
#             if len(d) > 4:
#                 break
#     return d
#
#
# for a in range(489421, 489441):
#     res = M(a)
#     if len(res) == 4:
#         print(*res)

# ---------------------------------------------------------------------------------------------------------------- 28123

def M(n):
    d = []
    for x in range(2, n + 1):
        if n % x == 0 and x % 2 == 0:
            d.append(x)
            if len(d) > 6:
                break
    return d


for a in range(125256, 125330):
    res = M(a)
    if len(res) == 6:
        print(*res)