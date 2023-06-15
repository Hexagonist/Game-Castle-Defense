import pygame

# Button class
class Button:

    def __init__(self, x, y, width, height, image, memory=False, mkey_num=0):
        self.x = x
        self.y = y
        self.x = x
        self.image = pygame.transform.scale(image, (int(width), int(height)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.memory = memory
        self.clicked = False
        self.pushed = False

    #draw button on screen
    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))

    def click_check(self, mkey_num=0):
        # get mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[mkey_num] and not self.clicked:
            self.clicked = True
            print("pressed")
            return True

        if (self.rect.collidepoint(pos) and not pygame.mouse.get_pressed()[mkey_num]) and self.clicked:  #or (not self.rect.collidepoint(pos)):
            self.clicked = False
            print("released")


