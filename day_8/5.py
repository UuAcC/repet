# ----------------------------------------------------------------------------------------------------------------- 7751

# for a in range(1, 10):
#     for b in range(10):
#         for c in range(10):
#             for d in range(10):
#                 x = a + b
#                 y = c + d
#                 x, y = max(x, y), min(x, y)
#                 s = str(y) + str(x)
#                 if s == '117':
#                     print(a, b, c, d, sep='')

# ---------------------------------------------------------------------------------------------------------------- 14767

# for a in range(1, 10):
#     for b in range(10):
#         for c in range(10):
#             for d in range(10):
#                 x = a + b
#                 y = b + c
#                 z = c + d
#                 mx = max(x, y, z)
#                 mn = min(x, y, z)
#                 md = x + y + z - mn - mx
#                 if str(md) + str(mx) == '613':
#                     print(a, b, c, d, sep='')

# -------------------------------------------------------------------------------------------------- двоичное и троичное

# ---------------------------------------------------------------------------------------------------------------- 58472
# for n in range(500000, 0, -1):
#     s = bin(n)[2:]
#     if n % 5 == 0:
#         s += '101'
#     else:
#         s += '1'
#     x = int(s, 2)
#     if x % 7 == 0:
#         s += '111'
#     else:
#         s += '1'
#     r = int(s, 2)
#     if r < 1728404:
#         print(n)
#         break

# ---------------------------------------------------------------------------------------------------------------- 52176

# def f(n):
#     s = [int(x) for x in str(n)]
#     return sum(s)
#
#
# a = []
# for n in range(10000):
#     s = bin(n)[2:]
#     for i in range(3):
#         k = f(int(s, 2))
#         if k % 2 == 1:
#             s += '1'
#         else:
#             s += '0'
#     r = int(s, 2)
#     if r > 2054:
#         a.append(r)
# print(min(a))

# ---------------------------------------------------------------------------------------------------------------- 59828

def f(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]


for n in range(1, 2000):
    s = f(n)
    if n % 3 == 0:
        s += s[-3:]
    else:
        s += f((n % 3) * 3)
    r = int(s, 3)
    if r > 150:
        print(n)
        break
