#Startposition Anfang der Strasse
xPos = 30
#Geschwindigkeit des Autos
offset = 4

#Startposition Ball
yPos = 50
#Geschwindikeit Ball
offsetball = 3

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
    background(255, 255, 255)
    strasse() #FUnktion Strasse aufrufen
    image(img1, 1030, 0, 40,90)
    for i in range(4):
        image(img2, 400 + i*100, 310, 80,80)
    image(img3, 300, 10, 100, 60)

#Fahrt Auto von links nach rechts
    global xPos
    global offset
    global modus
    
    #print xPos
    image(img4, xPos, 203, 160, 80)
    
    if modus == "fahren":
        xPos = xPos + offset
        
# Ball rollt rein
    global yPos
    global offsetball
    
    ball(yPos) #Funktion Ball aufrufen 
    
    print yPos

    yPos = yPos + offsetball

    if yPos > height - 155:
        offsetball = 0


#Fahrt wird durch Taste unterbrochen
def keyPressed():
    global modus
    modus = "stop"
    
# Definition Ball
def ball(yPos):
    noStroke
    fill(210, 105, 30)#Farbe
    circle(1400,yPos,30)

    
