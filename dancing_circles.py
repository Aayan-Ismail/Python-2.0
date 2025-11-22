import time
import random
import turtle
# import simpleaudio as sa

turtle.colormode(255)

pen = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("black")

pen.speed(0)

def circle():
    pen.penup()
    pen.goto(random.randint(-200,200), random.randint(-200,200))
    pen.color(
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255),
    )
    pen.begin_fill()
    pen.pendown()
    pen.circle(random.randint(20,70))
    pen.penup()
    pen.end_fill()
    pen.hideturtle()

def square():
    pen.penup()
    pen.goto(random.randint(-200,200), random.randint(-200,200))
    pen.color(
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255),
    )
    pen.pendown()

    square_size = random.randint(20,100)
    
    pen.begin_fill()
    for i in range(4):
        pen.forward(square_size)
        pen.right(90)
    pen.end_fill()


start_time = time.time()

for i in range(5):
    circle()
    time.sleep(1)
    pen.clear()
    square()
    time.sleep(1)
    pen.clear()

end_time = time.time()

elapsed_time = round(end_time - start_time,2)

pen.penup()

pen.goto(0,0)
pen.pencolor("red")
pen.pendown()
pen.write("Total animation time: {} seconds".format(elapsed_time),
    align="center",
    font=("Arial", 16, "bold"))



# soundfile = sa.WaveObject.from_wave_file("")
# soundfile.play()


turtle.done()


    



