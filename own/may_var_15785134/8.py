from itertools import product

c = 0
alp = 'иван'
a = list(product(alp, repeat=5))
for i in a:
    if 'и' in i:
        c += 1
print(c)