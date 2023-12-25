import pygame
import time

from main import Backs
from backward import moveInterval

Main=Backs()

#以下为主函数
def run():
    Main.init()
    #用于初始化画面
    
    moveTimer=time.perf_counter()
    #用于隔一段时间使得蛇向当前方向前进一步
    
    running=True
    #用于表示运行状态
    while running:
        if pygame.event.peek(pygame.QUIT) or Main.checkFoodEaten():
            running=False
        keys = pygame.key.get_pressed()
        
        #keys是一个元素为bool类型的元组，可以通过对应的键值得到一个按键是否按下
        #具体用法为keys[pygame.按键码]，会返回一个bool类型的值表示该按键是否按下
        #按键码请参考list.txt文本文件
        
        #你可以通过以下若干个函数对贪吃蛇进行操作
        #Main.MoveUp()使蛇头向上转
        #Main.MoveDown()使蛇头向下转
        #Main.MoveLeft()使蛇头向左转
        #Main.MoveRight()使蛇头向右转
        
        
        if time.perf_counter()-moveTimer>moveInterval:
            moveTimer=time.perf_counter()
            Main.moveSnake()
        #用于使贪吃蛇向当前方向移动一步
            
        Main.update()
        #用于更新画面
    pygame.quit()
    #用于退出


if __name__=='__main__':
    run()