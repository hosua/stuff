import turtle, math
import tkinter
from PIL import Image
pen = turtle.Turtle()
pen2 = turtle.Turtle()
screen = turtle.Screen()
screen.setup(1200,800)
screen.bgcolor("#006600")
def move_horizontal(t, distance):  # These functions will assume that turtle returns to its original orientation
    t.up()
    t.forward(distance)
    t.down()

def move_vertical(t, distance):
    t.up()
    t.right(-90)
    t.forward(distance)
    t.right(90)
    t.down()

def shape_maker(t, sides, length, c="#000000", fc="#FFFFFF"):
    t.color(c, fc)
    t.begin_fill()
    t.down()
    for i in range(sides):
        t.forward(length)
        t.left(360/sides)
    t.end_fill()

def rect(t, length, width, c="#FFFFFF",fc="#000000"):    # Note, width is not measured in pixels. Width is the multiple of length to get the actual width.
    t.color(c, fc)
    t.begin_fill()
    t.right(180)          # This draws a vertically standing rectangle for zero.
    t.forward(length)     # To draw a horizontal triangle, turn pen 90 degrees left or right before calling rect
    t.left(90)
    t.forward(length * width)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length * width)
    t.right(90)   # return to original orientation
    t.end_fill()

def roulette_wheel():
    #red_nums = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    #black_nums = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    pen.down()

    r = 200
    n = 37
    c_pos = []
    for i in range(n):  # get all circumference positions (inner circle)
        c_pos.append(pen.pos())
        pen.circle(r, extent=360/n)

    print(c_pos)
    pen.up()
    pen.left(90)
    pen.forward(r)
    # At center of circle here
    pen.right(90)
    center = pen.pos()
    pen.down()
    pen.up()
    pen.goto(center)
    for i in range(n):  # Slice circle n times

        if i % 2 == 0 and i != 0:
            col = "#FF0000" # red
        elif i % 2 != 0 and i != 0:
            col = "#000000" # black
        else:   # its 0
            col = "#006600" # green
        pen.color("#FFFFFF", col)
        pen.goto(c_pos[i])
        pen.down()  # drawing each block()
        pen.begin_fill()
        pen.circle(r, extent=360/n)
        pen.left(90)
        pen.forward(r * 1/4)
        pen.left(90)
        pen.circle(-r * 3/4, extent=360/n)
        pen.right(90)
        pen.forward(-r * 1/4)
        pen.right(90)   # end drawing of block and return to original orientation
        pen.end_fill()
        pen.left(360/n) # rotate per slice
    pen.up()
    pen.goto(center)
    pen.right(90)
    """
    # Draw inner circle
    inner_circle_r = (r - 1) * 3/4
    pen.forward(inner_circle_r)
    pen.left(90)
    pen.color("#FFFFFF", "#eab676")
    pen.begin_fill()
    pen.circle(inner_circle_r)
    pen.end_fill()
    pen.up()
    pen.left(90)
    pen.goto(center)
    # Move
    pen.right(180)
    pen.forward(1/7 * r)
    pen.left(90)    # Now facing 0 degrees
    """
    # Draw inner inner circle
    innermost_circle_r = 1 / 7 * r
    pen.forward(innermost_circle_r)
    pen.left(90)

    pen.color("#FFFFFF", "#873e23")
    pen.begin_fill()
    pen.circle(innermost_circle_r)
    pen.end_fill()
    pen.up()
    pen.left(90)
    pen.right(90)
    pen.left(360/n/2)
    # (order is listed counter clockwise)
    pen.goto(center)
    # Filling in numbers
    pen.right(90)
    wheel_order = [0, 26, 3, 35, 12, 28, 7, 29, 18, 22, 9, 31, 14, 20, 1, 33, 16, 24, 5, 10, 23, 8, 30, 11, 36, 13, 27,
                   6, 34, 17, 25, 2, 21, 4, 19, 15, 32]
    for i in range(11): # Lots of disgusting manual corrections done here because text alignment fucks everything up
        pen.forward(.9 * r)
        pen.down()
        pen.pencolor('#FFFFFF')
        pen.write(wheel_order[i], font=("courier", 8, 'bold'), align='right')
        pen.up()
        pen.goto(center)
        move_horizontal(pen, -5)
        pen.up()
        pen.left((360 / n))
    pen.right(3)
    for i in range(11, 24):
        if i == 11:
            pen.forward(9/10 * r)
        else:
            pen.forward((6 / 7) * r)
        pen.down()
        pen.pencolor('#FFFFFF')
        pen.write(wheel_order[i], font=("courier", 8, 'bold'), align='right')
        pen.up()
        pen.goto(center)
        pen.up()
        pen.left((360 / n))
    pen.left(3)
    for i in range(24, 29):
        pen.forward((7 / 8) * r)
        pen.down()
        pen.pencolor('#FFFFFF')
        pen.write(wheel_order[i], font=("courier", 8, 'bold'), align='right')
        pen.up()
        pen.goto(center)
        pen.up()
        pen.left((360 / n))
    pen.left(2.5)
    for i in range(29, 34):
        pen.forward((8/9) * r)
        pen.down()
        pen.pencolor('#FFFFFF')
        if len(str(i)) < 2: # if one digit
            pen.write(wheel_order[i], font=("courier", 8, 'bold'), align='right')
        else:
            pen.write(wheel_order[i], font=("courier", 8, 'bold'), align='left')
        pen.up()
        pen.goto(center)
        pen.up()
        pen.left((360 / n))
    for i in range(34, 37):
        pen.forward((8/9) * r)
        pen.down()
        pen.pencolor('#FFFFFF')
        if len(str(i)) < 2: # if one digit
            pen.write(wheel_order[i], font=("courier", 8, 'bold'), align='right')
        else:
            pen.write(wheel_order[i], font=("courier", 8, 'bold'), align='right')
        pen.up()
        pen.goto(center)
        pen.up()
        pen.left((360 / n))
