import random
import pygame
from scripts.settings import *
from os.path import join

class Star:
    def __init__(self):
        self.star_pos = []
        self.star_surface = pygame.image.load(join('assets', 'images', 'star.png')).convert_alpha()
        self.generate_star((window_width, window_height))

    def generate_star(self, display_size):
        width, height = display_size  # Obtém a largura e a altura da janela
        self.star_pos = [(random.randrange(0, width, 50), random.randrange(0, height, 50)) for i in range(20)]

    def draw_stars(self, display_surface):
        for pos in self.star_pos:
            display_surface.blit(self.star_surface, pos)
    
class Meteor:
    def __init__(self):
        self.meteor_surface = pygame.image.load(join('assets', 'images', 'meteor.png')).convert_alpha()
        self.meteor_rect = self.meteor_surface.get_frect(center=(window_width/2,window_height/2))
        

    def draw_meteor(self, display_surface):
        display_surface.blit(self.meteor_surface, self.meteor_rect)
 
