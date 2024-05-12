# ---------------------------------------------------------------------------------------------------------------- 27421

# f = open('27421.txt')
# s = f.readline()
# maxi = 0
# curr = 0
# for i in range(1, 10**6):
#     if s[i] == s[i - 1]:
#         maxi = max(curr, maxi)
#         curr = 0
#     else:
#         curr += 1
# print(maxi + 1)

# ---------------------------------------------------------------------------------------------------------------- 27686

# f = open('27686.txt')
# s = f.readline()
# s = s.replace('X', '1')
# s = s.replace('Y', ' ')
# s = s.replace('Z', ' ')
# print(len(max(s.split())))

# ---------------------------------------------------------------------------------------------------------------- 59791

# f = open('59791.txt')
# s = f.readline()
# a = []
# for i in range(len(s)):
#     if s[i] == 'W':
#         a.append(i)
# minimum = 10 ** 6
# for i in range(129, len(a)):
#     minimum = min(minimum, a[i] - a[i - 129] + 1)
# print(minimum)

# ---------------------------------------------------------------------------------------------------------------- 29672

# f = open('29672.txt')
# s = f.readlines()
# count = 0
# for line in s:
#     if line.count('E') > line.count('A'):
#         count += 1
# print(count)

# ---------------------------------------------------------------------------------------------------------------- 33494

# f = open('33494.txt')
# s = f.readline()
# a = []
# maxi = 0
# for i in range(len(s) - 1):
#     if s[i] == 'E':
#         a.append(s[i + 1])
# for char in list(set(a)):
#     if a.count(char) > maxi:
#         maxi = a.count(char)
#         res = char
# print(res)

# ---------------------------------------------------------------------------------------------------------------- 51993

# s = open('51993.txt').readline().split('F')
# mx = 0
# count = 1
# for i in range(len(s)):
#     if s[i].count('A') <= 2:
#         count += len(s[i]) + 1
#         mx = max(mx, count)
#     else:
#         count = 1
# print(mx)

# ---------------------------------------------------------------------------------------------------------------- 55611

# s = open('55611.txt').readlines()
# a = []
# mxr = 0
# for x in s:
#     r = []
#     for i in range(len(x)):
#         if x[i] == 'A':
#             r.append(x[i + 1])
#     mx = 0
#     for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#         mx = max(mx, r.count(c))
#     for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#         if r.count(c) == mx:
#             a.append(c)
# for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#     mxr = max(mxr, a.count(c))
# print(mxr)

# ---------------------------------------------------------------------------------------------------------------- 56552

# f = open('56552.txt')
# mx = -1
# mx_all = -1
# for s in f:
#     k = 1
#     for i in range(len(s) - 1):
#         if s[i] == s[i + 1]:
#             k += 1
#             if k > mx:
#                 mx = k
#                 mx_all = s.count(s[i])
#             if k == mx:
#                 mx_all = min(s.count(s[i]), mx_all)
#         else:
#             k = 1
# print(mx_all)

# ---------------------------------------------------------------------------------------------------------------- 58491

f = open('58491.txt')
s = f.readline()
a = ['0'] * len(s)
for i in range(2, len(s)):
    t = s[i - 2:i + 1]
    if ('A' in t) and ('B' in t) and ('C' in t):
        a[i - 2] = '1'
        a[i - 1] = '1'
        a[i] = '1'
print(len(max(''.join(a).split('1'))))
