import turtle
import random
turtle.speed(0)
a=random.randint(3,6)
b=random.randint(21,99)
c=list()
p=list()



turtle.penup()
turtle.setx(-1000)
turtle.sety(-200)
turtle.pendown()
turtle.setx(11000)
turtle.sety(-200)

turtle.penup()
turtle.setx(-400)
turtle.sety(-350)
turtle.pendown()

for i in range(8):
    turtle.penup()
    turtle.setx(-400+100*i)
    turtle.sety(-350)
    turtle.pendown()
    for k in range(4):
        turtle.fd(100)
        turtle.lt(90)
    turtle.penup()
    turtle.setx(-380 + 100 * i)
    turtle.sety(-330)
    d = random.randint(1,b)
    turtle.write((d), font=('Arial', 50, 'normal'))
    turtle.pendown()
    c.append(d)
print(c)

print(a)


def click_card(x, y):
    for l in range(8):
        if -400+(l*100) <x<-300+(l*100) and -350<y<-250:
            if len(p) < a:
                p.append(c[l])
                print(p)
                break
    if len(p)==a:
        for x in range(a):
            turtle.penup()
            turtle.setx(-400+(100*x))
            turtle.sety(-150)
            turtle.pendown()
            for kl in range(4):
                turtle.fd(100)
                turtle.lt(90)
            turtle.penup()
            turtle.setx(-380 + 100 * x)
            turtle.sety(-130)
            turtle.write((p[x]), font=('Arial', 50, 'normal'))
            turtle.pendown()





turtle.onscreenclick(click_card)



turtle.penup()
turtle.setx(-400)
turtle.sety(-150)
turtle.pendown()





















turtle.done()
