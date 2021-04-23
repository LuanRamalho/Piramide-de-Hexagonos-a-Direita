import turtle

a = turtle.Screen()
turtle.speed(0)

def Hexágono(posx, posy, lado):
    turtle.showturtle()
    # posiciona
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    # desenha

    for i in range(6):
        turtle.forward(lado)
        turtle.left(60)
        turtle.hideturtle()

# Normal
def pir_direita(n,posx, posy,lado):
    for i in range(1,n+1):
        # desenha coluna i
        # -- posiciona
        turtle.penup()
        turtle.goto(posx+(n-i)*lado,posy + (n-i)*lado/2)
        turtle.pendown()
        # -- desenha
        for j in range(1,i+1):
            Hexágono(turtle.xcor(),turtle.ycor(), lado)
            turtle.sety(turtle.ycor()+lado)
            turtle.hideturtle()

Hexágono(-350, -300, 50)
pir_direita(10, -350, -300, 50)
a.exitonclick()