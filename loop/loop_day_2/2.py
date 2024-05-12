for a in range(0,2):
    for b in range(0, 2):
        for c in range(0, 2):
            f = (a and (not c)) or ((not a) and b and c)
            print(a, b, c, int(f))
