import os.path
import os
import pygame
from .Tower import Tower

class Tower_1(Tower):
    def circle_collide(self, en):
        if self.range.collide_point(en.x, en.y):
            en.hp -= 10
            return True
        else:
            return False
    # imgs = []
    # Enemy.imgs.append(pygame.image.load(os.path.join("D:\Projects\TowerDefenseGamePJS\Grafika\Enemies_textures\Grey", "Grey_" + str(x) + ".png"))for x in range(1))
    pass



# def __init__(self):
#     super().__init__()