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


# SETUP -------------------------------------------------------
def setup():
    
    size(1500,400)#Fenstergrösse
    #Variablen global setzen
    global img1
    global img2
    global img3
    global img3
    global img4
    global modus
    #Bilder laden
    img1 = loadImage("fussgaenger.jpg")
    img2 = loadImage("baum.jpg")
    img3 = loadImage("bank.jpg")
    img4 = loadImage("auto.jpg")
    
    modus = "fahren" #Grundsätzlich ist das Auto beim Programmstart fahrend
                    
                                                
# DEF DRAW -----------------------------------------------------
def draw():
    background(255, 255, 255) #Hintergrundfarbe
    strasse() #Funktion Strasse aufrufen
    
    #Text (Spielanleitung)
    fill(0,0,0)
    textSize(25)
    text("Try to stop the car in time ", 20, 30)#Text und Position
    text("with your Space key! ", 20, 60)

    #Bild (Fussgänger) aufrufen
    image(img1, 1030, 0, 40,90)
    #Bilder (Bäume) aufrufen
    for i in range(4):
        image(img2, 400 + i*100, 310, 80,80)
    #Bild (Bank) aufrufen
    image(img3, 300, 10, 100, 60)

#Autofahrt
    #Variablen global setzen
    global xPos
    global offset
    global modus

    image(img4, xPos, 203, 160, 80) #Bild Auto aufrufen
    
    #Positionsänderung Autobild = Auto fährt
    if modus == "fahren":
        xPos = xPos + offset
    
    #Bei Crash, stoppt das Auto und LOSE erscheint
    if xPos > i +200:
        offset = 0
        boxlose()
    #Sonst erscheint LOSE
    else: 
        boxwin()
            
# Ballrollen
    #Variablen werden global gesetzt
    global yPos
    global offsetball
    
    ball(yPos) #Funktion Ball aufrufen 
    
    #yPos wird als Wert ausgegeben
    print yPos

    #Positionsänderung Ball = Ball rollt rein
    yPos = yPos + offsetball

    #Ball bremst auf Höhe der unteren Fahrbahn
    if yPos > height - 155:
        offsetball = 0

#Fahrt wird durch Leer-Taste unterbrochen
def keyPressed():
    if (key == ' '):
        global modus
        modus = "stop"

    else:
        xPos + offset

#i als X-Position des Ball (Zufallswert zwischen 250 -350 vor dem Auto)
i = random(xPos +250, xPos +350)

#Definition FUnktion Ball
def ball(yPos):
    noStroke
    fill(210, 105, 30)#Farbe
    circle(i,yPos,30)

#Definition Box LOSE
def boxlose():
    noStroke
    fill(255, 110, 74)#Farbe
    circle(1400,75,300)
    textSize(30)#Textgrösse
    fill(0, 0, 0)#Schriftfarbe
    text("YOU", 1365, 50)#Text und Position
    textSize(60)#Textgrösse
    fill(0, 0, 0)#Schriftfarbe
    text("LOSE", 1325, 110)#Text und Position

#DEFINITION BOX  WIN    
def boxwin():
    noStroke
    fill(124,252,0)#Farbe
    circle(1400,75,300)
    textSize(30)#Textgrösse
    fill(0, 0, 0)#Schriftfarbe
    text("YOU", 1365, 50)#Text und Position
    textSize(60)#Textgrösse
    fill(0, 0, 0)#Schriftfarbe
    text("WIN", 1340 , 110)#Text und Position
    