def roulette_table():
    pen2.down()
    length = 50
    col = "#006600"  # Color 0 to green
    rect(pen2, length, 3, fc=col) # We use 3 here because the width of a box around 0 is equal to 3 lengths.
    move_vertical(pen2, -length * 3)
    move_horizontal(pen2, -length)
    def return_position(t, pos):
        t.up()
        t.goto(pos)
        t.down()

    case1_columns = [0,2,5,8,9,11] # case 1: columns [0,2,5,8,9,11] are all red -> black -> red going up
    case2_columns = [1,4,7,10]  # case 2: columns [1,4,7,10] are all black -> red -> black
    case3_columns = [3,6]   # case 3: columns [3,6] are all black -> black -> red
    for column in range(13):  # 12 columns   # 0,2,3,5,6,8,9,11 Red, 12 = green, rest are black.
        if column == 12:
            col = "#006600"  # Green

        move_horizontal(pen2, length)
        for i in range(3):
            if column in case1_columns: # red -> black -> red
                if i == 0 or i == 2:
                    col = "#FF0000"  # Red
                if i == 1:
                    col = "#000000"  # Black

            if column in case2_columns: # black -> red -> black
                if i == 0 or i == 2:
                    col = "#000000"  # Black
                if i == 1:
                    col = "#FF0000"  # Red

            if column in case3_columns: # black -> black -> red
                if i == 0 or i == 1:
                    col = "#000000"  # Black
                if i == 2:
                    col = "#FF0000"  # Red
            shape_maker(pen2, 4, length, "#FFFFFF", col)
            move_vertical(pen2, length)
        move_vertical(pen2, -length * 3)

    move_horizontal(pen2, -length * 8)
    pen2.right(90)
    pen2.forward(length)
    for i in range(3):  # Drawing (1-12), (13-24), and (25-36) blocks
        c = "#FFFFFF"
        f = "#006600"
        rect(pen2, length, 4, c, f)
        move_vertical(pen2, length * 4)
    pen2.left(90) # return to original orientation
    move_horizontal(pen2, -length * 14)
    move_vertical(pen2, -50)
    pen2.right(90) # changing orientation to draw horizontal rectangle
    for i in range(6):    # Bottom most row
        if i == 2:
            col = "#FF0000" # red
        elif i == 3:
            col = "#000000" # black
        else:
            col = "#006600" # green
        rect(pen2, length, 2, "#FFFFFF", col)
        move_vertical(pen2, length * 2)
    pen2.up()
    pen2.home()
    pen2.down()
    move_horizontal(pen2, -length * 2)  # This needs to be changed depending on where the turtle starts.
    move_horizontal(pen2, (length * 2.4))   # Needed to manually move crap here.
    move_vertical(pen2, -length / 2)    # On tile 3 here
    move_vertical(pen2, -length * 2)    # On tile 1 here
    move_vertical(pen2, -6)
    start_pos = pen2.pos()  # start_pos will refer to tile 1

    # Writing the elements into each box now
    for i in range(1,10):
        pen2.left(90)
        pen2.write(i, font=('times', 14, 'bold'))
        pen2.right(90)
        move_vertical(pen2, length)
        if (i % 3 == 0):    # For every number divisible by 3
            move_horizontal(pen2, length)   # change column
            move_vertical(pen2, -length * 3)    # return to bottom row
    move_horizontal(pen2, -2)
    for i in range(10,37):
        pen2.left(90)
        pen2.write(i, font=('times', 14, 'bold'))
        pen2.right(90)
        move_vertical(pen2, length)
        if (i % 3 == 0):    # For every number divisible by 3
            move_horizontal(pen2, length)   # change column
            move_vertical(pen2, -length * 3)    # return to bottom row
    move_horizontal(pen2, -4)
    for i in range(3):  # For 2:1 blocks
        pen2.left(90)
        pen2.write("2:1", font=('times', 14, 'bold'))
        pen2.right(90)
        move_vertical(pen2, length) # On 36 we return to the bottom row, so we need to move pen up

    return_position(pen2, start_pos)
    move_horizontal(pen2, -length)
    move_vertical(pen2, length)
    pen2.write("0", font=('times', 14, 'bold')) # 0 box
    return_position(pen2, start_pos)
    move_vertical(pen2, -length)
    move_horizontal(pen2, length)    # at (1-12) box

    pen2.write("(1 to 12)", font=('times', 14, 'bold'))
    move_horizontal(pen2, length * 4)
    pen2.write("(13 to 24)", font=('times', 14, 'bold'))
    move_horizontal(pen2, length * 4)
    pen2.write("(25 to 36)", font=('times', 14, 'bold'))
    return_position(pen2, start_pos)
    move_vertical(pen2, -length * 2)
    move_horizontal(pen2, (length / 4) - 10)  # 1 to 18 box

    pen2.write("1 to 18", font=('times', 14, 'bold')) #
    move_horizontal(pen2, length * 2)
    pen2.write("Even", font=('times', 14, 'bold')) #
    move_horizontal(pen2, length * 2)
    pen2.write("Red", font=('times', 14, 'bold')) #
    move_horizontal(pen2, length * 2)
    pen2.write("Black", font=('times', 14, 'bold')) #
    move_horizontal(pen2, length * 2)
    pen2.write("Odd", font=('times', 14, 'bold')) #
    move_horizontal(pen2, length * 2)
    pen2.write("19 to 36", font=('times', 14, 'bold')) #
    move_horizontal(pen2, length * 2)
    #turtle.mainloop()
    # Drawing table finished
speed = 100
move_vertical(pen, -200)
move_horizontal(pen, -300)
#pen.width(1)
pen.hideturtle()
pen2.hideturtle()
pen.speed(speed)
pen2.speed(speed)

#move_horizontal(pen2, 100)
roulette_wheel()
#move_vertical(pen2,200)
roulette_table()

#move_horizontal(pen, 5000)   # making turtle leave screen
#move_horizontal(pen2, 5000)
screen.tracer(False)
screen.tracer(True)

#ts = turtle.getscreen()

#ts.getcanvas().postscript(file="roulette_table.eps")

#img = Image.open("roulette_table"+".eps")
#img.save("roulette_table"+".jpg")
turtle.done()


