for i in range(1000, 10000):
    s = [int(x) for x in str(i)]
    if 0 not in s:
        ss = sum(s)
        a = []
        for x in s:
            a.append(ss % x)
        a = [str(x) for x in sorted(a, reverse=True)]
        if int(''.join(a)) > 2000:
            print(i)
            break

