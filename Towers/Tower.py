import math
import os.path
import os
import pygame

class Circle_range:
    def __init__(self, color, x, y, r):
        self.color = color
        self.center = (x, y)
        self.r = r
        self.x = x
        self.y = y

    def draw(self, win):

        pygame.draw.circle(win, self.color, self.center, self.r)

    def collide_point(self, x, y):
        if math.sqrt(pow(self.x-x,2)+pow(self.y-y,2)) < self.r:
            return True
        else:
            return False

class Tower:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 300
        self.y = 100
        self.animation_count = 0
        self.range_val = 100
        self.img = pygame.image.load(os.path.join("..\Grafika\Towers_textures\Tower_1_1.png"))
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.rec = self.img.get_rect(center = (self.x, self.y))
        # self.range = pygame.image.load(os.path.join("..\Grafika\Towers_textures\Range.png"))
        self.range = Circle_range((192,192,192), self.x, self.y, self.range_val)
        # self.range = pygame.transform.scale(self.range, (300, 300))
        # self.range_rec = self.range.get_rect(center = (self.x, self.y))
        # self.range = pygame.transform.scale(self.range, (self.width*2, self.height*2))


    # def reload(self):
    #     self.rec = self.img.get_rect(center = (self.x, self.y))



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
        self.range.x, self.range.y = self.rec.x+25, self.rec.y+25
        self.range.center = self.rec.x+25, self.rec.y+25
        self.range.draw(win)
        # self.range_rec = self.range.get_rect(center = (self.x, self.y))
        # win.blit(self.range, self.range_rec)
        win.blit(self.img, self.rec)

    def circle_collide(self, en):
        return self.range.collide_point(en.x, en.y)

    # def collide(self, en):
    #     """
    #     Returns if position has hit enemy
    #     :param x: int
    #     :param y: int
    #     :return: Bool
    #     """
    #
    #     x = en.x
    #     y = en.y
    #     if self.range_rec.collidepoint(x, y):
    #         return True
    #     else:
    #         return False




        # if self.range_rec.collidepoint(X, Y): return True
        # return False
        # if X <= self.x + self.width and X >= self.x:
        #     if Y <= self.y + self.height and Y >= self.y:
        #         return True
        # return False