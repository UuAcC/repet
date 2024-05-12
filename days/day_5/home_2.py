# ---------------------------------------------------------------------------------------------------------------- 15814

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (x == (w or y)) or ((w <= z) and (y <= w))
#                 if not f:
#                     print(x, y, z, w)

# ---------------------------------------------------------------------------------------------------------------- 55619

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f1 = (x or (not y)) == (z <= w)
#                 f2 = ((not x) == y) and (z <= w)
#                 print(x, y, z, w, int(f1), int(f2))

# ---------------------------------------------------------------------------------------------------------------- 17366

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = ((x and w) or (w and z)) == ((z <= y) and (y <= x))
#                 if f:
#                     print(x, y, z, w)

# ---------------------------------------------------------------------------------------------------------------- 47206

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not(y <= x)) or (z <= w) or (not z)
                if not f:
                    print(x, y, z, w)