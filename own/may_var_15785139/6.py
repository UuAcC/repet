from turtle import *

tracer(0)
k = 30
for _ in range(10):
    forward(5 * k)
    right(60)
up()
for x in range(-20 * k, 20 * k, k):
    for y in range(-20 * k, 20 * k, k):
        goto(x, y)
        dot(4)
update()
mainloop()