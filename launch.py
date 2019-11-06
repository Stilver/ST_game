import pygame
from settings.color import WHITE
from settings.settings_reader import SETTINGS

pygame.init()
clock = pygame.time.Clock()

main_surf = pygame.display.set_mode(SETTINGS.get('RESOLUTION'))

pygame.draw.rect(main_surf, WHITE, (50, 50, 80, 30))

pygame.display.update()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    clock.tick(SETTINGS.get('FPS'))
