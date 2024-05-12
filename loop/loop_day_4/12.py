s = 47 * '7'
while ('2222' in s) or ('7777' in s):
    if '2222' in s:
        s = s.replace('2222', '77', 1)
    elif '7777' in s:
        s = s.replace('7777', '22', 1)
print(s)