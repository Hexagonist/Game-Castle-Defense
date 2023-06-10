import pygame
from button import Button

class UI:

    def __init__(self, x, y, width, height, image):
        self.image = pygame.transform.scale(image, (int(width), int(height)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False


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
        win.blit(self.image, (self.rect.x, self.rect.y))