# This is the source code of Freath.
# A hobby gaming project. Created by Eren Özer. 09/2025
# All rights reserved.
import random
import time

import pygame
from sys import exit


# initializing pygame for the first time
pygame.init()





# The game display screen and renaming the window

screen = pygame.display.set_mode()

            # Game Ready Screen

screenWidth, screenHeight = screen.get_size()
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN | pygame.NOFRAME)


# 1392, 760 Scaling Test Screen
#screenWidth, screenHeight = 1392, 760
#screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.NOFRAME)

pygame.display.set_caption("Freath")


# Independent frame rates (set to 60 in main)
clock = pygame.time.Clock()




# Image Scaler (Testing)

def imageScaler(image):
    width, height = image.get_width(), image.get_height()
    if width >= 1392:
        width = width * (1392 / screenWidth)
    else:
        width = width * (screenWidth / 1392)
    if height >= 1392:
        height = height * (1392 / screenHeight)
    else:
        height = height * (screenHeight / 1392)
    return int(width), int(height)


# Background Images


#BackgroundImage = pygame.image.load("HERE PASTE YOUR IMAGE HERE NERD")

coin = pygame.image.load("Blueberry_mob.png")


# End of Background Images




# Player Images & Animations

PlayerIdle = pygame.image.load("Simple_wizard_pixel.png").convert_alpha()
PlayerJump = pygame.image.load("wizardjump.png").convert_alpha()





# Monster Images & Animations

GhostMob = [pygame.image.load("ghost_mob_idle.png"), pygame.image.load("ghost_mob.png")]

Spike = pygame.image.load("spikeyboy.png").convert_alpha()






# Function for changing X

def addToX(num, velocity):
    num += velocity
    return num



# Repositioning and Rescaling Images Based on Development Screen 1392x760

def imagePos(positionX, positionY):
    horizontalScaler = (positionX * screenWidth) // 1392
    verticalScaler = (positionY * screenHeight) // 760
    return horizontalScaler, verticalScaler

def rescaleImagePosByX(positionX):
    horizontalScaler = (positionX * screenWidth) // 1392
    return horizontalScaler

def rescaleImagePosByY(positionY):
    verticalScaler = (positionY * screenHeight) // 760
    return verticalScaler



# Player X & Y Coordinates & Extras

PlayerXCoordinate = 200         # Player X

PlayerYCoordinate = 439         # Player Y

PlayerXCoordinate, PlayerYCoordinate = imagePos(PlayerXCoordinate, PlayerYCoordinate)  # Rescaled positions depending on screen width and height

FacingRight = True



# Map Obstacles X & Y Coordinates & Extras

SpikeX = random.randrange(0, screenWidth)
SpikeY = -50

