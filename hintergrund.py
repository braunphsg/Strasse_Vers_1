# HINTERGRUND DEFINIEREN --------------------------------------
def strasse():
    # Strasse -------------------------------------------------
    noStroke
    fill(154, 154, 154)#Farbe
    rect(0, 100, 1500, 200)#Strassenumfang
        
    # Seitenlinie oben ----------------------------------------
    noStroke
    fill(255, 255, 255)#Farbe
    rect(0, 106, 1500, 4) #Umfang Seitenlinie
        
    # Seitenlinie unten ---------------------------------------
    fill(255, 255, 255)#Farbe
    rect(0, 288, 1500, 4) #Umfang Seitenlinie
        
    # Mittelinie ---------------------------------------------
    for i in range(34):
        noStroke
        fill(255, 255, 255) #Farbe
        rect(i*45, 197, 30, 4) #Umfang Seitenlinie
            
    # Fussgaengerstrefen oberhalb der Mittellinie -----------
    for i in range(3):
        noStroke
        fill(251, 197, 0)#Farbe
        rect(1000, 114 + i*30, 100, 20)#Umfang Seitenline
            
    # Fussgaengerstreifen unterhalb der Mittellinie -----------
    for i in range(3):
        noStroke
        fill(251, 197, 0)#Farbe
        rect(1000, 204 + i *30, 100, 20)#Umfang Seitenlinie
