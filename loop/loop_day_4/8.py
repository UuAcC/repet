from itertools import product


alp = 'АЁРТШ'
a = list(product(alp, repeat=5))
print(a[182])
for x in range(len(a)):
    if a[x].count('А') <= 1:
        flag = True
        for i in range(4):
            if (a[x][i] == 'Ё') and (a[x][i + 1] == 'Ё'):
                flag = False
                break
        if flag:
            print(x + 1)
            break
