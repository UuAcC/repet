from itertools import product

c = 0
alp = "гдо"
a = list(product(alp, repeat=6))
for i in a:
    if ((i[0] == 'г') or (i[0] == 'д')) and ((i[-1] == 'г') or (i[-1] == 'д')):
        c += 1
print(c)