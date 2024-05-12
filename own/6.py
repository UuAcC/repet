from turtle import *

# ---------------------------------------------------------------------------------------------------------------- 64891

# tracer(0)
# k = 20
# for _ in range(4):
#     for __ in range(4):
#         forward(6 * k)
#         right(90)
#     forward(10 * k)
#     right(90)
#     forward(3 * k)
# up()
# goto(-k * 5, -k * 5)
# for x in range(-20 * k, 20 * k, k):
#     for y in range(-20 * k, 20 * k, k):
#         goto(x, y)
#         dot(4)
# update()
# mainloop()

# ---------------------------------------------------------------------------------------------------------------- 63055

# tracer(0)
# k = 20
# for _ in range(4):
#     forward(12 * k)
#     right(90)
# for _ in range(5):
#     forward(4 * k)
#     right(45)
# up()
# goto(-k * 5, -k * 5)
# for x in range(-20 * k, 20 * k, k):
#     for y in range(-20 * k, 20 * k, k):
#         goto(x, y)
#         dot(4)
# update()
# mainloop()

# ---------------------------------------------------------------------------------------------------------------- 63022

# tracer(0)
# k = 25
# for _ in range(4):
#     forward(14 * k)
#     right(90)
# for _ in range(5):
#     forward(5 * k)
#     right(45)
# up()
# for x in range(-20 * k, 20 * k, k):
#     for y in range(-20 * k, 10 * k, k):
#         goto(x, y)
#         dot(4)
# update()
# mainloop()

# ---------------------------------------------------------------------------------------------------------------- 61386

# tracer(0)
# k = 20
# for _ in range(8):
#     right(45)
#     forward(k * 6)
# up()
# for x in range(-20 * k, 20 * k, k):
#     for y in range(-20 * k, 20 * k, k):
#         goto(x, y)
#         dot(4)
# update()
# mainloop()

# ---------------------------------------------------------------------------------------------------------------- 59829

# tracer(0)
# k = 20
# for _ in range(2):
#     forward(9 * k)
#     right(90)
#     forward(15 * k)
#     right(90)
# up()
# forward(12 * k)
# right(90)
# down()
# for _ in range(2):
#     forward(6 * k)
#     right(90)
#     forward(12 * k)
#     right(90)
# up()
# for x in range(-20 * k, 20 * k, k):
#     for y in range(-20 * k, 20 * k, k):
#         goto(x, y)
#         dot(4)
# update()
# mainloop()

# ---------------------------------------------------------------------------------------------------------------- 58249

# tracer(0)
# k = 30
# up()
# goto(-5 * k, -5 * k)
# down()
# for _ in range(4):
#     circle(5 * k, -180)
#     left(90)
# up()
# for x in range(-20 * k, 20 * k, k):
#     for y in range(-20 * k, 20 * k, k):
#         goto(x, y)
#         dot(4)
# update()
# mainloop()

# ---------------------------------------------------------------------------------------------------------------- 58248

tracer(0)
k = 15
up()
goto(20 * k, -5 * k)
down()
right(90)
forward(5 * k)
right(90)
forward(50 * k)
right(90)
forward(5 * k)
for _ in range(5):
    left(180)
    circle(5 * k, -180)
up()
for x in range(-40 * k, 30 * k, k):
    for y in range(-20 * k, 20 * k, k):
        goto(x, y)
        dot(2)
update()
mainloop()
