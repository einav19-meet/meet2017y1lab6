import turtle
turtle.shape("turtle")
square = turtle.clone()
square.shape("square")
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(50,0)
turtle.goto(50,50)
turtle.goto(0,50)
turtle.goto(0,0)
turtle.clone('classic')


turtle.mainloop()
