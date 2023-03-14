def setup():
    #setup the screen
    global dvd
    background(0)
    frameRate(60)
    size(800, 600)
    #load the image
    dvd = loadImage("DVD_logo_white_nobg.png")
#define utility variables
x = 20
y = 20
up = 0
left = 0
r = 255
g = 255
b = 255
def draw():
    global x, y, up, left, r, g, b
    background(0)
    #color and draw the logo
    tint(r, g, b)
    image(dvd, x, y, 120, 60)
    #detect collisions
    if x >= 680:
        #change position to avoid continuous detection
        x = 677
        #change direction
        left = 1
        #randomise color
        r, g, b, = random(0, 255), random(0, 255), random(0, 255)
    if y >= 540:
        y = 537
        up = 1
        r, g, b, = random(0, 255), random(0, 255), random(0, 255)
    if x <= 0:
        x = 3
        left = 0
        r, g, b, = random(0, 255), random(0, 255), random(0, 255)
    if y<= 0:
        y = 3
        up = 0
        r, g, b, = random(0, 255), random(0, 255), random(0, 255)
    #direct movement based on collisions
    if up == 1:
        y = y-3
    else:
        y = y+3
    if left == 1:
        x = x-3
    else:
        x = x+3
    #utility to track exact position
    print(x)
    print(y)
    print("-------")
