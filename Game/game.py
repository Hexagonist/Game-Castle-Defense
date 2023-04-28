import os.path
import pygame
import os
from Enemies.Grey import Grey


class Game:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = [Grey()]
        self.towers = []
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("D:\Projects\TowerDefenseGamePJS\Grafika", "Mapa0.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))



    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass


            # loop through enemies
            to_del = []
            for en in self.enemys:
                if en.x > 1174:
                    to_del.append(en)

            # delete all enemies off the screen
            for d in to_del:
                self.enemys.remove(d)

            self.draw()


        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))

        # Draw enemies
        for en in self.enemys:
            en.draw(self.win)

        pygame.display.update()

g = Game()
g.run()