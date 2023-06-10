import pygame
import os
from button import Button

class UI:

    def __init__(self, x, y, width, height, image):
        self.image = pygame.transform.scale(image, (int(width), int(height)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.tow1_btn_img = pygame.image.load(os.path.join("..\Grafika", "tow1_btn.png"))
        self.tow1_btn = Button(self.rect.x + width // 2, self.rect.y + 50, 50, 50, self.tow1_btn_img)


# (self, x, y, width, height, image):
    def draw(self, win):
        # action = False
        #get mouse position
        # pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        # if self.rect.collidepoint(pos):
        #     if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        #         self.clicked = True
        #         action = True
        #
        # if pygame.mouse.get_pressed()[0] == 0:
        #     self.clicked = False

        #draw UI on screen
        # win.blit(self.image, (self.rect.x, self.rect.y))


        # added
        # image = pygame.transform.scale(image, (int(width), int(height)))
        # rect = image.get_rect()
        # rect.topleft = (x, y)

        win.blit(self.image, (self.rect.x, self.rect.y))
        self.tow1_btn.draw(win)


    def place_mode(self):
        mode = 0

        if self.tow1_btn.clicked_n_released():
            mode = 1

        return mode



        # if tow1_btn.draw(win) and not self.clicked:
        #     self.clicked = True
        #     self.tow1_place_mode = not self.tow1_place_mode
        #
        # if not tow1_btn.draw(win):
        #     self.clicked = False
        #
        # print(self.tow1_place_mode)
