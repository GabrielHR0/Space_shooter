import pygame
from os.path import join
from scripts.settings import *

class Player():
    def __init__(self):
        self.player_surface = pygame.image.load(join('assets', 'images', 'player.png')).convert_alpha()
        self.player_rect = self.player_surface.get_frect(topleft =(0,0))
    
    def draw_player(self, display_surface):
        display_surface.blit(self.player_surface, self.player_rect)
    
    def move_player(self):
        player_direction = 1
        if self.player_rect.right < window_width:
            self.player_rect.left += player_direction * 5
        else:
            player_direction = - 1

class Laser():
    def __init__(self):
        self.laser_surface = pygame.image.load(join('assets', 'images', 'laser.png')).convert_alpha()
        self.laser_rect = self.laser_surface.get_frect(bottomleft = (20, window_height-20))
    
    def draw_laser(self,display_surface):
        display_surface.blit(self.laser_surface, self.laser_rect)