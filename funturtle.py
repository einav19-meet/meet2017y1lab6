import turtle



# turtle.shape('square')
# einav = turtle.clone()
# einav.shape('classic')
# einav.goto(100,100)
# einav.stamp()
# einav.goto(0,100)
# turtle.goto(-100,0)
# turtle.stamp()
# turtle.goto(0,100)

'''

creat a turtle in the shap of square
creat einav using clone in the shap of a traingle
i want u to draw a square using the turtle
i want u to draw a triangle using einav
'''
turtle.shape('square')
einav = turtle.clone()
einav.shape('triangle')
turtle.goto(0,100)
turtle.goto(100,100)
turtle.goto(100,0)
turtle.goto(0,0)
einav.goto(0,100)
einav.goto(50,150)
einav.goto(100,100)


turtle.mainloop()
