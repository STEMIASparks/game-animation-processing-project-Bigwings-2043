def setup():
    #create the screen
    size(800, 600)
    background(0)
    frameRate(60)
    noStroke()
    #load comic sans
    cs = loadFont('ComicSansMS-48.vlw')
    textFont(cs)
    #draw instructions
    textSize(40)
    text("Bootleg MS Paint", 20, 50)
    textSize(20)
    text("Use R, G, and B to change color", 20, 90)
    text("Use W for white, E to erase, and X to reset", 20, 120)
    text("Use + and - to change pen size", 20, 150)
    text("Use U/J, I/K, and O/L to increase or decrease", 20, 180)
    text("R, G, and B values by one, respectively", 20, 210)
    text("Press S to screenshot your art", 20, 240)
#utility values
pen = 50
r, g, b = 255, 255, 255
def draw():
    global pen, r, g, b
    #set pen color
    fill(r, g, b)
    #detect clicks)
    if mousePressed:
        circle(mouseX, mouseY, pen)
    #detect key presses
    if keyPressed:
        #color presets
        if key == 'r' or key == 'R':
            r, g, b = 255, 0, 0
        elif key == 'g' or key == 'G':
            r, g, b = 0, 255, 0
        elif key == 'b' or key == 'B':
            r, g, b = 0, 0, 255
        elif key == 'w' or key == 'W':
            r, g, b = 255, 255, 255
        elif key == 'e' or key == 'E':
            r, g, b = 0, 0, 0
        #reset
        elif key == 'x' or key == 'X':
            #redraw background and instructions
            background(0)
            fill(255, 255, 255)
            textSize(40)
            text("Bootleg MS Paint", 20, 50)
            textSize(20)
            text("Use R, G, and B to change color", 20, 90)
            text("Use W for white, E to erase, and X to reset", 20, 120)
            text("Use + and - to change pen size", 20, 150)
            text("Use U/J, I/K, and O/L to increase or decrease", 20, 180)
            text("R, G, and B values by one, respectively", 20, 210)
            text("Press S to screenshot your art", 20, 240)
            #reset variables
            pen = 50
            r, g, b = 255, 255, 255
        #change pen size
        elif key == '=' or key == '+':
            pen = pen+1
        elif key == '-' or key == '_':
            pen = pen-1
        #specific color changes
        elif key == 'u' or key == 'U':
            r = r+1
        elif key == 'j' or key == 'J':
            r = r-1
        elif key == 'i' or key == 'I':
            g = g+1
        elif key == 'k' or key == 'K':
            g = g-1
        elif key == 'o' or key == 'O':
            b = b+1
        elif key == 'l' or key == 'L':
            b = b-1
        #save image
        elif key == 's' or key == 'S':
            saveFrame("Bootleg MS Paint ####.png")
    #draw r, g, and b value
    fill(0)
    rect(10, 245, 250, 35)
    fill(255)
    text(r, 20, 270)
    text(g, 110, 270)
    text(b, 200, 270)
    fill(r, g, b)
