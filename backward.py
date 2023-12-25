import pygame
import random

initialSnakeBlocks = 3
blockWidth = 20
screenWidth = 800
screenHeight = 600
moveInterval = 0.25
background_color = (0, 0, 0)

image = pygame.image.load("body.png")
image = pygame.transform.scale(image, (blockWidth, blockWidth))


class food:
    def __init__(self, parent=None, limit=[], randomPlace=True, x=0, y=0):
        self.parent = parent
        self.limit = limit
        if randomPlace:
            while True:
                checker = True
                x = random.randint(1, screenWidth // blockWidth - 2)
                y = random.randint(1, screenHeight // blockWidth - 2)
                for body in limit:
                    if x == body.x and y == body.y:
                        checker = False
                        break
                if checker:
                    break
        self.x = x
        self.y = y
        self.view()

    def view(self):
        foodImage = pygame.image.load("food.png")
        foodImage = pygame.transform.scale(foodImage, (blockWidth, blockWidth))
        self.parent.blit(foodImage, (self.x * blockWidth, self.y * blockWidth))
        self.parent.blit(foodImage, (self.x * blockWidth, self.y * blockWidth))
        pygame.display.flip()


class block:
    def __init__(
        self, x=0, y=0, parent=pygame.display.set_mode((screenWidth, screenHeight))
    ):
        self.parent = parent
        self.x = x
        self.y = y
        self.view()

    def clear(self):
        self.parent.fill(
            background_color,
            (self.x * blockWidth, self.y * blockWidth, blockWidth, blockWidth),
        )
        pygame.display.update(
            pygame.Rect(
                self.x * blockWidth, self.y * blockWidth, blockWidth, blockWidth
            )
        )

    def view(self):
        self.parent.blit(image, (self.x * blockWidth, self.y * blockWidth))
        pygame.display.update(
            pygame.Rect(
                self.x * blockWidth, self.y * blockWidth, blockWidth, blockWidth
            )
        )

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y


class snake:
    def __init__(self, parent=None, x=0, y=5):
        self.parent = parent
        self.body = []
        self.getLonger = False
        for i in range(initialSnakeBlocks):
            self.body.append((block(x + i + 1, y, self.parent)))

    def movement(self, dx=0, dy=0):
        # if (self.body[0].x+dx)*blockWidth<blockWidth or (self.body[0].x+dx)*blockWidth>screenWidth-2*blockWidth:
        # return
        # if (self.body[0].y+dy)*blockWidth<blockWidth or (self.body[0].y+dy)*blockWidth>screenHeight-2*blockWidth:
        # return
        # element=self.body[len(self.body)-1]
        if self.getLonger == False:
            self.body[len(self.body) - 1].clear()
            del self.body[len(self.body) - 1]
        self.getLonger = False
        self.body.insert(0, block(self.body[0].x + dx, self.body[0].y + dy))
        self.body[0].view()

    def view(self):
        for element in self.body:
            element.clear()
            element.view()
