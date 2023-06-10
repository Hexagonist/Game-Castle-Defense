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
        self.x = 30 # self.path[0][0]
        self.y = 300 # self.path[0][1]
        # self.path = [(20, 329), (76, 330), (146, 331), (192, 335), (255, 337), (327, 340), (409, 339), (475, 337), (513, 309), (561, 297), (640, 292), (707, 314), (736, 333), (779, 343), (838, 339), (886, 339), (981, 330), (1031, 330), (1169, 341)]
        self.img = pygame.image.load(os.path.join("..\Grafika\Enemies_textures\Grey\Grey_0.png"))
        self.img_rec = self.img.get_rect(center = (self.x, self.y))
        self.dis = 0
        self.vel = 5    # default for first movement =5
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0
        self.path = []
        self.mov_pos = 0
        f = open("path_0.txt", "r")
        # Enemy move path builder
        for coordinates in f:
            self.path.append((tuple(coordinates[1:-2].rsplit(", "))))
        self.x = int(self.path[0][0])
        self.y = int(self.path[0][1])


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


        win.blit(self.img, ((self.x-self.width//2), (self.y-self.height//2)))
        self.move()

    def collide(self, X, Y):
        """
        Returns if position has hit enemy
        :param x: int
        :param y: int
        :return: Bool
        """
        # if X <= self.x + self.width and X >= self.x:
        #     if Y <= self.y + self.height and Y >= self.y:
        #         return True
        # return False



    def move(self):
        """
        Move enemy
        :return: None
        """
        # self.x += self.vel
        self.x = int(self.path[self.mov_pos][0])
        self.y = int(self.path[self.mov_pos][1])
        self.mov_pos += self.vel

        # x1, y1 = self.path[self.path_pos]
        # if self.path_pos + 1 >= len(self.path):
        #     x2, y2 = (1474, 341)
        # else:
        #     x2, y2 = self.path[self.path_pos+1]
        #
        # move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        #
        #
        # self.move_count += 1
        # dirn = (x2 - x1, y2 - y1)
        #
        #
        # move_x, move_y = (self.x + dirn[0] * self.move_count, self.y + dirn[1] * self.move_count)
        # self.dis += math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2)
        #
        # # Go to next point
        # if self.dis >= move_dis:
        #     self.dis = 0
        #     self.move_count = 0
        #     self.path_pos += 1
        #     if self.path_pos >= len(self.path):
        #         return False
        #
        # self.x = move_x
        # self.y = move_y
        # return True




    def hit(self):
        """
        Returns if an enemy has died and removes one health
        each call
        :return: Bool
        """
        #self.health -= damage
        if self.health <= 0:
            return True

