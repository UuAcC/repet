from turtle import *
from time import sleep

# ---------------------------------------------------------------------------------------------------------------- 47210
# tracer(0)
# left(90)
# k = 40
# for i in range(7):
#     forward(10 * k)
#     right(120)
# up()
# for x in range(0 * k, 11 * k, k):
#     for y in range(0 * k, 11 * k, k):
#         goto(x, y)
#         dot(4)
# update()
# sleep(10)

# ---------------------------------------------------------------------------------------------------------------- 58249
tracer(0)
k = 30
up()
goto(-k * 2, -k * 2)
down()
for i in range(5):
    circle(5 * k, -180)
    left(90)
    circle(5 * k, -180)
    left(90)
    circle(5 * k, -180)
    left(90)
    circle(5 * k, -180)
    left(90)
up()
goto(-k * 5, -k * 5)
for x in range(-20 * k, 20 * k, k):
    for y in range(-20 * k, 20 * k, k):
        goto(x, y)
        dot(4)
update()
sleep(5)
