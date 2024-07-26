from turtle import *
speed('fastest')
pensize(5)
pencolor('grey')
fillcolor('light blue')
for i in range(8,0,-1):
    begin_fill()
    circle(i*20)
    lt(25)
    end_fill()
mainloop()