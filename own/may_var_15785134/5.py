for n in range(1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        r = int('1' + s + '0', 2)
    else:
        r = int('11' + s + '11', 2)
    if r > 52:
        print(n)
        break