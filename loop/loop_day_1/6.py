from math import sqrt
from turtle import *


tracer(0)
k = 23
# up()
# goto(-k * 2, -k * 2)
# down()
right(60)
for i in range(2):
    forward(10 * k)
    right(120)
    forward(5 * k)
    right(240)
right(120)
forward(3 * k)
right(90)
forward(20 * sqrt(3) * k)
right(90)
forward(8 * k)
right(120)
for i in range(2):
    forward(10 * k)
    left(120)
    forward(5 * k)
    left(240)
up()
goto(-k * 5, -k * 5)
for x in range(-20 * k, 20 * k, k):
    for y in range(-20 * k, 20 * k, k):
        goto(x, y)
        dot(4)
update()
mainloop()
