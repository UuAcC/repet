# ---------------------------------------------------------------------------------------------------------------- 63076

# # ---------- A ----------
# f = open('63076-A.txt')
#
# k = int(f.readline())
# n = int(f.readline())
# a = [int(s) for s in f]
#
# ans = -(10 * 8)
# for i in range(n - 2 * k):
#     ans = max(ans, a[i] + a[i + 2 * k] + max(a[i + 1:i + 2 * k]))
# print(ans)
#
# # ---------- B ----------
# from time import time
# f = open('63076-B.txt')
# st = time()
# k = int(f.readline())
# n = int(f.readline())
# a = [int(s) for s in f]
# b = []
# ans = -(10 * 8)
# for i in range(n):
#     b.append([a[i], i])
# b.sort(reverse=True)
# ans = -(10 ** 8)
# for i in range(n - 2 * k):
#     j = i + 2 * k
#     for m in range(n):
#         if b[m][1] != i and b[m][1] != j:
#             ans = max(ans, a[i] + a[j] + b[m][0])
#             break
# print(ans, time() - st)

# ---------------------------------------------------------------------------------------------------------------- 63043

# # ---------- A ----------
# f = open('63043-A.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(x) for x in f]
# ans = -(10 ** 10)
# for i in range(n - 3 * k):
#     ans = max(ans, a[i] + a[i + 3 * k] + max(a[i + 1: i + 3 * k]))
# print(ans)
#
# # ---------- B ----------
# f = open('63043-B.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(x) for x in f]
# ans = -(10 ** 10)
# s = [(a[i] + a[i + 3 * k], i, i + 3 * k) for i in range(n - 3 * k)]
# s.sort(reverse=True)
# for i in range(n):
#     for j in s:
#         if i != j[1] and i != j[2]:
#             ans = max(ans, a[i] + j[0])
#             break
# print(ans)

# ---------------------------------------------------------------------------------------------------------------- 61373

# ---------- A/B ----------
# c = open('61373-A.txt')
# d = open('61373-B.txt')
# for f in [c, d]:
#     k = int(f.readline())
#     n = int(f.readline())
#     a = [int(x) for x in f]
#     ans = -(10 ** 10)
#     s = [(a[i] + a[i + 3 * k], i, i + 3 * k) for i in range(n - 3 * k)]
#     s.sort(reverse=True)
#     for i in range(n):
#         for j in s:
#             if i != j[1] and j[2] != i:
#                 ans = max(ans, a[i] + j[0])
#                 break
# print(ans)

# ---------------------------------------------------------------------------------------------------------------- 60269

# # ---------- A ----------
#
# f = open('60269-A.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(x) for x in f]
# ans = -(10 ** 8)
# for i in range(n):
#     for j in range(i + k, n):
#         for m in range(j + k, n):
#             ans = max(ans, a[i] + a[j] + a[m])
# print(ans)
#
# # ---------- B ----------
#
# f = open('60269-B.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(x) for x in f]
# maxl = [0] * n
# maxl[0] = a[0]
# for i in range(1, n):
#     maxl[i] = max(maxl[i - 1], a[i])
# maxr = [0] * n
# maxr[-1] = a[-1]
# for i in range(n - 2, -1, -1):
#     maxr[i] = max(maxr[i + 1], a[i])
# ans = -(10 ** 8)
# for j in range(n):
#     i = j - k
#     m = j + k
#     if i >= 0 and m < n:
#         ans = max(ans, a[j] + maxl[i] + maxr[m])
# print(ans)

# ---------------------------------------------------------------------------------------------------------------- 59855

# for e in ['A', 'B']:
#     f = open(f'59855-{e}.txt')
#     k = int(f.readline())
#     n = int(f.readline())
#     a = [int(x) for x in f]
#     res = 10 ** 8
#     minn = 10 ** 8
#     for i in range(n):
#         minn = min(minn, a[i])
#         if i + k < n:
#             res = min(res, minn * a[i + k])
#     print(res)

# ---------------------------------------------------------------------------------------------------------------- 59826

