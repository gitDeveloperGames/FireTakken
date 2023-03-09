# سازنده علی اکبر رحیمی => developer Ali akbar Rahimi
# ساخت ایران => made in Iran
import pygame
import sys
import random
import time
from pygame import mixer
import pyttsx3
mixer.init()
sound = pyttsx3.init()
mixer.music.load("images/punch_sfx_3.mp3")
TakkenX = 20
TakkenY = 420
RivalX = 400
RivalY = 390
#-------------------------
DeateX_Takken = 60
DateX_Rival = 460
DateY_Takken = 15
DateY_Rival = 15
WidthCharsT = 300
HeightCharsT = 10
WidthCharsR = 300
HeightCharsR = 10
#-------------------------
folder = "Rival1"
TakkenPos = "defulte"
RivalPos = "defulte"
eventRL = ""
eventUD = ""
KickSleeper = 0
BoxSleeper= 0
sleeperRival = 0
pygame.init()
Alert = ""
FireSleeper = 0
f = pygame.font.Font(None,40)
Display = pygame.display.set_mode((800,600))
#-------------------------------------
Background = pygame.image.load("images/Bg.png")
BACKGROUND = pygame.transform.scale(Background,(800,600))
#-------------------------------------
image1 = pygame.image.load("images/image1.jpg")
IMAGE1 = pygame.transform.scale(image1,(50,50))
#-------------------------------------
#Takken Positions
Takken1 = pygame.image.load("images/Takken1.png")
TAKKEN1 = pygame.transform.scale(Takken1,(100,100))
#-----------------------------------------------------
Takken2 = pygame.image.load("images/Takken2.png")
TAKKEN2 = pygame.transform.scale(Takken2,(100,100))
#-----------------------------------------------
Takken3 = pygame.image.load("images/Takken3.png")
TAKKEN3 = pygame.transform.scale(Takken3,(100,100))
#------------------------------------------------
Takken4 = pygame.image.load("images/Takken4.png")
TAKKEN4 = pygame.transform.scale(Takken4,(100,100))
#-------------------------------------------------
Takken5 = pygame.image.load("images/Takken5.png")
TAKKEN5 = pygame.transform.scale(Takken5,(100,100))
#-----------------------------------------------
Takken6 = pygame.image.load("images/Takken6.png")
TAKKEN6 = pygame.transform.scale(Takken6,(100,100))
#-------------------------------------------------
Takken7 = pygame.image.load("images/Takken7.png")
TAKKEN7 = pygame.transform.scale(Takken7,(100,100))
def Bg(folder):
    image2 = pygame.image.load(f"images/{folder}/image2.jpg")
    IMAGE2 = pygame.transform.scale(image2,(50,50))
    Display.blit(BACKGROUND,(0,0))
    Text = f.render(Alert,True,(0,255,255))
    Display.blit(Text,(300,200))
    Display.blit(IMAGE1,(0,0))
    Display.blit(IMAGE2,(400,0))
    Deate_Takken = pygame.draw.rect(Display,(0,255,255),(DeateX_Takken,DateY_Takken,WidthCharsT,HeightCharsT))
    Deate_Rival = pygame.draw.rect(Display,(255,0,255),(DateX_Rival,DateY_Rival,WidthCharsR,HeightCharsR))
def Takken(TakkenX,TakkenY,TakkenPos):
    if TakkenPos == "defulte":
        Display.blit(TAKKEN1,(TakkenX,TakkenY))
    elif TakkenPos == "sejent":
        Display.blit(TAKKEN2,(TakkenX,TakkenY))
    elif TakkenPos == "AnimalKickD":
        Display.blit(TAKKEN3,(TakkenX,TakkenY))
    elif TakkenPos == "AnimalBoxS":
        Display.blit(TAKKEN4,(TakkenX,TakkenY))
    elif TakkenPos == "AnimalBoxD":
        Display.blit(TAKKEN5,(TakkenX,TakkenY))
    elif TakkenPos == "AnimalKickD2":
        Display.blit(TAKKEN6,(TakkenX,TakkenY))
    elif TakkenPos == "AnimalKickD3":
        Display.blit(TAKKEN7,(TakkenX,TakkenY))
