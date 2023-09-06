print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = x and (not y)
                f2 = y == z
                f = f1 or f2 or (not w)
                if not f:
                    print(x, y, z, w)
