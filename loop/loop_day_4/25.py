from fnmatch import fnmatch


for x in range(2024, 10**10 + 1, 2024):
    if fnmatch(str(x), '10*2024?'):
        print(x, x // 2024)