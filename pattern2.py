from turtle import *
speed('fastest')


# fd(5)
# lt(90)
# fd(10)
# lt(90)
# fd(15)
# lt(90)
# fd(20)
# lt(90)
# fd(25)
# lt(90)
# fd(30)
# lt(90)
# fd(35)
# lt(90)
# fd(40)
# lt(90)
# fd(45)
# lt(90)
# fd(50)
# lt(90)
# fd(55)
# lt(90)
# fd(60)
# lt(90)
# fd(65)
# lt(90)
# fd(70)
# lt(90)
# fd(75)
# lt(90)
# fd(80)
# lt(90)
# fd(85)
# lt(90)
# fd(90)
# lt(90)
# fd(100)
# lt(90)
# fd(105)
# lt(90)
# fd(110)
# lt(90)
# fd(115)
# lt(90)
# fd(120)
# lt(90)
# fd(125)
# lt(90)
# fd(130)
# lt(90)
# fd(135)
# lt(90)
# fd(140)               
# lt(90)
# fd(145)
# lt(90)
# fd(150)
# lt(90)
# fd(155)
# lt(90)
# fd(160)
# lt(90)
# fd(165)
# lt(90)
# fd(170)
# lt(90)

s=8
d=100
for i in range(s):
    fd(d)
    lt(360/s)
    write(i,font=('Arial',12,'normal'))
    circle(360/s,90)


pencolor('yellow')  
bgcolor('black')           
total=0
while total<500:
    total+=5
    fd(total)
    lt(90)

pencolor('blue')             
total=0
while total<500:
    total+=5
    fd(total)
    lt(59)
    



mainloop()

