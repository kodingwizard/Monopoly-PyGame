import turtle as t
from random import random
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
for i in range(4):
   run = run + 1
   #t.up()
   t.goto(-455,300-(width*run))\
   #t.down()
   t.forward(70)
'''
#t.forward(70)
#t.up()
t.goto(-455, 265)
t.down()
t.forward(70)
t.up()
t.goto(-455, 230)
t.down()
t.forward(70)
t.up()
t.goto(-455, 195)
t.down()
t.forward(70)
'''
t.mainloop()