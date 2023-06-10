import os.path
import pygame
import os

from Enemies.Grey import Grey
from Towers.Tower_1 import Tower_1
from Towers.Shot import Shot
from menu.button import Button
# from menu.UI import UI

# pygame.init() !!!!!!!!!!!!
class Game:
    def __init__(self):
        # Dev Test tools
        self.entieties_num_print = False
        self.mouse_pos_print = False
        self.spawn_wave = True
        self.menu = True

        self.game_active = False
        self.game_over = False
        self.quit = False
        self.width = 1200
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))#, pygame.FULLSCREEN)
        self.mouse_pos = (0, 0)
        self.enemys = []
        self.towers = []
        self.shots = []
        self.tow = Tower_1
        self.wave_0 = 4
        self.spawn_cntr = 0
        self.fps = 60
        self.cur_delay = 0
        self.x = 0
        self.towers = []
        self.lives = 10
        self.money = 100

        # Loading images:
        self.bg = pygame.image.load(os.path.join("..\Grafika", "Mapa1.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.start_button_img = pygame.image.load(os.path.join("..\Grafika", "start_btn.png"))
        self.exit_button_img = pygame.image.load(os.path.join("..\Grafika", "exit_btn.png"))
        self.try_again_button_img = pygame.image.load(os.path.join("..\Grafika", "try_again_btn.png"))
        self.end_map = pygame.image.load(os.path.join("..\Grafika", "Koniec.png"))
        self.menu_map = pygame.image.load(os.path.join("..\Grafika", "Menu.png"))
        self.game_over_map = pygame.image.load(os.path.join("..\Grafika", "GameOver.png"))
        self.pauza_map = pygame.image.load(os.path.join("..\Grafika", "Pauza.png"))
        self.ui_img = pygame.image.load(os.path.join("..\Grafika", "UI_0.png"))

        # Buttons initialisation:
        # Main Menu:
        self.start_button = Button(self.width//2, self.height//2, 200, 100, self.start_button_img)
        self.exit_button = Button(self.width//2, self.height//2 + 120, 200, 100, self.exit_button_img)
        self.try_again_button = Button(self.width//2, self.height//2, 200, 100, self.try_again_button_img)

        # UI :
        self.tow1_btn_img = pygame.image.load(os.path.join("..\Grafika", "tow1_btn.png"))



        # UI initialisation:
        # self.ui = UI(self.width-100, 0, 100, self.height, self.ui_img)



    def run(self):
        run = True
        clock = pygame.time.Clock()
        # self.create_wave()

        while run:
            clock.tick(self.fps)
            # self.tow.x, self.tow.y = pygame.mouse.get_pos()
            # px, py = pygame.mouse.get_pos()
            if self.quit:
                run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    # self.quit = True

                if event.type == pygame.MOUSEMOTION:
                #     # self.tow = Tower_1
                #     # self.tow.x, self.tow.y = event.pos

                # technical help to know mouse coursor position
                    if (self.mouse_pos_print) and (len(self.towers) > 0):
                        self.mouse_pos = event.pos
                        f = open("path_0.txt", "a")
                        f.write(str(self.mouse_pos))
                        f.write("\n")
                #     # print(self.tow.x, self.tow.y)
                #     # print(self.tow.x, self.tow.y)
                #     print(event.pos)
                if self.game_active == True:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # self.tow.reload()
                        # pygame.draw.rect(self.win, (255, 255, 255), (100, 100, 10, 10))
                        if self.entieties_num_print:
                            print("DOWN")
                        tow = Tower_1()
                        tow.x, tow.y = pygame.mouse.get_pos()
                        self.towers.append(tow)

                        # Testing shot
                        self.shots.append(Shot())

                        # technical help to know current number of towers
                        if self.entieties_num_print:
                            print("tow.x = " + str(tow.x))
                #else:
                    # if event.type == pygame.MOUSEBUTTONDOWN:


                        # pygame.quit()
                        # exit()
                    # if event.type == pygame.KEYDOWN:
                    #     if event. == pygame.K_ESCAPE:
                    #         self.menu = True


            if self.game_active == True:
                # loop through enemies
                to_del = []
                for en in self.enemys:
                    for tow in self.towers:
                        if tow.collide(en):
                            to_del.append(en)
                    if en.y > 650:
                        to_del.append(en)

                for en in self.enemys:
                    if en.y >= self.height-50:
                        self.game_active = False
                        self.game_over = True
                        # self.enemys = []
                # delete all enemies off the screen
                for d in to_del:
                    self.enemys.remove(d)

                # creates wave of enemies
                if (self.cur_delay >= self.fps) and (self.spawn_cntr < self.wave_0) and (self.spawn_wave):
                    self.enemys.append(Grey())
                    self.spawn_cntr += 1
                    self.cur_delay = 0
                else:
                    self.cur_delay += 1

                # Deleting all enemys & towers after state 'gameover' true
                if self.game_active == False:
                    for x in self.enemys:
                        if x not in to_del:
                            self.enemys.remove(x)
                    for x in to_del:
                        to_del.remove(x)






            self.draw()


        pygame.quit()

    def draw(self):
        if self.game_active:

            self.win.blit(self.bg, (0,0))
            self.UI_draw(self.width-100, 0, 100, self.height, self.ui_img)

            if self.entieties_num_print:
                # technical help to know current number of towers and enemies
                print("T = " + str(len(self.towers)))
                print("E = " + str(len(self.enemys)))

            # Draw towers
            for tow in self.towers:
                tow.draw(self.win)
            # Draw enemies
            for en in self.enemys:
                en.draw(self.win)
            # Draw shots fired
            for shot in self.shots:
                shot.draw(self.win)

            # Working resume button
            # if self.try_again_button.draw(self.win):
            #     self.game_active = True

            pygame.display.update()



        else:
            if self.game_over:
                self.win.blit(self.game_over_map, (0, 0))
                if self.exit_button.draw(self.win):
                    self.quit = True
                if self.try_again_button.draw(self.win):
                    self.game_over = False

            else:
                self.win.blit(self.menu_map, (0, 0))

                if self.start_button.draw(self.win):
                    for en in self.enemys:  # !!! Probably unwanted enemies removal there
                        self.enemys.remove(en)
                    for tow in self.towers:
                        self.towers.remove(tow)
                    self.spawn_cntr = 0
                    self.game_active = True

                if self.exit_button.draw(self.win):
                    self.quit = True


                # else:
                #     self.win.blit(self.end_map, (0, 0))
                #     pygame.display.update()
            pygame.display.update()


    # Function to draw UI
    def UI_draw(self, x, y, width, height, image):
        image = pygame.transform.scale(image, (int(width), int(height)))
        rect = image.get_rect()
        rect.topleft = (x, y)
        tow1_btn = Button(rect.x + width//2, rect.y + 50, 50, 50, self.tow1_btn_img)

        self.win.blit(image, (rect.x, rect.y))
        tow1_btn.draw(self.win)





    # def tow_add(self):
    #     print(self.tow.x, self.tow.y)
    #     self.towers.append(self.tow())

    # def tow_place(self, tow):



    # def create_wave(self):
    #     for i in range(len(self.enemys)):
    #         self.enemys[i].x += 30 * i





g = Game()
g.run()