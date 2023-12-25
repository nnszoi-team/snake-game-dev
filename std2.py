import pygame
import time

from main import Backs
from backward import moveInterval

#pygame.init()

Main=Backs()

def ifUp():
    #return pygame.event.peek(pygame.KEYDOWN)
    return pygame.key.get_pressed()[pygame.K_UP]

def ifDown():
    return pygame.key.get_pressed()[pygame.K_DOWN]

def ifLeft():
    #return pygame.event.peek(pygame.KEYDOWN)
    return pygame.key.get_pressed()[pygame.K_LEFT]

def ifRight():
    return pygame.key.get_pressed()[pygame.K_RIGHT]
    
def run():
    Main.push(ifUp,Main.moveUp)
    Main.push(ifDown,Main.moveDown)
    Main.push(ifLeft,Main.moveLeft)
    Main.push(ifRight,Main.moveRight)
    
    Main.interfaceRun()


if __name__=='__main__':
    run()