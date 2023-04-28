import pygame
import math
import os



class Enemy:
    imgs = []
    def __init__(self):
        self.width = 30
        self.height = 30
        self.animation_count = 0
        self.health = 1
        self.path = [(20, 329), (76, 330), (146, 331), (192, 335), (255, 337), (327, 340), (409, 339), (475, 337), (513, 309), (561, 297), (640, 292), (707, 314), (736, 333), (779, 343), (838, 339), (886, 339), (981, 330), (1031, 330), (1174, 341)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.vel = 3
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0


    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        # self.img = self.imgs[self.animation_count]
        #
        self.animation_count += 1 #!
        self.img = self.imgs[self.animation_count]
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0



        win.blit(self.img, (self.x, self.y))
        self.move()
        pass # !!!!

    def collide(self, X, Y):
        """
        Returns if position has hit enemy
        :param x: int
        :param y: int
        :return: Bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def move(self):
        """
        Move enemy
        :return: None
        """
        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (1474, 341)
        else:
            x2, y2 = self.path[self.path_pos+1]

        move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


        self.move_count += 1
        dirn = (x2 - x1, y2 - y1)


        move_x, move_y = (self.x + dirn[0] * self.move_count, self.y + dirn[1] * self.move_count)
        self.dis += math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2)

        # Go to next point
        if self.dis >= move_dis:
            self.dis = 0
            self.move_count = 0
            self.path_pos += 1
            if self.path_pos >= len(self.path):
                return False

        self.x = move_x
        self.y = move_y
        return True

    def hit(self):
        """
        Returns if an enemy has died and removes one health
        each call
        :return: Bool
        """
        #self.health -= damage
        if self.health <= 0:
            return True

