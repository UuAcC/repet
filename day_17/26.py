# ---------------------------------------------------------------------------------------------------------------- 60967

# f = open('60967.txt')
# n = int(f.readline())
# k = int(f.readline())
# containers = []
# detail = []
# for i in range(n):
#     detail.append(int(f.readline()))
# for i in range(k):
#     containers.append(int(f.readline()))
# ans = 0
# cnt = 0
# for x in detail:
#     for j in range(k):
#         if containers[j] >= x:
#             containers[j] -= x
#             ans += x
#             cnt += 1
#             break
# print(ans, cnt)

# ---------------------------------------------------------------------------------------------------------------- 60268

# f = open('60268.txt')
# n = int(f.readline())
# a = []
# for i in range(n):
#     st, fin = [int(x) for x in f.readline().split()]
#     b = [fin, st]
#     a.append(b)
# a.sort()
# cnt = 0
# last = 0
# times = []
# for i in range(n):
#     st = a[i][1]
#     fin = a[i][0]
#     if st >= last:
#         times.append(fin)
#         cnt += 1
#         last = fin
# t = times[-2]
# m = 0
# for i in range(n):
#     if a[i][1] >= t:
#         m = max(m, a[i][1] - t)
# print(cnt, m)

# ---------------------------------------------------------------------------------------------------------------- 57433

# f = open('57433.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = []
# containers = [0] * k
# for i in range(n):
#     st, fin = [int(x) for x in f.readline().split()]
#     b = [fin, st]
#     a.append(b)
# a.sort()
# cnt = 0
# last = 0
# res = 0
# for i in range(n):
#     st = a[i][1]
#     fin = a[i][0]
#     for j in range(k):
#         if containers[j] <= st:
#             containers[j] = fin + 1
#             cnt += 1
#             if last <= st:
#                 last = st
#                 res = j + 1
#             break
# print(cnt, res)
# я не понимаю, почему это не работает

# ---------------------------------------------------------------------------------------------------------------- 63075

# f = open('63075.txt')
# n = int(f.readline())
# a = []
# win_1 = []
# win_2 = []
# cnt = 0
# gone = 0
# for i in range(n):
#     a.append([int(x) for x in f.readline().split()])
# a.sort()
# for x in a:
#     came_in = x[0]
#     time = x[1]
#     win = x[2]
#     while len(win_1) > 0 and win_1[0] <= came_in:
#         del win_1[0]
#     while len(win_2) > 0 and win_2[0] <= came_in:
#         del win_2[0]
#     if win == 1 or (win == 0 and len(win_1) <= len(win_2)):
#         if not win_1:
#             win_1.append(came_in + time)
#         elif len(win_1) < 14:
#             win_1.append(win_1[-1] + time)
#         else:
#             gone += 1
#     else:
#         if not win_2:
#             cnt += 1
#             win_2.append(came_in + time)
#         elif len(win_2) < 14:
#             cnt += 1
#             win_2.append(win_2[-1] + time)
#         else:
#             gone += 1
# print(cnt, gone)

# ---------------------------------------------------------------------------------------------------------------- 61406

# f = open('61406.txt')
# n = int(f.readline())
# a = []
# for i in range(n):
#     st, fin = [int(x) for x in f.readline().split()]
#     if fin + 20 > 1440:
#         a.append([1440, st])
#     else:
#         a.append([fin + 20, st])
# a.sort()
# cnt = 0
# last = 0
# times = []
# for x in a:
#     st = x[1]
#     fin = x[0]
#     if last <= st:
#         cnt += 1
#         times.append(fin)
#         last = fin
# t = times[-2]
# m = 0
# for x in a:
#     if x[1] >= t:
#         m = max(m, x[1] - t + 20)
# print(cnt, m)

# ---------------------------------------------------------------------------------------------------------------- 63042

# f = open('63042.txt')
# n = int(f.readline())
# a = []
# for i in range(n):
#     a.append([int(x) for x in f.readline().split()])
# a.sort()
# cnt = 0
# gone = 0
# win_1 = []
# win_2 = []
# for x in a:
#     came_in = x[0]
#     time = x[1]
#     win = x[2]
#     while len(win_1) > 0 and win_1[0] <= came_in:
#         del win_1[0]
#     while len(win_2) > 0 and win_2[0] <= came_in:
#         del win_2[0]
#     if win == 1 or (win == 0 and len(win_1) <= len(win_2)):
#         if not win_1:
#             win_1.append(came_in + time)
#             cnt += 1
#         elif len(win_1) < 12:
#             win_1.append(win_1[-1] + time)
#             cnt += 1
#         else:
#             gone += 1
#     else:
#         if not win_2:
#             win_2.append(came_in + time)
#         elif len(win_2) < 12:
#             win_2.append(win_2[-1] + time)
#         else:
#             gone += 1
# print(cnt, gone)

# ---------------------------------------------------------------------------------------------------------------- 61372

# f = open('61372.txt')
# n = int(f.readline())
# a = []
# for i in range(n):
#     st, fin = [int(x) for x in f.readline().split()]
#     if fin + 15 >= 1440:
#         a.append([1440, st])
#     else:
#         a.append([fin + 15, st])
# a.sort()
# last = 0
# count = 0
# ts = []
# for x in a:
#     start = x[1]
#     finish = x[0]
#     if last <= start:
#         count += 1
#         last = finish
#         ts.append(finish)
# t = ts[-2]
# m = 0
# for x in a:
#     if x[1] >= t:
#         m = max(m, x[1] - t + 15)
# print(count, m)
