# HINTERGRUND DEFINIEREN -------------------------------------------------------------
def strasse():
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
            
    # FUSSGÄNGERSTREIFEN UNTERHALB DER MITTELLINIE ------------------------------
    for i in range(3):
        noStroke
        fill(251, 197, 0)#Farbe
        rect(1000, 204 + i *30, 100, 20)#Umfang Seitenlinie
        
    #BILD DER FUSSGÄNGER UND BÄUME LADEN -----------------------------------------------------------------------------
    #image(img1, 1030, 0, 40,90)
    #for i in range(4):
        #image(img2, 400 + i*100, 310, 80,80)
    #image(img3, 300, 10, 100, 60)
