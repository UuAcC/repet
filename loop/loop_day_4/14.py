alp = '0123456789ABCDEFGHIJKLMOPQRST'
for x in alp:
    a = int(f'42{x}158', 29) + int(f'16{x}234', 29)
    if a % 28 == 0:
        print(a // 28)
        break