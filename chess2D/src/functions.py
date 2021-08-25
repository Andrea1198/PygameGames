import numpy as np
import pygame
from src.moves import *

def create_grid():
    pieces   = [[11,10, 9, 8, 7, 9,10,11],
                [12,12,12,12,12,12,12,12],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 6, 6, 6, 6, 6, 6, 6, 6],
                [ 5, 4, 3, 2, 1, 3, 4, 5]]
    # pieces   = [[ 0, 0, 0, 0, 0, 0, 0, 0],
    #             [ 0, 0, 0, 0, 0, 0, 0, 0],
    #             [ 0, 0, 0, 0, 0, 0, 0, 0],
    #             [ 0, 0, 0, 2, 0, 0, 0, 0],
    #             [ 0, 0, 0, 0, 0, 0, 0, 0],
    #             [ 0, 5, 4, 0, 0, 3, 0, 0],
    #             [ 0, 0, 0, 0, 0, 0, 0, 0],
    #             [ 0, 0, 0, 0, 0, 0, 0, 0]]
    grid    = np.array(pieces)
    return grid


def show_grid(W, H, c1, c2, screen, grid, pieces, n, moves):
    col     = [c1, c2]
    l       = W//8
    cell    = pygame.Surface((l, l))
    k = 0
    #col row
    for i in range(8):
        for j in range(8):
            cell.fill(col[(i+j)%2])
            screen.blit(cell,(l*j, l*i))
    if  n != [0,0]:
        cell.fill((100,0,255,0))
        screen.blit(cell,(l*n[0], l*n[1]))
    for move in moves:
        cell.fill((0,155,0, 50))
        screen.blit(cell, (l*move[0], l*move[1]))
    for i in range(8):
        for j in range(8):
            if grid[i,j] != 0:
                screen.blit(pieces[grid[i,j]-1], (j*l, i*l))


def possible_moves(grid, i1, j1, rook1Moved, rook2Moved, kingMoved):
    from numpy import array
    piece = grid[j1, i1]

    if piece == 1:
        moves = king(0, grid, i1, j1, rook1Moved, rook2Moved, kingMoved)
    elif piece == 7:
        moves = king(1, grid, i1, j1, rook1Moved, rook2Moved, kingMoved)
    elif piece == 2:
        moves = queen(0, grid, i1, j1)
    elif piece == 8:
        moves = queen(1, grid, i1, j1)
    elif piece == 3:
        moves = bishop(0, grid, i1, j1)
    elif piece == 9:
        moves = bishop(1, grid, i1, j1)
    elif piece == 4:
        moves = knight(0, grid, i1, j1)
    elif piece == 10:
        moves = knight(1, grid, i1, j1)
    elif piece == 5:
        moves = rook(0, grid, i1, j1)
    elif piece == 11:
        moves = rook(1, grid, i1, j1)
    elif piece == 6:
        moves = pawn(0, grid, i1, j1)
    elif piece == 12:
        moves = pawn(1, grid, i1, j1)

    return moves

def whitePromotion(grid, i, j, l):
    import pygame
    # makeGrid
    cell = pygame.Surface((l, l))
    


def checkPromotion(grid, i, j, l):
    if grid[j,i] == 6:
        if j == 0:
            whitePromotion(grid, i, j, l)


def move(grid, i1, j1, i2, j2, l):
    if grid[j1, i1] != 0:
        grid[j2, i2] = grid[j1, i1]
        grid[j1, i1] = 0
    checkPromotion(grid, i2, j2, l)


def get_pieces():
    dir     = './images/'
    names   = ['B_king.png', 'B_queen.png', 'B_bishop.png', 'B_knight.png', 'B_rook.png', 'B_pawn.png',
               'W_king.png', 'W_queen.png', 'W_bishop.png', 'W_knight.png', 'W_rook.png', 'W_pawn.png']
    pieces  = []
    for name in names:
        im  = pygame.image.load(dir+name)
        pieces.append(im)
    return pieces



def crop_pieces(file):
    from PIL import Image
    dir     = "./images/"
    im      = Image.open(file)
    name    = ['B_king.png', 'B_queen.png', 'B_bishop.png', 'B_knight.png', 'B_rook.png', 'B_pawn.png',
               'W_king.png', 'W_queen.png', 'W_bishop.png', 'W_knight.png', 'W_rook.png', 'W_pawn.png']
    pieces  = []
    k       = 0
    size    = 60,60
    for i in range(2):
        top     = 200*i
        bottom  = 200+200*i
        for j in range(6):
            left    = 200*j
            right   = 200+200*j
            im1     = im.crop((left, top, right, bottom))
            im1.thumbnail(size)
            im1.save(dir+name[i*6+j])
    return pieces
