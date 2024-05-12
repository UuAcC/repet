for A in range(1000, 10, -1):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            f = ((x <= 9) <= (x ** 2 <= A)) and ((y ** 2 <= A) <= (y <= 9))
            if not f:
                flag = False
    if flag:
        print(A)
        break