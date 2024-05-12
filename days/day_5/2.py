# ------------------------------------------------------------------------------------------------------ first on lesson

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f1 = (x <= y <= w)
#                 f2 = (z == (x or y))
#                 f = f1 or f2
#                 if not f:
#                     print(x, y, z, w)

# ----------------------------------------------------------------------------------------------------- second on lesson

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (x and (not y)) or (y == z) or w
#                 if not f:
#                     print(x, y, z, w)

# ------------------------------------------------------------------------------------------------------ third on lesson

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (x or (not y)) and (y != z) and (not w)
#                 if f:
#                     print(x, y, z, w)

# ------------------------------------------------------------------------------------------------------ forth on lesson

print('x y z w f1 f2')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = (x <= y) == (w or not z)
                f2 = (x <= y) and (not w == z)
                print(x, y, z, w, int(f1), int(f2))
