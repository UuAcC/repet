print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x == (w or y)) or ((w <= z) and (y <= w))
                if not F:
                    print(x, y, z, w, int(F))