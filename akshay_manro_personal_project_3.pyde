import time

def setup():
    size(800,600)
    frameRate(60)
    noStroke()
    background(19, 189, 44)
    #start screen
    gb = loadFont("Gabriola-48.vlw")
    textFont(gb)
    textSize(60)
    text("Bootleg Mini Golf", 230, 300)
    textSize(40)
    text("Click to start", 320, 350)
    text("Click to move", 320, 390)
start = 0
x = 115
y = 350
h = 0
#the direction the ball should move
right = False
up = False
#calculating direction
angle = 0
rise = 0
run = 0
slope = 0
distance = 0
def draw():
    global start, x, y, h, slope, distance, right, up, angle, rise, run
    h = 600-y
    if mousePressed and start == 0:
        #ensure loop only runs once
        start = 1
        #remove text
        background(19, 189, 44)
        #draw ball
        circle(x, y, 20)
        fill(0)
        #draw hole
        circle(675, 500, 30)
        fill(8, 110, 13)
        #draw map
        triangle(0, 400, 0, 0, 300, 0)
        triangle(0, 600, 300, 600, 300, 200)
        rect(300, 200, 300, 400)
        rect(750, 0, 50, 600)
        rect(0, 0, 800, 50)
        rect(0, 0, 50, 600)
        rect(0, 550, 800, 50)
    elif mousePressed and start == 1:
        #calculations
        rise = mouseY-y
        run = mouseX-x
        slope = rise/run
        distance = sqrt(((abs(mouseY-y))^2)+((abs(mouseX-x))^2))
        #determining direction
        if mouseX < x:
            right = True
        elif mouseX > x:
            right = False
        if mouseY > y:
            up = True
        elif mouseY < y:
            up = False
        #more calculations
        angle = atan(slope)
        angle = degrees(angle)
        #unused code
        if up == True and right == True:
            pass
        if up == True and right == False:
            pass
        if up == False and right == True:
            pass
        if up == False and right == False:
            pass
        #failed attempt at movement
        '''
        for i in range(0, run):
            x = x+1
        for i in range(0, rise):
            y = y+1
        '''
        #incorrect but functional movement
        x = x+run
        y = y+rise
        
        #draw movement
        background(19, 189, 44)
        #draw ball
        fill(255)
        circle(x, y, 20)
        fill(0)
        #draw hole
        circle(675, 500, 30)
        fill(8, 110, 13)
        #redraw map
        triangle(0, 400, 0, 0, 300, 0)
        triangle(0, 600, 300, 600, 300, 200)
        rect(300, 200, 300, 400)
        rect(750, 0, 50, 600)
        rect(0, 0, 800, 50)
        rect(0, 0, 50, 600)
        rect(0, 550, 800, 50)
        #weird thing with this calculation, it won't calculate shallow angles on either side
        #using the clock analogy, 1:30 to 4:30 is unresponsive, along with 7:30 to 10:30
        #in those ranges, it jumps from 45 degrees, to 0 degrees, to -45 degrees
        #presumably because of an odd interaction between tan 45 = 1 and the way I calculate angles
        
        #check if ball is in the hole
        if 660 < x < 690 and 485 < y < 515:
            start = 2
        #utility for debugging
        print(slope)
        print(angle)
        print("---")
        print(right)
        print(up)
        print("---")
        print(distance)
        print("---")
        print(x)
        print(y)
        print("---")
    #end screen
    if start == 2:
        background(19, 189, 44)
        fill(255)
        textSize(80)
        text("You did it", 290, 320)
    #utility for mapping
    if mousePressed:
        print(mouseX)
        print(mouseY)
        print("------------")
        time.sleep(0.1)
