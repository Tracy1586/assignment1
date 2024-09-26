from turtle import *

def draw_myown():
    speed(13)  # Painting speed control
    bgcolor("Dark blue")
    pensize(10)
    penup()
    goto(0, 50)
    pendown()
    circle(-120)
    penup()
    circle(-120, -60)
    pendown()
    right(50)
    circle(-120)
    penup()
    circle(-120, -60)
    pendown()
    right(50)
    circle(-120)
    penup()
    circle(-120, -60)

    done()


print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Please select what you want to draw:\n"
              " (1 for start drawing)\n")
    try:
        a = eval(a)
        if a == 1:
            draw_myown()


        else:
            print("Please input the value 1 to start drawing")
    except:
        print("Please input the value 1 to start drawing")



