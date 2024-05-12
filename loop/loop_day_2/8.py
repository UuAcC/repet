from itertools import product

count = 0
alp = 'аивсл'
a = list(product(alp, repeat=6))
for i in a:
    if i.count('а') + i.count('и') > 3:
        count += 1
print(count)