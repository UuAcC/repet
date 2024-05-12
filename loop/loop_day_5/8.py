from itertools import product

c = 0
alp = '0123456789ABCDEF'
a = list(product(alp, repeat=5))
for x in a:
    if x[0] != '0':
        cc = 0
        for i in '0123456789':
            cc += x.count(i)
        if cc == 1:
            c += 1
print(c)