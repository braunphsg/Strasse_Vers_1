# SETUP -------------------------------------------------------------------------

from hintergrund import strasse

def setup():
    size(1500,400)#Fenstergrösse
    background(255, 255, 255)#Fenster Hintergrundfarbe 
    global img1
    global img2
    global img3
    img1 = loadImage("fussgaenger.jpg")
    img2 = loadImage("baum.jpg")
    img3 = loadImage("bank.jpg")
    
# DEF DRAW -------------------------------------------------------------------------------------------------
def draw():
    strasse()

    
    
    
