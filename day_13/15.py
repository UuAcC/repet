# for A in range(64):
#     flag = True
#     for x in range(64):
#         f1 = (x & 28) != 0
#         f2 = (x & 45) != 0
#         f3 = (x & 17) == 0
#         f4 = (x & A) != 0
#         f = (f1 or f2) <= (f3 <= f4)
#     if flag:
#         print(A)
#         break

# ---------------------------------------------------------------------------------------------------------------- 33187

for A in range(90, 0, -1):
    flag = True
    for x in range(1, 1000):
        f = (90 % A == 0) and ((x % A != 0) <= ((x % 15 == 0) <= (x % 20 != 0)))
        flag &= f
    if flag:
        print(A)
        break
