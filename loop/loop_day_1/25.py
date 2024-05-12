a = []
for m in range(0, 30, 2):
    for n in range(1, 20, 2):
        x = 2 ** m * 3 ** n
        if 200_000_000 <= x <= 400_000_000:
            a.append(x)
a.sort()
for x in a:
    print(x)
