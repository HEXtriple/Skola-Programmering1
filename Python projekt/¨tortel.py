import turtle as t
import random as rand

p1 = t.Turtle()
p1.color('red')
p1.shape('turtle')
p1.penup()
p1.goto(-160, 100)
p1.pendown()

p2 = t.Turtle()
p2.color('blue')
p2.shape('turtle')
p2.penup()
p2.goto(-160, 70)
p2.pendown()

p3 = t.Turtle()
p3.color('purple')
p3.shape('turtle')
p3.penup()
p3.goto(-160, 40)
p3.pendown()

p4 = t.Turtle()
p4.color('green')
p4.shape('turtle')
p4.penup()
p4.goto(-160, 10)
p4.pendown()

kvadrat = t.Turtle()
kvadrat.color('yellow')
kvadrat.shape('triangle')
kvadrat.penup()
kvadrat.goto(100, 100)

t.penup()
t.speed(1000)
t.hideturtle()
t.goto(-140, 140)
for i in range(0, 14):
    t.write(i, align='center')
    t.width(4)
    t.right(90)
    t.forward(10)
    t.pendown()
    t.forward(150)
    t.penup()
    t.backward(160)
    t.left(90)
    t.forward(20)


for i in range(100):
    p1.forward(rand.randint(1, 5))
    p2.forward(rand.randint(1, 5))
    p3.forward(rand.randint(1, 5))
    p4.forward(rand.randint(1, 5))

t.mainloop()


