# ---------------------------------------------------------------------------------------------------------------- 61392
# def f(n):
#     r = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             r.append(i)
#     if len(r) == 2:
#         return True
#     else:
#         return False
#                                       # Проверка на простое - говно, ниже есть лучше
#
# res = []
# for x in range(1, 101):
#     for y in range(1, 101):
#         a = '0' + '1' * x + '2' * y + '0'
#         b = '0' + '1' * x + '2' * y + '0'
#         while ('01' in b) or ('02' in b):
#             b = b.replace('02', '1110')
#             b = b.replace('01', '220')
#         if len(a) > 44 and f(sum([int(x) for x in b])):
#             res.append(sum([int(x) for x in a]))
# print(min(res))

# ---------------------------------------------------------------------------------------------------------------- 61358

# def f(n):
#     r = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             r.append(i)
#     if len(r) == 2:
#         return True
#     else:
#         return False
#
#                                       # Проверка на простое - говно, ниже есть лучше
# res = []
# for x in range(1, 101):
#     for y in range(1, 101):
#         a = '0' + '1' * x + '2' * y + '0'
#         b = '0' + '1' * x + '2' * y + '0'
#         while ('01' in b) or ('02' in b):
#             b = b.replace('02', '1110')
#             b = b.replace('01', '220')
#         if len(a) > 40 and f(sum([int(x) for x in b])):
#             res.append(sum([int(x) for x in a]))
# print(min(res))

# ---------------------------------------------------------------------------------------------------------------- 60254

# res = []
# for n in range(1000, 4, -1):
#     s = '5' + '2' * n
#     while ('52' in s) or ('2222' in s) or ('1122' in s):
#         if '52' in s:
#             s = s.replace('52', '11', 1)
#         if '2222' in s:
#             s = s.replace('2222', '5', 1)
#         if '1122' in s:
#             s = s.replace('1122', '25', 1)
#     if sum([int(x) for x in s]) == 64:
#         print(n)
#         break

# ---------------------------------------------------------------------------------------------------------------- 58520


# def f(c):
#     for i in range(2, c):
#         if c % i == 0:
#             return False
#     return True
#
#
# for n in range(49, 1000):
#     a = '0' + 48 * '1' + '2' * n + '0'
#     b = '0' + 48 * '1' + '2' * n + '0'
#     while '00' not in b:
#         b = b.replace('02', '101')
#         b = b.replace('11', '2')
#         b = b.replace('012', '30')
#         b = b.replace('010', '00')
#     if f(sum([int(x) for x in b])):
#         print(n)
#         break

# ---------------------------------------------------------------------------------------------------------------- 58479

# def f(c):
#     for i in range(2, c):
#         if c % i == 0:
#             return False
#     return True
#
#
# for n in range(41, 1000):
#     s = 40 + n * 2 - 1
#     if f(s):
#         print(n)
#         break

# ---------------------------------------------------------------------------------------------------------------- 57419

# for n in range(4, 1000):
#     s = '2' + n * '5'
#     while ('25' in s) or ('355' in s) or ('555' in s):
#         if '25' in s:
#             s = s.replace('25', '5', 1)
#         if '355' in s:
#             s = s.replace('355', '52', 1)
#         if '555' in s:
#             s = s.replace('555', '3', 1)
#     if sum([int(x) for x in s]) == 17:
#         print(n)
#         break

# ---------------------------------------------------------------------------------------------------------------- 56540

# res = []
# for n in range(1, 10000):
#     # a = '0' + '1' * n + '2' * n + '0'
#     b = '0' + '1' * n + '2' * n + '0'
#     while '00' not in b:
#         if '011' in b:
#             b = b.replace('011', '101', 1)                 # Понаписали задач
#         else:
#             b = b.replace('01', '40', 1)
#             b = b.replace('02', '20', 1)
#             b = b.replace('0222', '1401', 1)
#     if b.count('1') == 8 and b.count('2') == 13:
#         # res.append(b.count('4'))
#         print(b.count('4'))
# # print(min(res))

# ---------------------------------------------------------------------------------------------------------------- 55808

# for n in range(4, 1000):
#     s = '3' + n * '5'
#     while ('25' in s) or ('355' in s) or ('555' in s):
#         if '25' in s:
#             s = s.replace('25', '3', 1)
#         if '355' in s:
#             s = s.replace('355', '52', 1)
#         if '555' in s:
#             s = s.replace('555', '23', 1)
#     if sum([int(x) for x in s]) == 27:
#         print(n)
#         break

# ---------------------------------------------------------------------------------------------------------------- 55599

# def f(c):
#     for i in range(2, c):
#         if c % i == 0:
#             return False
#     return True
#
#
# for n in range(70, 200):
#     s = n * 3 - 1
#     if f(s):
#         print(n)
#         break

# ---------------------------------------------------------------------------------------------------------------- 51981

from itertools import product

alp = '12'
for n in product(alp, repeat=20):
    s = '0' + ''.join(n) + '0'
    if n.count('1') == n.count('2'):
        while '00' not in s:
            s = s.replace('012', '30', 1)
            if '011' in s:
                s = s.replace('011', '20', 1)
                s = s.replace('022', '40', 1)
            else:
                s = s.replace('01', '10', 1)
                s = s.replace('02', '101', 1)
        if s.count('1') == 7 and s.count('2') == 5:
            print(s.count('3'))
            break
