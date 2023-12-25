import pygame
import time
import sys
from threading import Thread,Lock
from pynput import keyboard
from queue import Queue

from backward import block, snake, food
from backward import screenHeight, screenWidth, blockWidth,moveInterval

image = pygame.image.load("wall.png")
image = pygame.transform.scale(image, (blockWidth, blockWidth))
moveTimer=time.perf_counter()

lock = Lock()

pygame.init()

class IF:
    def __init__(self):
        pass
    pass


class Backs:
    def __init__(
        self,
        moveInterval=0.2,
        row=screenWidth // blockWidth,
        column=screenHeight // blockWidth,
    ):
        self.row = row
        self.column = column
        self.turn = "Down"
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        self.Snake = snake(self.screen)
        self.Snake.view()
        self.moveInterval = moveInterval
        self.foods = []
        self.upTimer = time.perf_counter()
        self.downTimer = time.perf_counter()
        self.leftTimer = time.perf_counter()
        self.rightTimer = time.perf_counter()
        
        self.operations=[]

    def drawMap(self):
        for i in range(self.column):
            self.screen.blit(image, (0, i * blockWidth))
            pygame.display.flip()
            self.screen.blit(image, ((self.row - 1) * blockWidth, i * blockWidth))
            pygame.display.flip()
        for i in range(self.row):
            self.screen.blit(image, (i * blockWidth, 0))
            pygame.display.flip()
            self.screen.blit(image, (i * blockWidth, (self.column - 1) * blockWidth))
            pygame.display.flip()

    # def quiter(self):

    def rectorCheck(self)->bool:
        for i in range(len(self.Snake.body)):
            if self.Snake.body[i].y * blockWidth < blockWidth:
                #print(21)
                return True
            if self.Snake.body[i].y * blockWidth >= screenHeight - blockWidth:
                #print(21)
                return True
            if self.Snake.body[i].x * blockWidth < blockWidth:
                #print(21)
                return True
            if self.Snake.body[i].x * blockWidth >= screenWidth - blockWidth:
                #print(21)
                return True
            for j in range(len(self.Snake.body)):
                if i == j:
                    continue
                if (
                    self.Snake.body[i].x == self.Snake.body[j].x
                    and self.Snake.body[i].y == self.Snake.body[j].y
                ):
                    #print(2)
                    return True
        return False

    def moveSnake(self):
        if self.turn == "Up":
            self.Snake.movement(0, -1)
        if self.turn == "Down":
            self.Snake.movement(0, 1)
        if self.turn == "Left":
            self.Snake.movement(-1, 0)
        if self.turn == "Right":
            self.Snake.movement(1, 0)

    def moveUp(self):
        if (
            time.perf_counter() - self.upTimer <= self.moveInterval
            or self.turn == "Down"
        ):
            return
        self.upTimer = time.perf_counter()
        self.Snake.movement(0, -1)
        self.turn = "Up"

    def moveDown(self):
        if (
            time.perf_counter() - self.downTimer <= self.moveInterval
            or self.turn == "Up"
        ):
            return
        self.downTimer = time.perf_counter()
        self.Snake.movement(0, 1)
        self.turn = "Down"

    def moveLeft(self):
        if (
            time.perf_counter() - self.leftTimer <= self.moveInterval
            or self.turn == "Right"
        ):
            return
        self.leftTimer = time.perf_counter()
        self.Snake.movement(-1, 0)
        self.turn = "Left"

    def moveRight(self):
        if (
            time.perf_counter() - self.rightTimer <= self.moveInterval
            or self.turn == "Left"
        ):
            return
        self.rightTimer = time.perf_counter()
        self.Snake.movement(1, 0)
        self.turn = "Right"

    def init(self, foodNum=1):
        self.drawMap()
        for i in range(foodNum):
            self.foods.append(food(self.screen))

    def checkFoodEaten(self)->bool:
        if self.rectorCheck():
            return True
        while True:
            eatfood = False
            for i in range(len(self.foods)):
                if (
                    self.Snake.body[0].x == self.foods[i].x
                    and self.Snake.body[0].y == self.foods[i].y
                ):
                    self.Snake.getLonger = True
                    del self.foods[i]
                    eatfood = True
                    break
            if eatfood == True:
                self.foods.append(food(self.screen, self.Snake.body))
            else:
                return 
        return False

    def update(self):
        for element in self.foods:
            element.view()
        self.Snake.view()
        pygame.display.flip()
        
    def backRun(self):
        global moveTimer
        with lock:
            if pygame.event.peek(pygame.QUIT) or self.checkFoodEaten():
                return
            self.moveSnake()
            self.update()
    
    def push(self,condition=None,operator=None):
        self.operations.append([condition,operator])
        pass
    
    def doSth(self,condition=None,operator=None):
        with lock:
            if pygame.event.peek(pygame.QUIT) or self.checkFoodEaten():
                return
            if condition():
                operator()
                #pygame.display.flip()
        return
    
    def interfaceRun(self):
        global moveTimer
        self.init()
        counter=time.perf_counter()
        moveTimer=time.perf_counter()
        while True:
            if time.perf_counter()-counter>self.moveInterval and pygame.event.peek(pygame.KEYDOWN):
                for i in range(len(self.operations)):
                    outsideRunner=Thread(target=self.doSth,args=(self.operations[i][0],self.operations[i][1]))
                    outsideRunner.start()
                counter=time.perf_counter()
            if time.perf_counter()-moveTimer>moveInterval:
                backrunner=Thread(target=self.backRun,args=())
                backrunner.start()
                moveTimer=time.perf_counter()
            
        
        
