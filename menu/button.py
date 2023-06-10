import pygame

# Button class
class Button:

    def __init__(self, x, y, width, height, image):
        # widt = image.get_width()
        # height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width), int(height)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x-width//2, y-height//2)
        self.clicked = False

    def draw(self, win):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        win.blit(self.image, (self.rect.x, self.rect.y))

        return action