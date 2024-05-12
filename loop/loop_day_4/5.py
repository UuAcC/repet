for n in range(1000):
    bn = bin(n)[2:]
    if n % 2 == 0:
        bn = '1' + bn + '1'
    else:
        bn = bn + '10'
    if int(bn, 2) > 179:
        print(n)
        break

