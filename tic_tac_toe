import turtle
turtle.speed(0)
turtle.penup()
turtle.setx(-300)
turtle.sety(-300)
turtle.pendown()
for x in range(4):
    turtle.fd(600)
    turtle.lt(90)
turtle.setx(-100)
turtle.sety(-300)
turtle.setx(-100)
turtle.sety(300)
turtle.setx(100)
turtle.sety(300)
turtle.setx(100)
turtle.sety(-300)
turtle.setx(300)
turtle.sety(-300)
turtle.setx(300)
turtle.sety(-100)
turtle.setx(-300)
turtle.sety(-100)
turtle.setx(-300)
turtle.sety(100)
turtle.setx(300)
turtle.sety(100)
b=0
a=[[0,0,0],[0,0,0],[0,0,0]]
def play(x, y):
    global b
    turtle.penup()
    global a
    c=b%2
    print(x, y)
    ax = -1
    ay = -1
    if c==0:
        if -300<x<-100:
            ay+=1
            turtle.setx(-200)
        if -100 < x < 100:
            ay+=2
            turtle.setx(0)
        if 100 < x < 300:
            ay+=3
            turtle.setx(200)
        if -300<y<-100:
            ax+=3
            turtle.sety(-300)
        if -100 < y < 100:
            ax+=2
            turtle.sety(-100)
        if 100 < y < 300:
            ax+=1
            turtle.sety(100)
        turtle.pendown()
        turtle.circle(100)
        turtle.penup()
        a[ax][ay]=1
        b+=1
    if c == 1:
        if -300<x<-100:
            ay+=1
            turtle.setx(-300)
        if -100 < x < 100:
            ay+=2
            turtle.setx(-100)
        if 100 < x < 300:
            ay+=3
            turtle.setx(100)
        if -300<y<-100:
            ax+=3
            turtle.sety(-300)
        if -100 < y < 100:
            ax+=2
            turtle.sety(-100)
        if 100 < y < 300:
            ax+=1
            turtle.sety(100)

        turtle.pendown()
        turtle.lt(45)
        turtle.fd(200*1.414)
        turtle.lt(135)
        turtle.fd(200)
        turtle.lt(135)
        turtle.fd(200*1.414)
        turtle.lt(45)
        turtle.penup()
        a[ax][ay]=2
        b+=1
    print(ax,ay)
    print(a)


turtle.onscreenclick(play)





turtle.done()
