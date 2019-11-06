import pygame
from settings.color import WHITE


class Button:
    def __init__(self, surf, text, x, y, width, height, color=WHITE):
        self.surf = surf
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        pygame.draw.rect(self.surf, self.color, (self.x, self.y, self.width, self.height))
