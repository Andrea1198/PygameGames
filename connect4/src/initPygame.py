import pygame
width   = ___
height  = ___
screen  = pygame.display.set_mode((width, height))


def start():
    pygame.init()
    pygame.display.set_caption("______")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
