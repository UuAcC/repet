# ---------- A ----------

# from time import time
# start = time()
# f = open('27-A.txt')
# n = int(f.readline())
# a = [0] * n
# b = [0] * n
# ans = 10 ** 8
# for i in range(n):
#     a[i], b[i] = [int(x) for x in f.readline().split()]
# for x in range(2 ** n):
#     s = bin(x)[2:]
#     while len(s) < n:
#         s = '0' + s
#     k0 = k1 = 0
#     res = 0
#     for i in range(n):
#         if s[i] == '0':
#             res += a[i]
#             if a[i] % 2 == 0:    # a[i] & 1 == 0 - альтернатива
#                 k0 += 1
#             else:
#                 k1 += 1
#         else:
#             res += b[i]
#             if b[i] % 2 == 0:
#                 k0 += 1
#             else:
#                 k1 += 1
#     if res % 2 == 1 and k1 > k0:
#         ans = min(ans, res)
#     elif res % 2 == 0 and k1 < k0:
#         ans = min(ans, res)
# print(ans)
# print(time() - start)

# ---------- B ----------

# f = open('27-B.txt')
# n = int(f.readline())
# a = [0] * n
# b = [0] * n
# ans = 0
# k0 = k1 = 0
# ch = []
# nech = []
# for i in range(n):
#     a[i], b[i] = [int(x) for x in f.readline().split()]
#     if a[i] < b[i]:
#         if a[i] % 2 == 0 and b[i] % 2 == 1:
#             ch.append(b[i] - a[i])
#         elif a[i] % 2 == 1 and b[i] % 2 == 0:
#             nech.append(b[i] - a[i])
#     if a[i] > b[i]:
#         if a[i] % 2 == 0 and b[i] % 2 == 1:
#             nech.append(a[i] - b[i])
#         elif a[i] % 2 == 1 and b[i] % 2 == 0:
#             ch.append(a[i] - b[i])
#     if a[i] < b[i]:
#         ans += a[i]
#         if a[i] % 2 == 1:
#             k1 += 1
#         else:
#             k0 += 1
#     else:
#         ans += b[i]
#         if b[i] % 2 == 1:
#             k1 += 1
#         else:
#             k0 += 1
# print(ans, k0, k1)
# ch.sort()
# nech.sort()
#
# print(ans + nech[0], ans + ch[0] + ch[1])
