import pygame
from scripts.settings import *
from scripts.player import Player, Laser
from scripts.tilemap import Star, Meteor

class Game:
    def __init__(self):
        self.display_surface = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Hot Line Moscow")
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.star = Star()
        self.meteor = Meteor()
        self.laser = Laser()

    def run(self):
        while self.running:
            self.clock.tick(fps)
            self.events()
            self.draw()

    def update(self):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.display_surface.fill(BACKGROUND_COLOR)
        self.player.draw_player(self.display_surface)
        self.star.draw_stars(self.display_surface)
        self.meteor.draw_meteor(self.display_surface)
        self.laser.draw_laser(self.display_surface)
        self.player.move_player()
        pygame.display.flip()
