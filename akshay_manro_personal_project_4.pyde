import time

def setup():
    rectMode(CENTER)
    size(800, 600)
    background(0)
    frameRate(60)
    #start screen
    ba = loadFont("BookAntiqua-48.vlw")
    textFont(ba)
    textSize(60)
    text("Bootleg Agar.io", 200, 250)
    textSize(30)
    text("Use arrow keys to move", 240, 300)
    text("Don't hit the circles", 270, 350)
    text("Press X to start", 300, 400)
y = 300
x = 400
obs = 0
obsx = 0
obsy = 0
obss = 0
start = 0
obsr = 0
def draw():
    global x, y, obs, obsx, obsy, obss, obsr, start
    if keyPressed and start == 0:
        if key == 'x' or key == 'X':
            background(0)
            #ensure loop only runs once
            start = 1
    elif start == 1:
        background(0)
        fill(255)
        rect(x, y, 60, 60)
        #move player
        if keyPressed:
            if keyCode == UP:
                y = y-4
            elif keyCode == DOWN:
                y = y+4
            elif keyCode == LEFT:
                x = x-4
            elif keyCode == RIGHT:
                x = x+4
        #obstacle generation
        if obs == 1:
            if obss == 0:
                obsx = int(random(120, 680))
                obsy = int(random(120, 480))
            obss = obss+4
            obsr = obss/2
            circle(obsx, obsy, obss)
            if obss == 240:
                obss = 0
                obsr = 0
                obs = 0
        else:
            obs = int(random(0, 50))
        #detect collision
        if obsx-obsr-30 < x < obsx+obsr+30 and obsy-obsr-30 < y < obsy+obsr+30:
            start = 2
    #end screen
    elif start == 2:
        background(0)
        textSize(80)
        text("You Died", 250, 300)
        textSize(30)
        text("Press X to restart", 300, 340)
        if keyPressed:
            if key == 'x' or key == 'X':
                #reset game
                start = 1
                obs, obss, obsx, obsy = 0, 0, 0, 0
    #debugging utility
    print(x)
    print(y)
    print("---")
    print(obsx)
    print(obsy)
    print("---")
    print(obss)
    print(obsr)
    print("----------")
    
