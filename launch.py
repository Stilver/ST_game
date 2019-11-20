import pygame
from settings.color import WHITE, BLACK
from settings.settings_reader import SETTINGS
from objects.menu.main_menu import Button


pygame.init()
clock = pygame.time.Clock()

main_surf = pygame.display.set_mode(SETTINGS.get('RESOLUTION'))
window_center = SETTINGS.get('RESOLUTION')[0] // 2, SETTINGS.get('RESOLUTION')[1] // 2

game_started = False

while True:
    current_objects = []
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    if not game_started:
        mouse_key_state = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        start_button = Button(main_surf, 'START', window_center[0], 50, 80, 30, WHITE)
        quit_button = Button(main_surf, 'QUIT', window_center[0], 100, 80, 30, WHITE)
        start_button.draw()
        quit_button.draw()
        current_objects.append(start_button.rect)
        current_objects.append(quit_button.rect)
        if start_button.rect.collidepoint(mouse_pos) and mouse_key_state[0]:
            game_started = True
        if quit_button.rect.collidepoint(mouse_pos) and mouse_key_state[0]:
            print('quitting...')
            exit()
    else:
        main_surf.fill(BLACK)

    if not current_objects:
        pygame.display.update()
    else:
        pygame.display.update(current_objects)
    clock.tick(SETTINGS.get('FPS'))
