alp = '0123456789ABCDEFGHIJKL'
for x in alp:
    for y in alp:
        a = int(f'34256{x}4', 22) + int(f'72847{y}3', 22)
        if a % 125 == 0:
            print(f'x, y = {x},{y}, x + y = {int(x, 22) + int(y, 22)}, a / 125 = {a // 125}')