def Rival(RivalX,RivalY,RivalPos,folder):
    #Rival Positions
    try:
        Rival1 = pygame.image.load(f"images/{folder}/rival1.png")
        RIVAL1 = pygame.transform.scale(Rival1,(150,150))
        #------------------------------------------------
        Rival2 = pygame.image.load(f"images/{folder}/rival2.png")
        RIVAL2 = pygame.transform.scale(Rival2,(150,150))
        #-----------------------------------------------
        Rival3 = pygame.image.load(f"images/{folder}/rival3.png")
        RIVAL3 = pygame.transform.scale(Rival3,(150,150))
        #-----------------------------------------------
        Rival4 = pygame.image.load(f"images/{folder}/rival4.png")
        RIVAL4 = pygame.transform.scale(Rival4,(150,150))
    except:
        pass
    if RivalPos == "defulte":
        try:
            Display.blit(RIVAL1,(RivalX,RivalY))
        except:
            pass
    elif RivalPos == "AnimalKickD":
        try:
            Display.blit(RIVAL2,(RivalX,RivalY))
        except:
            pass
    elif RivalPos == "sejent":
        try:
            Display.blit(RIVAL3,(RivalX,RivalY))
        except:
            pass
    elif RivalPos == "FrontKick":
        try:
            Display.blit(RIVAL4,(RivalX,RivalY))
        except:
            pass
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                eventRL = "Left"
            elif event.key == pygame.K_RIGHT:
                eventRL = "Right"
            elif event.key == pygame.K_DOWN:
                TakkenPos = "sejent"
            elif event.key == pygame.K_UP:
                TakkenPos = "defulte"
            elif event.key == pygame.K_TAB:
                if TakkenPos != "sejent":
                    TakkenY -= 200
            elif event.key == pygame.K_SPACE:
                if TakkenPos == "defulte":
                    ranNum1 = random.randint(0,3)
                    if ranNum1 == 0:
                        TakkenPos = "AnimalKickD"
                    elif ranNum1 == 1:
                        TakkenPos = "AnimalBoxD"
                    elif ranNum1 == 2:
                        TakkenPos = "AnimalKickD2"
                if TakkenPos == "sejent":
                    ranNum2 = random.randint(0,1)
                    if ranNum2 == 0:
                        TakkenPos = "AnimalBoxS"
        elif event.type == pygame.KEYUP:
            eventRL = ""
    if RivalX < TakkenX:
        RivalX = TakkenX + 80
    if TakkenY == 500:
        TakkenY -= 5
    if RivalX > 780:
        RivalX -= 150
        TakkenX -= 200
    sleeperRival += 25
    if TakkenPos == "AnimalKickD" or "AnimalKickD2":
        KickSleeper += 30
    if TakkenPos == "AnimalBoxS":
        BoxSleeper += 30
    if TakkenPos == "AnimalBoxD":
        BoxSleeper += 30
    if KickSleeper > 150 or BoxSleeper > 150:
        TakkenPos = 'defulte'
        KickSleeper = 0
        BoxSleeper = 0
    if TakkenY < 420:
        TakkenY += 40
    if eventRL == "Left":
        TakkenX -= 35
    if eventRL == "Right":
        TakkenX += 35
    # RivalST
    if sleeperRival > 50 and RivalX - TakkenX < 250:
        sleeperRival = 0
        Position = random.randint(0,3)
        if Position == 0:
            RivalPos = "AnimalKickD"
            RivalX -= 25
        elif Position == 1:
            RivalPos = "defulte"
        elif Position == 2:
            RivalPos = "sejent"
        elif Position == 3:
            RivalPos = "FrontKick"
    #RivalST2
    if RivalY < 390:
        RivalY += 40
    #---------------------------
    # Colitions
    for i in range(50):
        if TakkenX + i == RivalX and TakkenPos != "defulte":
            Alert = "Lets Go Bybi !"
            RivalX += 50
            WidthCharsR -= 20
            mixer.music.play()
        if RivalX - i == TakkenX and RivalPos != "defulte":
            Alert = "Oh Not"
            WidthCharsT -= 10
            RivalX -= 30
            TakkenX -= 30
            mixer.music.play()
    for x in range(50):
        if TakkenX == RivalX and TakkenPos == "defulte":
            TakkenX -= 50
    if TakkenY < 420 and eventRL != "":
        TakkenPos = "AnimalKickD3"
    #----------Crasheds------------
    if WidthCharsR == 0:
        RivalX = 400
        TakkenX = 20
        WidthCharsR = 300
        Alert = "Lets Fight"
        Fighter = random.randint(0,3)
        if Fighter == 0:
            folder = "Rival1"
        elif Fighter == 1:
            folder = "Rival2"
        elif Fighter == 2:
            folder = "Rival3"
        elif Fighter == 3:
            folder = "Rival4"
        sound.setProperty("rate",100)
        sound.say("Lets Fight")
        sound.runAndWait()
    if WidthCharsT < 5:
        sound.setProperty("rate",100)
        sound.say("You Crashed")
        sound.runAndWait()
        sys.exit()
    pygame.display.update()
    Bg(folder)
    Takken(TakkenX,TakkenY,TakkenPos)
    Rival(RivalX,RivalY,RivalPos,folder)
    
# Game Over
