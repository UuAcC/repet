# ---------------------------------------------------------------------------------------------------------------- 15803

# d = 0
# for Al in range(-20, 21):
#     for Ar in range(Al + 1, 21):
#         flag = True
#         for x in range(-20, 21):
#             f = ((Al <= x <= Ar) <= (x ** 2 <= 100)) and ((x ** 2 <= 64) <= (Al <= x <= Ar))
#             flag &= f
#         if flag:
#             d = max(d, Ar - Al)
# print(d)

# ---------------------------------------------------------------------------------------------------------------- 16821

# for A in range(50):
#     flag = True
#     for x in range(128):
#         for y in range(128):
#             f = (3 * x + 4 * y != 70) or (A > x) or (A > y)
#             flag &= f
#     if flag:
#         print(A)
#         break

# ---------------------------------------------------------------------------------------------------------------- 18566

for A in range(64):
    flag = True
    for x in range(128):
        for y in range(128):
            f = (3 * x + 4 * y > 66) or (x <= A) or (y < A)
            flag &= f
    if flag:
        print(A)
        break
