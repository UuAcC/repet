for x in range(1000):
    c = x * (x - 1) * 3 + (x - 1) ** 2
    if c > 100000:
        print(x)
        break
