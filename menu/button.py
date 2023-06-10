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

    def draw(self, win, mkey_num=0, button_up_mode=False):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[mkey_num] == 1 and self.clicked == False:
                self.clicked = True
                if not button_up_mode:
                    action = True

            if pygame.mouse.get_pressed()[mkey_num] == 0 and button_up_mode and self.clicked:
                print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                action = True
                self.clicked = False
            # if pygame.mouse.get_pressed()[mkey_num] == 1 and self.clicked == False and button_up_mode:
            #     self.clicked = True

            # if pygame.mouse.get_pressed()[mkey_num] == 1 and button_up_mode:

        if pygame.mouse.get_pressed()[mkey_num] == 0 and not button_up_mode:
            if not button_up_mode:
                self.clicked = False

        # if pygame.mouse.get_pressed()[mkey_num] == 0 and self.clicked and button_up_mode:
        #     action = True
        #     self.clicked = False




        #draw button on screen
        win.blit(self.image, (self.rect.x, self.rect.y))

        return action


    def clicked_n_released(self, mkey_num=0):
        cliked = False
        released = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[mkey_num] == 1 and self.clicked == False:
                self.clicked = True
                if not button_up_mode:
                    action = True

        return True