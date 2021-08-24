import src.functions as f
import src.colors as c
import numpy as np
import pygame

WIDTH   = 480
HEIGHT  = 480
c1      = c.LIGHT_BROWN
c2      = c.DARK_BROWN
cm      = c.LIGHT_BLUE
grid    = f.create_grid()
pieces  = f.get_pieces()

pygame.init()
# f.crop_pieces("Images/pieces.png")
screen  = pygame.display.set_mode((WIDTH, HEIGHT))
l       = WIDTH//8
cell    = pygame.Surface((l,l))
running = True
n1      = 0
counter = 0
while running:
    # moves = f.possible_moves(n, grid)
    f.show_grid(WIDTH, HEIGHT, c1, c2, screen, grid, pieces, n1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if pygame.mouse.get_pressed()[0] and counter == 0:
            xmouse, ymouse = pygame.mouse.get_pos()
            i = xmouse*8//WIDTH
            j = ymouse*8//WIDTH
            n1 = j*8+i
            counter = 1
            pygame.time.delay(100)
            # while pygame.MOUSEBUTTONUP:
            #     pygame.time.wait(1)
        elif pygame.mouse.get_pressed()[0] and counter == 1:
            xmouse, ymouse = pygame.mouse.get_pos()
            i = xmouse*8//WIDTH
            j = ymouse*8//WIDTH
            n2 = j*8+i
            if n1 != n2:
                f.move(grid, n1, n2)
            counter = 0
            n1 = 0
            pygame.time.delay(100)


    pygame.display.update()
