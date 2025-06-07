import pygame
from constants import *

class ScoreText:
    def __init__(self, font_size=48, color="white", position=(SCREEN_WIDTH // 2, 30), font_name=None):
        self.font = pygame.font.SysFont(font_name, font_size)
        self.color = color
        self.position = position
        self.score = 0
        self.update_surface()

    def update_surface(self):
        score_string = f"Score: {self.score}"
        self.text_surface = self.font.render(score_string, True, self.color)
        self.text_rect = self.text_surface.get_rect(center=self.position)

    def set_score(self, new_score):
        self.score = new_score
        self.update_surface()

    def draw(self, surface):
        surface.blit(self.text_surface, self.text_rect)