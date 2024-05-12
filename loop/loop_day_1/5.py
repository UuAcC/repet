x = bin(int(input()))[2:]
if x[-2:] == '10':
    print(int(x[:-2] + '1', 2))
else:
    print(int(x[:-2] + '0', 2))
