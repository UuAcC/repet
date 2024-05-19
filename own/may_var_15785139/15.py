for A in range(1, 100):
    flag = True
    for x in range(100):
        for y in range(100):
            f = (5 * x + 3 * y != 60) or ((A > x) and (A > y))
            if not f:
                flag = False
    if flag:
        print(A)
        break