coinXCoordinate = random.randrange(0, screenWidth)
coinYCoordinate = random.randrange(0, screenHeight//2)

score = 0



# Monsters X & Y Coordinates & Extras

GhostXCoordinate = 1200          # Ghost X

GhostYCoordinate = 439          # Ghost Y

GhostXCoordinate, GhostYCoordinate = imagePos(GhostXCoordinate, GhostYCoordinate)



# Jumping Variables

isJumping = False
JumpVelocity = rescaleImagePosByY(18)
JumpAccelerator = rescaleImagePosByY(1)



# Main function of the project
if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()



        # Test screen

        #screen.blit(BackgroundImage)
        screen.fill((1, 1, 15))



        # Collision detection with spike

        if 30 > abs(PlayerXCoordinate - SpikeX) > 0:
            if 65 > abs(PlayerYCoordinate - SpikeY) > 30:
                PlayerIdle = pygame.image.load("spikeyboydeath.png")
                screen.blit(PlayerIdle, (PlayerXCoordinate, PlayerYCoordinate))
                screen.blit(GhostMob[0], (GhostXCoordinate, GhostYCoordinate))
                pygame.display.update()
                Spike = 0
                time.sleep(3)
                pygame.quit()
                exit()



        # Player Image Loader

        if FacingRight:
            if not isJumping:
                screen.blit(PlayerIdle, (PlayerXCoordinate, PlayerYCoordinate))
            else:
                screen.blit(PlayerJump, (PlayerXCoordinate, PlayerYCoordinate))
        else:
            if not isJumping:
                screen.blit(pygame.transform.flip(PlayerIdle, True, False), (PlayerXCoordinate, PlayerYCoordinate))
            else:
                screen.blit(pygame.transform.flip(PlayerJump, True, False), (PlayerXCoordinate, PlayerYCoordinate))


        # Mouse Position
        mouseXCoordinate, mouseYCoordinate = pygame.mouse.get_pos()


        # Drawing spike and other map obstacles

        if screenHeight + 100 > SpikeY > -101:
            screen.blit(Spike, (SpikeX, SpikeY))
        else:
            SpikeY = -100
            SpikeX = random.randrange(0, screenWidth)
        SpikeY = addToX(SpikeY, screenHeight//100)



        # Draw ghost and initiate movement with player distance

        if (screenWidth // 2) > GhostXCoordinate - PlayerXCoordinate > 55:
            screen.blit(GhostMob[1], (GhostXCoordinate, GhostYCoordinate))
            if GhostXCoordinate - PlayerXCoordinate > 55:
                GhostXCoordinate = addToX(GhostXCoordinate, -3)

        elif GhostXCoordinate - PlayerXCoordinate < -30:
            screen.blit(pygame.transform.flip(GhostMob[1], True, False), (GhostXCoordinate, GhostYCoordinate))
            if PlayerXCoordinate - GhostXCoordinate < (screenWidth // 2):
                GhostXCoordinate = addToX(GhostXCoordinate, +3)

        else:
            if GhostXCoordinate - PlayerXCoordinate > 0:
                screen.blit(GhostMob[0], (GhostXCoordinate, GhostYCoordinate))
            else:
                screen.blit(pygame.transform.flip(GhostMob[0], True, False), (GhostXCoordinate, GhostYCoordinate))

        # End of Draw ghost and initiate movement with player distance




        # Player left and right movement

        keyPressed = pygame.key.get_pressed()
        mouseClick = pygame.mouse.get_pressed()

        if mouseClick[0] or mouseClick[2]:
            if mouseXCoordinate < (2.5 * screenWidth) / 10:
                FacingRight = False
                PlayerXCoordinate = addToX(PlayerXCoordinate, -5)
            elif (2.5 * screenWidth) / 10 < mouseXCoordinate < (5 * screenWidth) / 10:
                FacingRight = True
                PlayerXCoordinate = addToX(PlayerXCoordinate, 5)


        if keyPressed[pygame.K_d] or keyPressed[pygame.K_RIGHT]:
            FacingRight = True
            if PlayerXCoordinate != screenWidth-60:
                PlayerXCoordinate = addToX(PlayerXCoordinate, 5)


        elif keyPressed[pygame.K_a] or keyPressed[pygame.K_LEFT]:
            FacingRight = False
            if PlayerXCoordinate != 0:
                PlayerXCoordinate = addToX(PlayerXCoordinate, -5)

        # End of Player left and right movement





        # Player Jump
        if PlayerYCoordinate == rescaleImagePosByY(439) or PlayerYCoordinate < rescaleImagePosByY(439):
            if keyPressed[pygame.K_SPACE] or (mouseXCoordinate > (7.5 * screenWidth) / 10 < mouseXCoordinate < screenWidth):
                if mouseClick[0] or mouseClick[2] or keyPressed[pygame.K_SPACE]:
                    isJumping = True

        if isJumping:
            if PlayerYCoordinate < rescaleImagePosByY(750):
                PlayerYCoordinate -= JumpVelocity
                JumpVelocity -= JumpAccelerator
            else:
                PlayerYCoordinate += JumpVelocity
                JumpVelocity += JumpAccelerator
        if PlayerYCoordinate == rescaleImagePosByY(439):
            isJumping = False
            JumpVelocity = int(rescaleImagePosByY(18))
            JumpAccelerator = rescaleImagePosByY(1)

        # End of Player Jump


        # Randomly Spawning Coin
        screen.blit(coin, (coinXCoordinate, coinYCoordinate))
        if abs(PlayerXCoordinate - coinXCoordinate) < 30 and abs(PlayerYCoordinate - coinYCoordinate) < 30:
            coinXCoordinate = random.randrange(0, screenWidth)
            coinYCoordinate = random.randrange(screenHeight//4, (screenHeight // 2))
            score += 1




        pygame.display.update()

        clock.tick(60)                  # Frame rate = 60


        # Exit game with ESC
        if keyPressed[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
