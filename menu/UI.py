import pygame
import os
from menu.button import Button


class Panel:

    def __init__(self, x, y, width, height, img):
        self.x = x
        self.y = y

        self.img = pygame.transform.scale(img, (width, height))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)


    def draw(self, win):
        win.blit(self.img, (self.rect.x, self.rect.y))



class Res_indicator:

    def __init__(self, x, y, text, font, color):
        self.x = x
        self.y = y
        self.font = font
        self.color = color
        self.text = text

    def draw(self, win):
        img = self.font.render(self.text, True, self.color)
        win.blit(img, (self.x, self.y))



class UI:

    def __init__(self, x, y, width, height, r_panel, up_panel, font, coins, level):
        self.ui_font = font

        self.image = pygame.transform.scale(r_panel, (int(width), int(height)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.up_panel = Panel(0, 0, 1600, 30, up_panel)

        self.clicked = False

        self.coins_num = coins
        self.level_num = level
        # self.coins = Res_indicator(10, 5, "Coins: " + str(self.coins_num), self.ui_font, (0, 0, 0))
        self.tow1_btn_img = pygame.image.load(os.path.join("..\Grafika", "tow1_btn.png"))
        self.tow1_btn = Button(self.rect.x+width//2-25, self.rect.y+25, 50, 50, self.tow1_btn_img, True)




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
        self.up_panel.draw(win)

        coins = Res_indicator(10, 5, "Coins: " + str(self.coins_num), self.ui_font, (0, 0, 0))
        coins.draw(win)
        wave = Res_indicator(150, 5, "Wave: " + str(self.level_num), self.ui_font, (0, 0, 0))
        wave.draw(win)

        self.tow1_btn.draw(win)



        # if tow1_btn.draw(win) and not self.clicked:
        #     self.clicked = True
        #     self.tow1_place_mode = not self.tow1_place_mode
        #
        # if not tow1_btn.draw(win):
        #     self.clicked = False
        #
        # print(self.tow1_place_mode)

    def update(self, coins, level):
        self.coins_num = coins
        self.level_num = level