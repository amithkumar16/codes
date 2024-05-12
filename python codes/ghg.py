import turtle
s = turtle.Turtle()
turtle.bgcolor("white")
s.color("red")
s.speed(10)
s.width(2)  
def draw_heart():
    for _ in range(2):
        s.circle(-90, 90)
        s.circle(-20, 180)
    s.circle(-90, 90)


s.penup()
s.goto(0, 100)  # Adjust the starting position
s.pendown()
s.left(140)
s.begin_fill()
draw_heart()
s.end_fill()
s.hideturtle()
s.penup()
s.goto(0, -200)
s.color("black")
s.write("I love you", align="center", font=("Arial", 30, "bold"))
