import pygame
from settings.color import WHITE, BLACK


class Button:
    def __init__(self, surf, text, x, y, width, height, color=WHITE):
        self.surf = surf
        self.text = text
        self.x = self.center_pos(x, width)
        self.y = self.center_pos(y, height)
        self.width = width
        self.height = height
        self.color = color

    def center_pos(self, coordinate, value):
        return coordinate - value // 2

    def draw(self):
        surface = pygame.Surface((self.width, self.height))
        surface.fill(WHITE)

        text = pygame.font.Font(None, 35)
        text_surf = text.render(self.text, 1, BLACK)
        text_pos = text_surf.get_rect(center=(self.width // 2, self.height // 2))
        surface.blit(text_surf, text_pos)

        self.rect = surface.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.surf.blit(surface, self.rect)
