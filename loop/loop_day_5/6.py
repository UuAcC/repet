from turtle import *


tracer(0)
k = 10
up()
right(270)
forward(35 * k)
right(270)
forward(5 * k)
right(180)
down()
for i in range(2):
    forward(53 * k)
    right(90)
    forward(38 * k)
    right(90)
up()
right(90)
forward(k)
right(90)
forward(2 * k)
right(270)
down()
for i in range(2):
    forward(83 * k)
    left(90)
    forward(53 * k)
    left(90)
up()
for x in range(-30 * k, 80 * k, k):
    for y in range(-50 * k, 80 * k, k):
        goto(x, y)
        dot(3)
update()
mainloop()