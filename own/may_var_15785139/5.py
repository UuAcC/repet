for n in range(100):
    bn = bin(n)[2:]
    if n % 2 == 0:
        bn += '10'
    else:
        bn += '01'
    r = int(bn, 2)
    if r < 102:
        print(r)
    else:
        break
