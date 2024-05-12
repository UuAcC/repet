from turtle import *

# ---------------------------------------------------------------------------------------------------------------- 58248

# tracer(0)
# k = 9
# up()
# forward(11 * k)
# down()
# left(90)
# right(180)
# forward(5 * k)
# right(90)
# forward(50 * k)
# right(90)
# forward(5 * k)
# right(180)
# for i in range(5):
#     circle(5 * k, -180)
#     right(180)
# up()
# for x in range(-40 * k, 40 * k, k):
#     for y in range(-20 * k, 20 * k, k):
#         goto(x, y)
#         dot(3)
# update()
# mainloop()

# ---------------------------------------------------------------------------------------------------------------- 47407

# tracer(0)
# k = 30
# left(90)
# for _ in range(4):
#     forward(8 * k)
#     right(90)
# for _ in range(3):
#     forward(12 * k)
#     right(120)
# up()
# for x in range(0, 20 * k, k):
#     for y in range(-10 * k, 20 * k, k):
#         goto(x, y)
#         dot(4)
# update()
# mainloop()

# ---------------------------------------------------------------------------------------------------------------- 55623

# for x in range(1, 100):
#     if (x * (x - 1) * 4 + (x - 1) ** 2) > 1500:
#         print(x)
#         break

# ---------------------------------------------------------------------------------------------------------------- 59829

# tracer(0)
# k = 20
# left(90)
# for i in range(2):
#     forward(9 * k)
#     right(90)
#     forward(15 * k)
#     right(90)
# up()
# forward(12 * k)
# right(90)
# down()
# color('green')
# for i in range(2):
#     forward(6 * k)
#     right(90)
#     forward(12 * k)
#     right(90)
#
# up()
# for x in range(-5 * k, 20 * k, k):
#     for y in range(-5 * k, 20 * k, k):
#         goto(x, y)
#         dot(3, 'red')
# update()
# mainloop()

# ---------------------------------------------------------------------------------------------------------------- 47249

tracer(0)
k = 30
left(90)
for i in range(6):
    forward(13 * k)
    right(120)
up()
for x in range(-5 * k, 20 * k, k):
    for y in range(-5 * k, 20 * k, k):
        goto(x, y)
        dot(3, 'red')
update()
mainloop()
