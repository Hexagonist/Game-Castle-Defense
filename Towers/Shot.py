import os
import pygame

class Shot:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.width = 10
        self.height = 10
        self.img = pygame.image.load(os.path.join("..\Grafika\Towers_textures\Shot_0.png"))



    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        # self.img = self.imgs[self.animation_count]
        #
        # self.img = self.imgs[self.animation_count]
        # if self.animation_count >= len(self.imgs):
        #     self.animation_count = 0
        # self.animation_count += 1 #!



        self.rec = self.img.get_rect(center=(self.x, self.y))
        win.blit(self.img, self.rec)

    def move(self):
        """
        Move Shot
        :return: None
        """
        # self.x += self.vel
        self.x = int(self.path[self.mov_pos][0])
        self.y = int(self.path[self.mov_pos][1])
        self.mov_pos += self.vel