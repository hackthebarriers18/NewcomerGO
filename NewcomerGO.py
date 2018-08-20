#Hack the Barriers 18
#Elham Islam, Eric Wei, Jim Wu, Samuel Sun, Tailai Wang 
from pygame import*
from pygame.locals import*
from math import*
from math import radians, cos, sin, asin, sqrt
from random import*
import tkinter as tk
from tkinter import filedialog
import pygame



pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(22050,-16,2,2048) #sound 

#SCREEN STUFF AND CONSTANTS
#####################################################################
radius = 6371
screenWidth = 640
screenHeight = 640
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
GREY = (111,111,111)
TEAL = (0, 128, 128)
screen = display.set_mode((screenWidth,screenHeight))#screen size (16:9 iOS ratios)
#####################################################################
#FONTS
font.init()
ralewayBold60 = font.Font("raleway/Raleway-Bold.ttf",60)
ralewayRegular48 = font.Font("raleway/Raleway-Regular.ttf", 48)
ralewayMedium36 = font.Font("raleway/Raleway-Medium.ttf", 36)
ralewayRegular24 = font.Font("raleway/Raleway-Regular.ttf", 24)
ralewayRegular12 = font.Font("raleway/Raleway-Regular.ttf", 12)
testText =ralewayBold60.render("B-Safe", True, BLACK)
testTextX,testTextY = ralewayBold60.size("B-Safe")
####################################################################
logo = image.load("2000px-Pokémon_GO_logo.png")
logo = transform.scale(logo, (640, 384))
startRect = Rect(screenWidth/2 - 160, 450, 320, 80)
startText = ralewayRegular48.render("Start", True, BLACK)
####################################################################
maps = image.load("map.png")
maps = transform.scale(maps, (640, 291))

####################################################################
def screenFill(c):
    draw.rect(screen, (c), (0, 0, screenWidth, screenHeight))
    
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r
lat1 = 53.32055555555556
lat2 = 53.31861111111111
lon1 = -1.7297222222222221
lon2 = -1.6997222222222223
print(haversine(lon1,lat1,lon2,lat2))

def drawMenu():
    screen.blit(logo, (0,0))
    draw.rect(screen, BLACK, startRect, 2)
    screen.blit(startText, (screenWidth/2 - startText.get_width()/2, 460))

def drawMap():
    screen.blit(maps, (0,150))
#####################################################################
running = True
section = "Menu"
while running:
    leftClick = False #leftClick and rightClick are used to prevent accidental drag
    enter = False
    for evt in event.get():
        if evt.type == QUIT:
            running=False
        if evt.type == KEYDOWN:
            if evt.key == K_ESCAPE:
                running = False #shuts program on ESC
            if evt.key == K_RETURN:
                enter = True
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1:
                leftClick = True
     
#---------------------------------------------------------------------
    mx,my = mouse.get_pos() #Mouse position
#---------------------------------------------------------------------
    if section == "Menu":
         screenFill(TEAL)
         drawMenu()
         if (startRect.collidepoint(mx,my) and leftClick):
             section = "Map"

    if section == "Map":
        screenFill(WHITE)
        drawMap()
    display.flip()
quit() #<---the worst thing ever
