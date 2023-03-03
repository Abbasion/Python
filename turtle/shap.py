from turtle import *

title("Maaz KM")
setup(width=750,height=650)
tracer(2)
pensize()
bgcolor("black")
delay(0)
sides = 3
colors = ["blue","yellow","red"]

for i in range(500):
    color(colors[i % len(colors)])
    fd(i*3//sides+1)
    lt(210/sides+1)
    width(i*sides/230)
    fd(i*1//sides+1)
    lt(510/sides+1)
    width(i*sides/230)

done()