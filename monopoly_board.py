import turtle as t
from random import random
t.speed(0)
t.up()
t.goto(-455, -455)
t.down()
t.goto(455, -455)
t.goto(455, 455)
t.goto(-455, 455)
t.goto(-455, -455)
#for i in range(4):
#    t.forward(500)
#    t.left(90)
width = 70
run = 0
t.goto(-455, 315)
t.forward(140)
for i in range(9):
   run = run + 1
   t.up()
   t.goto(-455,315-(width*run))
   t.down()
   t.forward(140)
t.up()
t.goto(455, 315)
t.down()
t.forward(-140)
run = 0
for i in range(9):
   run = run + 1
   t.up()
   t.goto(455,315-(width*run))
   t.down()
   t.forward(-140)
t.up()
t.goto(-315, 455)
t.down()
t.left(-90)
t.forward(140)
run = 0
for i in range(9):
   run = run + 1
   t.up()
   t.goto(-315+(width*run), 455)
   t.down()
   t.forward(140)
t.up()
t.goto(-315, -455)
t.down()
t.left(180)
t.forward(140)
run = 0
for i in range(9):
   run = run + 1
   t.up()
   t.goto(-315+(width*run), -455)
   t.down()
   t.forward(140)
t.up()
t.goto(-315, 315)
t.down()
for i in range(4):
   t.left(-90)
   t.forward(630)
t.up()

#background square
t.goto(0,0)
t.shape("square")
t.shapesize(31,31)
t.fillcolor("turquoise")

t.clone()
#chance cards area on board
t.goto(190, -190)
t.shape("square")
t.shapesize(10,5)
t.tilt(-135)
t.fillcolor("orange")

t.up()
t.clone()
#community chest area on board
t.goto(-190, 190)
t.shape("square")
t.shapesize(10,5)
t.tilt(0)
t.fillcolor("skyblue")

#center banner
t.shape("monopoly-center.gif")


t.mainloop()