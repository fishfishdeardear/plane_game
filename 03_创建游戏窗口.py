import pygame

pygame.init()

# 创建游戏窗口480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# <1 加载图像数据
bg = pygame.image.load("./images/background.png")
# <2 blit绘制图像
screen.blit(bg, (0, 0))
# <3 update更新屏幕显示
# 可以在screen对象完成所有blit后再更新屏幕
pygame.display.update()


# 绘制英雄的飞机
hero = bg = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))
pygame.display.update()

while True:
    pass


pygame.quit()