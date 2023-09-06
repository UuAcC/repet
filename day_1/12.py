def check(a):
    k = 0
    for i in range(2, a // 2+1):
        if a % i == 0:
            k += 1
    if k <= 0:
        return True
    else:
        return False


n = 0
while True:
    given = ">" + "0" * 39 + "1" * n + "2" * 39
    copied = str(given)
    while (">1" in copied) or (">2" in copied) or (">0" in copied):
        if ">1" in copied:
            copied = copied.replace(">1", "22>", 1)
        elif ">2" in copied:
            copied = copied.replace(">2", "2>", 1)
        elif ">0" in copied:
            copied = copied.replace(">0", "1>", 1)
    if check(sum([int(x) for x in list(copied.replace('>', ''))])):
        break
    else:
        n += 1
print(n)
