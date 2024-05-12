print('x y z w F')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f1 = (x <= (y == w))
                f2 = (y == (w <= z))
                f = f1 and f2
                print(x, y, z, w, int(f))