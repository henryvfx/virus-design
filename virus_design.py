from turtle import speed, color, bgcolor, left, forward, exitonclick
speed(100)
color("green")
bgcolor("black")
b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1
exitonclick()
