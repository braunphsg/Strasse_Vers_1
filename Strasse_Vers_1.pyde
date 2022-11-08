# SETUP -------------------------------------------------------------------------
def setup():
    size(1500,400)#Fenstergrösse
    background(255, 255, 255)#Fenster Hintergrundfarbe
    bild = loadImage("fussgaenger.png")

# DEF DRAW -------------------------------------------------------------------------------------------------
def draw():
    # STRASSE ----------------------------------------------------------------------------------------------
    noStroke
    fill(154, 154, 154)#Farbe
    rect(0, 100, 1500, 200)#Strassenumfang
    
    # SEITENLINIE OBEN -------------------------------------------------------------------------------------
    noStroke
    fill(255, 255, 255)#Farbe
    rect(0, 106, 1500, 4) #Umfang Seitenlinie
    
    # SEITENLINIE UNTEN ------------------------------------------------------------------------------------
    noStroke
    fill(255, 255, 255)#Farbe
    rect(0, 288, 1500, 4) #Umfang Seitenlinie
    
    # MITTELLINIE ------------------------------------------------------------------------------------------
    for i in range(34):
        noStroke
        fill(255, 255, 255) #Farbe
        rect(i*45, 197, 30, 4) #Umfang Seitenlinie
        
    # FUSSGAENGERSTREIFFEN OBERHABLB DER MITTELINIE --------------------------------------------------------
    for i in range(3):
        noStroke
        fill(251, 197, 0)#Farbe
        rect(1000, 114 + i*30, 100, 20)#Umfang Seitenline
        
    # FUSSGAENGERSTREIFFEN OBERHABLB DER MITTELINIE --------------------------------------------------------
    for i in range(3):
        noStroke
        fill(251, 197, 0)#Farbe
        rect(1000, 204 + i*30, 100, 20)#Umfang Seitenline
    
    #BILD DER FUSSGÄNGER LADEN -----------------------------------------------------------------------------
    image(bild, 800, 100)
    
    
    
