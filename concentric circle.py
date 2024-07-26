from turtle import *
s= Screen()
# s.setup(1000,500)
colors=['red','yellow']
pencolor('white')
pensize(5)
for i in range(6,0,-1):
    penup()
    setpos(10,-20*i)
    pendown()
    fillcolor(colors[i%2])
    begin_fill()
    circle(20*i)
    end_fill()
mainloop()


