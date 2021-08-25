import src.functions as f
import src.colors as c
from src.moves import check_bounds
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
f.crop_pieces("Images/pieces.png")
screen  = pygame.display.set_mode((WIDTH, HEIGHT))
l       = WIDTH//8
cell    = pygame.Surface((l,l))
running = True
counter = 0
n1      = [0, 0]
moves   = []
player = 0
rook1Moved  = [False, False]
rook2Moved  = [False, False]
kingMoved   = [False, False]
while running:
    # moves = f.possible_moves(n, grid)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if player == 0:
        if pygame.mouse.get_pressed()[0] and counter == 0:
            xmouse, ymouse = pygame.mouse.get_pos()
            i1 = xmouse*8//WIDTH
            j1 = ymouse*8//WIDTH
            n1 = [i1, j1]
            if check_bounds(grid[j1, i1], 1, 7):
                counter = 1
                moves = f.possible_moves(grid, i1, j1, rook1Moved, rook2Moved, kingMoved)
                print("Final moves", moves)
            pygame.time.delay(100)

            # while pygame.MOUSEBUTTONUP:
            #     pygame.time.wait(1)
        elif pygame.mouse.get_pressed()[0] and counter == 1:
            xmouse, ymouse = pygame.mouse.get_pos()
            i2 = xmouse*8//WIDTH
            j2 = ymouse*8//WIDTH
            if i1 != i2 or j1 != j2:
                if  [i2, j2] in moves:
                    f.move(grid, i1, j1, i2, j2, l)
                    if grid[j1, i1] == 1:
                        kingMoved[0] = True
                        if grid[j1, i1] == 6:
                            if i1 == 0:
                                rook1Moved[0] = True
                            elif i1 == 7:
                                rook2Moved[0] = True
                    player = 1
            counter = 0
            moves = []
            pygame.time.delay(100)
    if player == 1:
        if pygame.mouse.get_pressed()[0] and counter == 0:
            xmouse, ymouse = pygame.mouse.get_pos()
            i1 = xmouse*8//WIDTH
            j1 = ymouse*8//WIDTH
            n1 = [i1, j1]
            if check_bounds(grid[j1, i1], 7, 13):
                counter = 1
                moves = f.possible_moves(grid, i1, j1, rook1Moved, rook2Moved, kingMoved)
            pygame.time.delay(100)

            # while pygame.MOUSEBUTTONUP:
            #     pygame.time.wait(1)
        elif pygame.mouse.get_pressed()[0] and counter == 1:
            xmouse, ymouse = pygame.mouse.get_pos()
            i2 = xmouse*8//WIDTH
            j2 = ymouse*8//WIDTH
            if i1 != i2 or j1 != j2:
                if  [i2, j2] in moves:
                    f.move(grid, i1, j1, i2, j2, l)
                    if grid[j1, i1] == 7:
                        kingMoved[1] = True
                    if grid[j1, i1] == 11:
                        if i1 == 0:
                            rook1Moved[1] = True
                        elif i1 == 7:
                            rook2Moved[1] = True
                    player = 0
            counter = 0
            moves = []
            pygame.time.delay(100)

    f.show_grid(WIDTH, HEIGHT, c1, c2, screen, grid, pieces, n1, moves)

    pygame.display.update()
