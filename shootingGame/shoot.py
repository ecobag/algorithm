import pygame
import sys
from time import sleep

BLACK = (0,0,0)
padWidth = 480
padHeight = 640

# initialize variables
def initGame():
    global gamepad, clock
    pygame.init()
    gamepad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('Pyshooting')
    clock = pygame.time.Clock()


# Game logic
def runGame():
    global gamepad, clock
    
    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
        
        gamepad.fill(BLACK)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()


initGame()
runGame()