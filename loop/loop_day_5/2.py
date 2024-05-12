print('w', 'x', 'y', 'F')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            f = (x and (w <= y)) == 1
            print(w, x, y, int(f))