#Startposition Auto
xPos = 30
#Geschwindigkeit des Autos
offset = 4

#Startposition Ball
yPos = 50
#Geschwindikeit Ball
offsetball = 6

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
    background(255, 255, 255) #Weisser Hintergrund
    strasse() #Funktion Strasse aufrufen
    image(img1, 1030, 0, 40,90)
    #Bilder (Bäume) aufrufen
    for i in range(4):
        image(img2, 400 + i*100, 310, 80,80)
    #Bild (Bank) laden
    image(img3, 300, 10, 100, 60)

#Autofahrt
    global xPos
    global offset
    global modus

    image(img4, xPos, 203, 160, 80) #Bild Auto aufrufen
    
    #Positionsänderung Autobild = Auto fährt
    if modus == "fahren":
        xPos = xPos + offset
    
    #Bei Crash, stoppt das Auto und Lose erscheint
    if xPos > i +200:
        offset = 0
        boxlose()
    
    else: 
        boxwin()
            
# Ballrollen
    global yPos
    global offsetball
    
    ball(yPos) #Funktion Ball aufrufen 
    
    print yPos

    #Positionsänderung Ball = Ball rollt rein
    yPos = yPos + offsetball

    if yPos > height - 155:
        offsetball = 0

#Fahrt wird durch Leer-Taste unterbrochen
def keyPressed():
    if (key == ' '):
        global modus
        modus = "stop"

    else:
        xPos + offset


i = random(xPos +250, xPos +350)

def ball(yPos):
    noStroke
    fill(210, 105, 30)#Farbe
    circle(i,yPos,30)
    
def boxlose():
    noStroke
    fill(255, 110, 74)#Farbe
    circle(750,200,100)
    
def boxwin():
    noStroke
    fill(124,252,0)#Farbe
    circle(750,200,100)
    
