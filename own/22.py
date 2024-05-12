# ---------------------------------------------------------------------------------------------------------------- 59815

# f = open('59815.txt')
# d = dict()
# d[0] = 0
# matrix = [x for x in f]
# fl = True
# while fl:
#     fl = False
#     for s in matrix:
#         ID, T, *a = [int(x) for x in s.split()]
#         if ID in d:
#             continue
#         flag = True
#         start = 0
#         for x in a:
#             if x in d:
#                 start = max(d[x], start)
#             else:
#                 flag = False
#                 break
#         if flag:
#             d[ID] = start + T
#             fl = True
# print(max(d.values()))

# ---------------------------------------------------------------------------------------------------------------- 59788

f = open('59788.txt')
d = dict()
d[0] = 0
matrix = [s for s in f]
flag = True
while flag:
    flag = False
    for s in matrix:
        ID, T, *a = [int(x) for x in s.split()]
        if ID in d:
            continue
        fl = True
        start = 0
        for x in a:
            if x not in d:
                fl = False
                break
            start = max(start, d[x])
        if fl:
            d[ID] = start + T
            flag = True
print(max(d.values()))
