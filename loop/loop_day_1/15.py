for a in range(60):
    flag = True
    for x in range(1000):
        for y in range(1000):
            flag &= ((2 * x + 3 * y != 60) or (a >= x) or (a >= y))
    if flag:
        print(a)
        break
