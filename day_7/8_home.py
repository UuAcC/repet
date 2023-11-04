from itertools import product, permutations

# ----------------------------------------------------------------------------------------------------------------- 7667
# alp = 'ЕГЭ'
# a = list(product(alp, repeat=5))
# count = 0
# for x in a:
#     if x[0] != 'Г':
#         count += 1
# print(count)

# ---------------------------------------------------------------------------------------------------------------- 16886
alp = 'МАТВЕЙ'
count = 0
a = list(permutations(alp, 6))
for x in a:
    if (x[0] != 'Й') and ('АЕ' not in ''.join(x)):
        count += 1
print(count)
