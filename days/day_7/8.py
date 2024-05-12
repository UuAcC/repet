from itertools import product, permutations

# ----------------------------------------------------------------------------------------------------------------- 3195

# alp = 'akru'
# a = list(product(alp, repeat=5))
# print(a[349])

# ----------------------------------------------------------------------------------------------------------------- 3200

# alp = 'аоу'
# a = list(product(alp, repeat=5))
# for x in a:
#     if list(x)[0] == 'у':
#         print(a.index(x) + 1)
#         break

# ---------------------------------------------------------------------------------------------------------------- 35466

# alp = 'авеиконр'
# a = list(product(alp, repeat=3))
# k = 0
# for x in a:
#     if x.count('в') == 1:
#         k += 1
#         if x.count('а') == 0:
#             print(k)
#             break

# ---------------------------------------------------------------------------------------------------------------- 46966

# ans = set()
# alp = 'росомаха'
# a = list(permutations(alp))
# gl = 'ао'
# for x in a:
#     flag = True
#     for i in range(1, 8):
#         if x[i] in gl and x[i-1] in gl:
#             flag = False
#         if x[i] not in gl and x[i-1] not in gl:
#             flag = False
#     if flag:
#         ans.add(x)
# print(len(ans))

# ---------------------------------------------------------------------------------------------------------------- 26982

alp = '0123456789'
a = list(permutations(alp, 6))
k = 0
for x in a:
    if x[-1] == '0' or x[-1] == '5':
        flag = True
        for i in range(1, 6):
            if int(x[i]) % 2 == int(x[i - 1]) % 2 or x[0] == "0":
                flag = False
        if flag:
            k += 1
print(k)
