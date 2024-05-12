for A in range(1, 1001):
    flag = True
    for x in range(1, 5000):
        if not ((not (x % 72 == 0)) or (x % 495 == 0) or (not (x % A == 0))):
            flag = False
    if flag:
        print(A)
