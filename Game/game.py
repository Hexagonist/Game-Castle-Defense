import os.path
import pygame
import os
from Enemies.Grey import Grey
from Towers.Tower_1 import Tower_1

# pygame.init() !!!!!!!!!!!!
class Game:
    def __init__(self):
        self.game_active = False
        self.menu = True
        self.width = 1200
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.mouse_pos = (0, 0)
        self.enemys = []
        self.towers = []
        self.tow = Tower_1
        self.wave_0 = 4
        self.spawn_cntr = 0
        self.fps = 60
        self.cur_delay = 0
        self.x = 0
        self.towers = []
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("D:\Projects\TowerDefenseGamePJS\Grafika", "Mapa0.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.end_map = pygame.image.load(os.path.join("D:\Projects\TowerDefenseGamePJS\Grafika", "Koniec.png"))
        self.menu_map = pygame.image.load(os.path.join("D:\Projects\TowerDefenseGamePJS\Grafika", "Menu.png"))



    def run(self):
        run = True
        clock = pygame.time.Clock()
        # self.create_wave()
        while run:
            clock.tick(self.fps)
            # self.tow.x, self.tow.y = pygame.mouse.get_pos()
            # px, py = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                # if event.type == pygame.MOUSEMOTION:
                #     # self.tow = Tower_1
                #     # self.tow.x, self.tow.y = event.pos
                #     # self.mouse_pos = event.pos
                #     # print(self.mouse_pos)
                #     # print(self.tow.x, self.tow.y)
                #     # print(self.tow.x, self.tow.y)
                #     print(event.pos)
                if self.game_active == True:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # self.tow.reload()
                        # pygame.draw.rect(self.win, (255, 255, 255), (100, 100, 10, 10))
                        print("DOWN")
                        tow = Tower_1()
                        tow.x, tow.y = pygame.mouse.get_pos()
                        self.towers.append(tow)
                        print("tow.x = "+ str(tow.x))
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for en in self.enemys:
                            self.enemys.remove(en)
                        for tow in self.towers:
                            self.towers.remove(tow)
                        self.spawn_cntr = 0
                        self.game_active = True

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
                    if en.x > 1169:
                        to_del.append(en)

                # delete all enemies off the screen
                for d in to_del:
                    self.enemys.remove(d)

                # creates wave of enemies

                if (self.cur_delay >= self.fps) and (self.spawn_cntr < self.wave_0):
                    self.enemys.append(Grey())
                    self.spawn_cntr += 1
                    self.cur_delay = 0
                else:
                    self.cur_delay += 1



                for en in self.enemys:
                    if en.x >= self.width-200:
                        self.game_active = False


            self.draw()


        pygame.quit()

    def draw(self):
        if self.game_active == True:

            self.win.blit(self.bg, (0,0))

            print("T = " + str(len(self.towers)))
            print("E = " + str(len(self.enemys)))

            # Draw towers
            for tow in self.towers:
                tow.draw(self.win)
            # Draw enemies
            for en in self.enemys:
                en.draw(self.win)
            pygame.display.update()

        else:
            # if self.menu:
            self.win.blit(self.menu_map, (0, 0))
            pygame.display.update()
            # else:
            #     self.win.blit(self.end_map, (0, 0))
            #     pygame.display.update()




    # def tow_add(self):
    #     print(self.tow.x, self.tow.y)
    #     self.towers.append(self.tow())

    # def tow_place(self, tow):



    # def create_wave(self):
    #     for i in range(len(self.enemys)):
    #         self.enemys[i].x += 30 * i





g = Game()
g.run()