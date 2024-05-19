rr = open('9.txt').readlines()
co = 0
for s in rr:
    a, b, c = [int(x) for x in s.split()]
    if (a ** 2 + b ** 2 == c ** 2) or (c ** 2 + b ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2):
        co += 1
print(co)