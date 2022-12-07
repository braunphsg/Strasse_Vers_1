#Startposition Anfang der Strasse
xPos = 30
#Geschwindigkeit des Autos
offset = 4

# Funktion Strasse wird aus der Datei hintergrund geladen
from hintergrund import strasse

# SETUP -------------------------------------------------------------------------
def setup():
    
    size(1500,400)#Fenstergrösse
    background(255, 255, 255)#Fenster Hintergrundfarbe 
    global img1
    global img2
    global img3
    global img3
    global img4
    global modus
    img1 = loadImage("fussgaenger.jpg")
    img2 = loadImage("baum.jpg")
    img3 = loadImage("bank.jpg")
    img4 = loadImage("auto.jpg")
    
    modus = "fahren"   
   

# DEF DRAW -------------------------------------------------------------------------------------------------
def draw():
    strasse()
    image(img1, 1030, 0, 40,90)
    for i in range(4):
        image(img2, 400 + i*100, 310, 80,80)
    image(img3, 300, 10, 100, 60)
    
    global xPos
    global offset
    global modus
    
    print xPos
    image(img4, xPos, 203, 160, 80)
    
    if modus == "fahren":
        xPos = xPos + offset

    
def keyPressed():
    global modus
    modus = "stop"


    



        



    
    
    
