# ---------------------------------------------------------------------------------------------------------------- 59832

from itertools import product, permutations

# count = 0
# alp = '012345678'
# nech = '1357'
# a = list(product(alp, repeat=5))
# for x in a:
#     if x[0] == '0':
#         continue
#     if x.count('3') == 2:
#         flag = True
#         for i in range(5):
#             if i == 0:
#                 if (x[i] == '2') and (x[i + 1] in nech):
#                     flag = False
#                     break
#             elif i == 4:
#                 if (x[i] == '2') and (x[i - 1] in nech):
#                     flag = False
#                     break
#             else:
#                 if (x[i] == '2') and ((x[i + 1] in nech) or (x[i - 1] in nech)):
#                     flag = False
#                     break
#         if flag:
#             count += 1
# print(count)

# ---------------------------------------------------------------------------------------------------------------- 58235

# count = 0
# alp = '0123'
# a = list(product(alp, repeat=3))
# for x in a:
#     if x[0] == '0':
#         continue
#     if (int(x[0]) + int(x[2])) > int(x[1]):
#         count += 1
# print(count)

# ---------------------------------------------------------------------------------------------------------------- 58237

# count = 0
# alp = '0123456'
# a = list(product(alp, repeat=4))
# for x in a:
#     if x[0] == '0':
#         continue
#     if int(x[0]) > int(x[1]) > int(x[2]) > int(x[3]):
#         count += 1
# print(count)

# ---------------------------------------------------------------------------------------------------------------- 58240

# c = 0
# alp = '012345678'
# a = list(product(alp, repeat=5))
# for x in a:
#     if x[0] == '0':
#         continue
#     if int(x[0]) > int(x[1]) > int(x[2]) > int(x[3]) > int(x[4]):
#         c += 1
# print(c)

# ---------------------------------------------------------------------------------------------------------------- 59713

# c = 0
# alp = 'пятница'
# a = list(product(alp, repeat=5))
# for x in a:
#     if x[0] != 'н' and x.count('я') == 1:
#         c += 1
# print(c)

# ---------------------------------------------------------------------------------------------------------------- 63057
#
# res = 0
# for a in '12345678':
#     check = int(a)
#     if check % 2 == 0:
#         for b in '1357':
#             for c in '2468':
#                 for d in '1357':
#                     for e in '2468':
#                         for f in '1357':
#                             for g in '2468':
#                                 for h in '1357':
#                                     for i in '2468':
#                                         s = ''.join([a, b, c, d, e, f, g, h, i])
#                                         flag = True
#                                         for j in '12345678':
#                                             if s.count(j) > 3:
#                                                 flag = False
#                                         if flag:
#                                             res += 1
#     else:
#         for b in '2468':
#             for c in '1357':
#                 for d in '2468':
#                     for e in '1357':
#                         for f in '2468':
#                             for g in '1357':
#                                 for h in '2468':
#                                     for i in '1357':
#                                         s = ''.join([a, b, c, d, e, f, g, h, i])
#                                         flag = True
#                                         for j in '12345678':
#                                             if s.count(j) > 3:
#                                                 flag = False
#                                         if flag:
#                                             res += 1
#
# print(res)

# ---------------------------------------------------------------------------------------------------------------- 63024

# res = 0
# c = '2468'
# nec = '1357'
# a = list(product(c, nec, c, nec, c, nec, c, nec, c, nec, c))
# for x in a:
#     flag = True
#     for i in '12345678':
#         if x.count(i) > 4:
#             flag = False
#     if flag:
#         res += 1
# print(res * 2)

# ---------------------------------------------------------------------------------------------------------------- 60250

# res = 0
# c = '0246'
# nec = '357'
# a = list(product(nec, c, nec, c, nec)) + list(product('246', nec, c, nec, c))
# for x in a:
#     flag = True
#     for i in '0234567':
#         if x.count(i) > 1:
#             flag = False
#     if flag:
#         res += 1
# print(res)

# ---------------------------------------------------------------------------------------------------------------- 58241

# res = 0
# a = list(product('12345', '012345', '012345'))
# for x in a:
#     if int(x[0]) >= int(x[1]) >= int(x[2]):
#         res += 1
# print(res)

# ---------------------------------------------------------------------------------------------------------------- 56536

# res = 0
# for a in '1234567':
#     for b in '01234567':
#         for c in '01234567':
#             for d in '01234567':
#                 for e in '01234567':                          # сдохнуть можно, пока считает
#                     for f in '01234567':
#                         for g in '01234567':
#                             for h in '01234567':
#                                 for i in '01234567':
#                                     for j in '01234567':
#                                         for k in '01234567':
#                                             for m in '01234567':
#                                                 x = ''.join([a, b, c, d, e, f, g, h, i, j, k, m])
#                                                 flag = True
#                                                 if x.count('1') + x.count('3') + x.count('5') + x.count('7') != 3:
#                                                     flag = False
#                                                 for y in range(6):
#                                                     if int(x[y]) % 2 == 1 and int(x[y + 1]) % 2 == 1:
#                                                         flag = False
#                                                 if flag:
#                                                     res += 1
# print(res)

# ---------------------------------------------------------------------------------------------------------------- 55625

res = 0
alp = 'ярослав'
a = list(permutations(alp, 5))
for x in a:
    flag = True
    if (x.count('я') + x.count('о') + x.count('а')) >= (x.count('р') + x.count('с') + x.count('л') + x.count('в')):
        flag = False
    for i in range(4):
        if (x[i] in 'яоа') and (x[i + 1] in 'яоа'):
            flag = False
    if flag:
        res += 1
print(res)