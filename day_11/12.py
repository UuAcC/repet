# --------------------------------------------------------------------------------------------------------------- пример
# s = '5' * 54 + '7'
# while ('722' in s) or ('557' in s):
#     if '722' in s:
#         s = s.replace('722', '57', 1)
#     else:
#         s = s.replace('557', '72', 1)
# print(s)

# ------------------------------------------------------------------------------------------------------------- пример-2

# for n in range(4, 10000):
#     s = '5' + '2' * n
#     while ('72' in s) or ('2222' in s) or ('522' in s):
#         s = s.replace('72', '2', 1)
#         s = s.replace('522', '27', 1)
#         s = s.replace('2222', '5', 1)
#     if sum([int(x) for x in s]) == 63:
#         print(n)
#         break

# ------------------------------------------------------------------------------------------------------------- пример-3
for x in range(21):  # блоки по 1 двойке
    y = 40 - 2 * x   # блоки по 2 двойки
    k = 2 * y + x    # кол-во двоек в исходной
    for i in range(k + 1):  #
        j = k - i           #
        z = i * 2           #
        if z > 50:
            print(z)
            break
    break
