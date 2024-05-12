from fnmatch import fnmatch


c = 0
m = 0
for x in range(492_000_000_000 + 42, 500_000_000_000, 123):
    if x % 123 == 42:
        if fnmatch(str(x), '4?8?15?16?23'):
            print(x)
            c += 1
            m = max(m, x)
print(c, m)