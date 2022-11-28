# SETUP -------------------------------------------------------------------------

from hintergrund import strasse

def setup():
    size(1500,400)#Fenstergrösse
    background(255, 255, 255)#Fenster Hintergrundfarbe 
    #global img1
    #global img2
    #global img3
    #img1 = loadImage("fussgaenger.jpg")
    #img2 = loadImage("baum.jpg")
    #img3 = loadImage("bank.jpg")
    
# DEF DRAW -------------------------------------------------------------------------------------------------
def draw():
    strasse()
#Erzeugt ein Objekt der Klasse Auto
Auto Kaefer;
 
void setup() {
size(800, 800);
// Aufruf des Konstruktors
Kaefer = new Auto(0, color(100, 50, 255));
rectMode(CENTER);
}
 
void draw() {
background(200);
#Aufruf der Methoden des Objekts
Kaefer.move();
Kaefer.render();
}
 
#Zum Steuern des Autos werden
void keyPressed() {
if (key == CODED) {
if (keyCode == UP) {
Kaefer.accelerate();
}
else if (keyCode == DOWN) {
Kaefer.slowDown();
}
else if (keyCode == LEFT) {
Kaefer.steerLeft();
}
else if (keyCode == RIGHT) {
Kaefer.steerRight();
}
    
    
    
