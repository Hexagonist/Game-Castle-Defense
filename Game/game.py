import os.path
import pygame
import os

from Enemies.Grey import Grey
from Towers.Tower_1 import Tower_1
from Towers.Shot import Shot
from menu.button import Button
from menu.UI import UI
from Enemies.enemy import Health_bar


pygame.init() #!!!!!!!!!!!!

class Base():
    def __init__(self, x, y, width, height, img):
        self.x = x
        self.y = y
        self.img = pygame.transform.scale(img, (width, height))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.hp = 100
        self.health_bar = Health_bar(self.rect.x, self.rect.y, width-20, 5, 100)


    def draw(self, win):
        win.blit(self.img, (self.rect.x, self.rect.y))
        self.health_bar.update(self.x+10, self.y+5, self.hp)
        self.health_bar.draw(win)


    def collide(self, en):

        x = en.x
        y = en.y
        if self.rect.collidepoint(x, y):
            return True
        else:
            return False



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
        self.fps = 60
        self.x = 0
        self.towers = []
        self.lives = 10
        self.coins = 100
        self.game_win = False

        # wave
        self.wave_0 = 4
        self.spawn_cntr = 0
        self.cur_delay = 0
        self.spawn_delay = 0
        self.level = 1


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
        self.win_screen = pygame.image.load(os.path.join("..\Grafika", "Win.png"))


        # Buttons initialisation:
        # Main Menu:
        self.start_button = Button(self.width//2 -100, self.height//2 -50, 200, 100, self.start_button_img)
        self.exit_button = Button(self.width//2 -100, self.height//2 -50 + 120, 200, 100, self.exit_button_img)
        self.try_again_button = Button(self.width//2 -100, self.height//2 -50, 200, 100, self.try_again_button_img)

        # UI :
        self.ui_r_p_img = pygame.image.load(os.path.join("..\Grafika", "UI_0.png"))
        self.ui_up_p_img = pygame.image.load(os.path.join("..\Grafika", "UI_up.png"))
        self.button_collision = False
        self.clicked = False
        self.ui_font = pygame.font.SysFont("Arial", 20)
        self.ui = UI(self.width-100, 0, 100, self.height, self.ui_r_p_img, self.ui_up_p_img,
                     self.ui_font, self.coins, self.level)
        self.tow_place_mode = False
        self.place_mode = 0
        # self.base_pos1 = ()

        self.base_img = pygame.image.load(os.path.join("..\Grafika", "Base.png"))
        self.base = Base(self.width-210, self.height - 100, 100, 100, self.base_img)
        # self.base_gr = pygame.sprite.g


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

                # technical help to know mouse coursor position     D E V
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

                        # /// cutted
                        # if self.entieties_num_print:
                        #     print("DOWN")
                        #
                        # mx, my = pygame.mouse.get_pos()
                        #
                        # if self.tow1_place_mode :#and mx < self.width-100:
                        #     tow = Tower_1()
                        #     tow.x, tow.y = mx, my
                        #     self.towers.append(tow)
                        #     # Testing shot
                        #     self.shots.append(Shot())
                        # /// cutted V

                        # technical help to know current number of towers       D E V
                        if self.entieties_num_print:
                            print("tow.x = " + str(tow.x))

                        # /// HERE ^
                        mx, my = pygame.mouse.get_pos()

                        if self.ui.tow1_btn.click_check():
                            self.tow_place_mode = True
                            self.place_mode = 1
                            self.ui.tow1_btn.click_check()

                        self.ui.tow1_btn.clicked = False
                        if self.ui.tow1_btn.click_check(2):
                            self.tow_place_mode = False
                            self.ui.tow1_btn.click_check(2)

                        if self.tow_place_mode and mx < self.width-100 and self.place_mode == 1 and self.coins >= 100:
                            tow = Tower_1()
                            tow.x, tow.y = mx, my
                            self.towers.append(tow)
                            # Testing shot
                            # self.shots.append(Shot())
                            self.coins -= 100







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
                self.ui.update(self.coins, self.level)

                for en in self.enemys:
                    for tow in self.towers:
                        if tow.circle_collide(en):
                            if en.hp <= 0:
                                self.coins += en.loot
                                if en not in to_del:
                                    to_del.append(en)
                    if en.y > 650:
                        to_del.append(en)
                    if self.base.collide(en):
                        self.base.hp -= en.dmg
                        to_del.append(en)

                for en in self.enemys:
                    if en.y >= self.height-50:
                        self.game_active = False
                        self.game_over = True
                        # self.enemys = []

                if self.base.hp <= 0:
                    self.game_active = False
                    self.game_over = True

                # delete all enemies off the screen
                for d in to_del:
                    self.enemys.remove(d)

                # creates wave of enemies
                if self.level == 1:
                    self.wave_spwn(self.fps, 120, 3)
                elif self.level == 2:
                    self.wave_spwn(self.fps*0.7, 120, 5)
                elif self.level == 3:
                    self.wave_spwn(self.fps/3, 120, 12)
                elif self.level == 4:
                    self.game_win = True
                    self.game_active = False


                # if len(self.enemys) == 0 and :
                #     self.level += 1


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

            self.win.blit(self.bg, (0, 0))
            # self.UI_draw(self.width-100, 0, 100, self.height, self.ui_img)
            self.ui.draw(self.win)

            # if self.placement_mode == 1:



            # technical help to know current number of towers and enemies       D E V
            if self.entieties_num_print:
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


            self.base.draw(self.win)
            pygame.display.update()



        else:
            self.exit_button.clicked = False
            self.try_again_button.clicked = False
            if self.game_over:
                self.win.blit(self.game_over_map, (0, 0))
                self.exit_button.draw(self.win)
                if self.exit_button.click_check():
                    self.quit = True
                    self.exit_button.click_check()

                self.try_again_button.draw(self.win)
                if self.try_again_button.click_check():
                    self.game_reset()
                    self.game_over = False
                    self.tow1_place_mode = False
                    self.try_again_button.click_check()

            elif self.game_win:
                self.win.blit(self.win_screen, (0, 0))

                self.exit_button.draw(self.win)
                if self.exit_button.click_check():
                    self.quit = True
                    self.exit_button.click_check()

                self.try_again_button.draw(self.win)
                if self.try_again_button.click_check():
                    self.game_reset()
                    self.game_over = False
                    self.tow1_place_mode = False
                    self.try_again_button.click_check()

            else:
                self.win.blit(self.menu_map, (0, 0))

                self.start_button.draw(self.win)
                if self.start_button.click_check():
                    self.start_button.click_check()
                    for en in self.enemys:  # !!! Probably unwanted enemies removal there
                        self.enemys.remove(en)
                    for tow in self.towers:
                        self.towers.remove(tow)
                    self.spawn_cntr = 0
                    self.game_active = True

                self.exit_button.draw(self.win)
                if self.exit_button.click_check():
                    self.quit = True
                    self.exit_button.click_check()


                # else:
                #     self.win.blit(self.end_map, (0, 0))
                #     pygame.display.update()
            pygame.display.update()


    def wave_spwn(self, cur_del, delay, en_num):
        # creates wave of enemies
        if (self.cur_delay >= cur_del) and (self.spawn_cntr < en_num) and (self.spawn_wave) and self.spawn_delay > delay:
            en = Grey()
            if self.level == 2:
                en.vel = 15
            elif self.level == 3:
                en.vel = 20
            self.enemys.append(en)
            self.spawn_cntr += 1
            self.cur_delay = 0
        else:
            self.cur_delay += 1
            self.spawn_delay += 1

        if self.spawn_delay >= delay-1 and self.spawn_cntr >= en_num and len(self.enemys) <= 0:
            self.spawn_delay = 0
            self.spawn_cntr = 0
            self.level += 1


    def game_reset(self):
        for en in self.enemys:  # !!! Probably unwanted enemies removal there
            self.enemys.remove(en)
        for tow in self.towers:
            self.towers.remove(tow)
        self.spawn_cntr = 0
        self.base.hp = 100
        self.coins = 100
        self.spawn_delay = 0
        self.level = 1
        self.game_win = False


    # Function to draw UI
    # def UI_draw(self, x, y, width, height, image):
    #
    #
    #     image = pygame.transform.scale(image, (int(width), int(height)))
    #     rect = image.get_rect()
    #     rect.topleft = (x, y)
    #     tow1_btn = Button(rect.x + width//2, rect.y + 50, 50, 50, self.tow1_btn_img)
    #
    #     self.win.blit(image, (rect.x, rect.y))
    #
    #     if tow1_btn.draw(self.win) and not self.clicked:
    #         self.clicked = True
    #         self.tow1_place_mode = not self.tow1_place_mode
    #
    #
    #
    #     if not tow1_btn.draw(self.win):
    #         self.clicked = False
    #
    #     print(self.tow1_place_mode)




    # def tow_add(self):
    #     print(self.tow.x, self.tow.y)
    #     self.towers.append(self.tow())

    # def tow_place(self, tow):



    # def create_wave(self):
    #     for i in range(len(self.enemys)):
    #         self.enemys[i].x += 30 * i





g = Game()
g.run()