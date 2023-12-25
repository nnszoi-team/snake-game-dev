import pygame
import time

from main import Backs
from backward import moveInterval

Main=Backs()

def run():
    Main.init()
    moveTimer=time.perf_counter()
    running=True
    while running:
        if pygame.event.peek(pygame.QUIT) or Main.checkFoodEaten():
            running=False
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            Main.moveUp()
        if keys[pygame.K_DOWN]:
            Main.moveDown()
        if keys[pygame.K_LEFT]:
            Main.moveLeft()
        if keys[pygame.K_RIGHT]:
            Main.moveRight()
        
        if time.perf_counter()-moveTimer>moveInterval:
            moveTimer=time.perf_counter()
            Main.moveSnake()
            
            
        Main.update()
    pygame.quit()


if __name__=='__main__':
    run()