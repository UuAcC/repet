# ---------------------------------------------------------------------------------------------------------------- 59729
# f = open('59729.txt')
# s = f.readline()[:-1]
#
# a = []
# for i in range(1, len(s)):
#     if s[i - 1] + s[i] == 'TT':
#         a.append(i)
# min_len = 10 ** 8
# for i in range(149, len(a)):
#     min_len = min(min_len, a[i] - a[i - 149] + 2)
# print(min_len)

# ---------------------------------------------------------------------------------------------------------------- 59817

# f = open('59817.txt')
# s = f.readline()
# s = s.replace('B', 'A')
# s = s.replace('C', 'A')
# max_len = 0
# last = 0
# for i in range(1, len(s)):
#     if s[i - 1] + s[i] == 'AA':
#         max_len = max(max_len, i - last)
#         last = i
# max_len = max(max_len, len(s) - last)
# print(max_len)

# ---------------------------------------------------------------------------------------------------------------- 48472
f = open('59817.txt')
s = f.readline()
s = s.replace('O', 'A')
s = s.replace('D', 'C')
s = s.replace('F', 'C')
s = s.replace('AAC', '1')
for k in range(1, 1000000000):
    if '1' * k not in s:
        print(k)
        break

