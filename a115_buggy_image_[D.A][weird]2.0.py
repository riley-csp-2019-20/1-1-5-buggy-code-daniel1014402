#   a115_buggy_image.py
import turtle as trtl
# spider body
#spider head
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
#spider legs
leg = 8
LoL = 100
AbL = 220 / leg
print("AbL=", AbL)
spider.pensize(5)
NL = 0
while (NL < leg):
  spider.goto(0,0)
  spider.setheading(AbL*NL)
  spider.forward(LoL)
  NL = NL + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()