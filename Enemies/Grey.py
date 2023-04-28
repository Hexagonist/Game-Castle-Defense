import os.path
import os
import pygame
from .enemy import Enemy




class Grey(Enemy):
    imgs = []
    imgs.append(pygame.image.load(os.path.join("D:\Projects\TowerDefenseGamePJS\Grafika\Enemies_textures\Grey", "Grey_" + str(x) + ".png"))for x in range(2))


# def __init__(self):
#     super().__init__()