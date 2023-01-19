import turtle
import time

turtle.title("PaperMindVention")
turtle.speed(5)

turtle.getturtle()
turtle.resizemode("small")
turtle.shape("turtle")
t=turtle
t.up()
a = t.clone()
b = t.clone()
c = t.clone()
d = t.clone()
e = t.clone()

a.left(90)
c.right(60)
d.right(120)
e.right(180)

a.forward(100)
b.forward(100)
c.forward(100)
d.forward(100)
e.forward(100)

a.down()
b.down()
c.down()
d.down()
e.down()

a.begin_fill()
b.begin_fill()
c.begin_fill()
d.begin_fill()
e.begin_fill()

a.color('red')
b.color('green')
c.color('blue')
d.color('red')
e.color('green')
for x in range(0,12):
    a.right(45)
    b.right(45)
    c.right(45)
    d.right(45)
    e.right(45)
    a.forward(10)
    b.forward(10)
    c.forward(10)
    d.forward(10)
    e.forward(10)
    pass
a.end_fill()
b.end_fill()
c.end_fill()
d.end_fill()
e.end_fill()

a.forward(70)
b.forward(50)
c.forward(50)
d.forward(50)
e.forward(70)

a.left(70)
b.left(90)
c.left(90)
d.left(90)
e.left(70)

a.forward(70)
b.forward(50)
c.forward(50)
d.forward(50)
e.forward(70)

time.sleep(3)

for x in range(0,170):
    a.undo()
    b.undo()
    c.undo()
    d.undo()
    e.undo()
    time.sleep(0.3)
    pass

turtle.mainloop()