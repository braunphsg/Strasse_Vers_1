# SETUP -------------------------------------------------------------------------

xPos = 50
offset = 5

from hintergrund import strasse

def setup():
    size(1500,400)#Fenstergrösse
    background(255, 255, 255)#Fenster Hintergrundfarbe 
    global img1
    global img2
    global img3
    global img3
    global img4
    img1 = loadImage("fussgaenger.jpg")
    img2 = loadImage("baum.jpg")
    img3 = loadImage("bank.jpg")
    img4 = loadImage("auto.jpg")
    
# DEF DRAW -------------------------------------------------------------------------------------------------
def draw():
    
    strasse()
    image(img1, 1030, 0, 40,90)
    for i in range(4):
        image(img2, 400 + i*100, 310, 80,80)
    image(img3, 300, 10, 100, 60)
    
    global xPos
    global offset
    
    print xPos
    image(img4, xPos, 200, 200, 100)
    
    xPos = xPos + offset
    



        



    
    
    
