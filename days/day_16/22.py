# ---------------------------------------------------------------------------------------------------------------- 47226

# f = open('47226.txt')
# R = [0] * 13
# for s in f:
#     ID, T, *a = [int(x) for x in s.split()]
#     st = 0
#     for x in a:
#         st = max(st, R[x])
#     R[ID] = st + T
# print(max(R))

# ---------------------------------------------------------------------------------------------------------------- 59788

# f = open('59788.txt')
# R = [0] * 21
# a = []
# for s in f:
#     a.append([int(x) for x in s.split()])
# while R.count(0) > 1:
#     for b in a:
#         ID, T, c = b[0], b[1], b[2:]
#         if R[ID] > 0:
#             continue
#         if c[0] == 0:
#             R[ID] = T
#         flag = True
#         st = 0
#         for x in c:
#             if R[x] == 0:
#                 flag = False
#                 break
#             st = max(st, R[x])
#         if flag:
#             R[ID] = st + T
# print(max(R))

# ---------------------------------------------------------------------------------------------------------------- 47549

# f = open('47549.txt')
# R = [0] * 16
# for s in f:
#     ID, T, *a = [int(x) for x in s.split()]
#     start = 0
#     for x in a:
#         start = max(start, R[x])
#     R[ID] = start + T
# print(max(R))

# ---------------------------------------------------------------------------------------------------------------- 58489

# f = open('58489.txt')
# D = dict()
# res = 0
# D[0] = 0
# matrix = []
# for s in f:
#      matrix.append(s)
# fl = True
# while fl:
#     fl = False
#     for s in matrix:
#         ID, T, *a = [int(x) for x in s.split()]
#         if ID in D:
#             continue
#         flag = True
#         start = 0
#         for x in a:
#             if x not in D:
#                 flag = False
#                 break
#             start = max(start, D[x])
#         if start >= 80:
#             res += 1
#         if flag:
#             D[ID] = start + T
#             fl = True
# print(max(D.values()))
# print(res)

# ---------------------------------------------------------------------------------------------------------------- 51991

# f = open('51991.txt')
# D = dict()
# D[0] = 0
# res = 0
# matrix = [x for x in f]
# check = True
# while check:
#     check = False
#     for s in matrix:
#         ID, T, *a = [int(x) for x in s.split()]
#         if ID in D:
#             continue
#         flag = True
#         start = 0
#         for x in a:
#             if x not in D:
#                 flag = False
#                 break
#             start = max(start, D[x])
#         if flag:
#             D[ID] = start + T
#             check = True
#             if start + T <= 170:
#                 res += 1
# print(res)

# ---------------------------------------------------------------------------------------------------------------- 58530

# f = open('58530.txt')
# D = dict()
# D[0] = 0
# matrix = [x for x in f]
# res = 0
# check = True
# while check:
#     check = False
#     for s in matrix:
#         ID, T, *a = [int(x) for x in s.split()]
#         if ID in D:
#             continue
#         flag = True
#         start = 0
#         for x in a:
#             if x not in D:
#                 flag = False
#                 break
#             start = max(start, D[x])
#         if start > 100:
#             res += 1
#         if flag:
#             D[ID] = start + T
#             check = True
# print(res)

# ---------------------------------------------------------------------------------------------------------------- 48443

# f = open('48443.txt')
# D = dict()
# D[0] = 0
# matrix = [x for x in f]
# check = True
# while check:
#     check = False
#     for s in matrix:
#         ID, T, *a = [int(x) for x in s.split()]
#         if ID in D:
#             continue
#         flag = True
#         start = 0
#         for x in a:
#             if x not in D:
#                 flag = False
#                 break
#             start = max(start, D[x])
#         if flag:
#             D[ID] = start + T + 3
#             check = True
# print(max(D.values()) - 3)

# ---------------------------------------------------------------------------------------------------------------- 59815

f = open('59815.txt')
D = dict()
D[0] = 0
matrix = [x for x in f]
check = True
while check:
    check = False
    for s in matrix:
        ID, T, *a = [int(x) for x in s.split()]
        if ID in D:
            continue
        flag = True
        start = 0
        for x in a:
            if x not in D:
                flag = False
                break
            start = max(start, D[x])
        if flag:
            D[ID] = start + T
            check = True
print(max(D.values()))
