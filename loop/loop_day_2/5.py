for x in range(1000):
    s = bin(x)[2:]
    if s[-1] == '0':
        res = '1' + s + '00'
    else:
        res = '10' + s + '11'
    if int(res, 2) > 1023:
        print(int(res, 2))
        break