# for e in ['A', 'B']:
#     f = open(f'59826-{e}.txt')
#     k = int(f.readline())
#     n = int(f.readline())
#     a = [int(x) for x in f]
#     res = -(10 ** 8)
#     maxn = -(10 ** 8)
#     for i in range(n):
#         maxn = max(maxn, a[i])
#         if i + k < n:
#             res = max(res, maxn * a[i + k])
#     print(res)

# ---------------------------------------------------------------------------------------------------------------- 45261

# ---------- A ----------

# f = open('45261-A.txt')
# n = int(f.readline())
# a = [int(x) for x in f]
#
# ans = 10 ** 15
# for i in range(n):
#     res = 0
#     for j in range(n):
#         if j < i:
#             res += min(i - j, j + n - i) * 3 * a[j]
#         else:
#             res += min(j - i, i - j + n) * 3 * a[j]
#     ans = min(ans, res)
# print(ans)

# ---------- B ----------

f = open('45261-B.txt')
n = int(f.readline())
a = [int(s) * 3 for s in f]
b = a + a + a
ans = 0
s = [0] * (3 * n)
s[0] = b[0]
for i in range(1, 3 * n):
    s[i] = s[i - 1] + b[i]

for i in range(n // 2 + 1):
    ans += i * b[n + i]
for i in range((n + 1) // 2 + 1):
    ans += i * b[n - i]

prev = ans
for i in range(n + 1, 2 * n):
    res = prev
    res -= (n - 1) // 2 * b[i - (n - 1) // 2 - 1]
    res += n // 2 * b[i * n // 2]

# # a = [(int(x) * 3) for x in f]
# # res = [0 for i in range(n)]
# # prom_res = 0
# # leftSum = 0
# # rightSum = 0
# # for i in range(1, n // 2):
# #     prom_res += (a[i] * i + a[n - i] * i)
# #     leftSum += a[n - i]
# #     rightSum += a[i]
# # prom_res += (a[n // 2] * (n // 2))
# # res[0] = prom_res
# # for i in range(1, n):
# #     res[i] = res[i - 1] + leftSum + a[i - 1] - rightSum - a[(i + n // 2 + 1) % n]
# #     rightSum = rightSum + a[(i + n // 2 - 1) % n] - a[i]
# #     leftSum = leftSum - a[(i + n // 2) % n] + a[i - 1]
# # print(min(res))

# ---------------------------------------------------------------------------------------------------------------- 61407

# for e in ['A', 'B']:
#     f = open(f'61407-{e}.txt')
#     k = int(f.readline())
#     n = int(f.readline())
#     a = [int(x) for x in f]
#     ans = -(10 ** 8)
#     maxr = [0] * n
#     maxr[-1] = a[-1]
#     for i in range(n - 2, -1, -1):
#         maxr[i] = max(maxr[i + 1], a[i])
#     maxl = [0] * n
#     maxl[0] = a[0]
#     for i in range(1, n):
#         maxl[i] = max(maxl[i - 1], a[i])
#     for i in range(n - 2 * k):
#         j = i + 2 * k
#         if j < n:
#             ans = max(ans, a[i] + maxr[j] + maxl[-1])
#     print(ans)

# ---------------------------------------------------------------------------------------------------------------- 59854

# for e in ['A', 'B']:
#     f = open(f'59854-{e}.txt')
#     k = int(f.readline())
#     n = int(f.readline())
#     a = [int(x) for x in f]
#     res = -(10 ** 8)
#     maxr = [0] * n
#     maxr[-1] = a[-1]
#     for i in range(n - 2, -1, -1):
#         maxr[i] = max(maxr[i + 1], a[i])
#     for i in range(n - k):
#         j = i + k
#         if j < n:
#             res = max(res, a[i] + maxr[j])
#     print(res)

# ---------------------------------------------------------------------------------------------------------------- 59825

# for e in ['A', 'B']:
#     f = open(f'59825-{e}.txt')
#     k = int(f.readline())
#     n = int(f.readline())
#     a = [int(x) for x in f]
#     res = -(10 ** 8)
#     maxr = [0] * n
#     maxr[-1] = a[-1]
#     for i in range(n - 2, -1, -1):
#         maxr[i] = max(maxr[i + 1], a[i])
#     for i in range(n - 2 * k):
#         j = i + 2 * k
#         if j < n:
#             res = max(res, a[i] + maxr[j] + maxr[0])
#     print(res)
