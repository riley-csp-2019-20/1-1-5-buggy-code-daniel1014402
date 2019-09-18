#   a115_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
leg = 6
LoL = 70
SbL = 380 / leg
spider.pensize(5)
n = 0
while (n < leg):
  spider.goto(0,0)
  spider.setheading(SbL*n)
  spider.forward(LoL)
  n = n + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()