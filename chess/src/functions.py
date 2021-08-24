import numpy as np
import pygame

def create_grid():
    k = 0
    grid    = np.zeros(64, np.int32)
    pieces   = [11,10, 9, 8, 7, 9,10,11,
                12,12,12,12,12,12,12,12,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 6, 6, 6, 6, 6, 6, 6, 6,
                 5, 4, 3, 2, 1, 3, 4, 5]
    grid    = np.array(pieces)
    return grid

def show_grid(W, H, c1, c2, screen, grid, pieces, n1):
    col     = [c1, c2]
    l       = W//8
    cell    = pygame.Surface((l, l))
    k = 0
    #col row
    for i in range(8):
        for j in range(8):
            cell.fill(col[(i+j)%2])
            screen.blit(cell,(l*j, l*i))
    if n1 != 0:
        cell.fill((100,0,255,100))
        screen.blit(cell,(l*(n1%8), l*int(n1/8)))
    for i,piece in enumerate(grid):
        if piece != 0:
            x = i%8
            y = i//8
            screen.blit(pieces[piece-1], (x*l, y*l))


def possible_moves(piece, n):
    if piece == 0:
        moves = [-9,-8,-7,
                 -1,    1,
                  7, 8, 9]
        moves += n
    if piece == 1:
        moves = []
        for i in range(8):
            moves.append(-7*i)
            moves.append(7*i)
            moves.append(9*i)
            moves.append(-9*i)
            moves.append(-8*i)
            moves.append(8*i)
            moves.append(i)
            moves.append(-i)


def move(grid, n1, n2):
    if grid[n1] != 0:
        grid[n2] = grid[n1]
        grid[n1] = 0





def get_pieces():
    dir     = './Images/'
    names   = ['B_king.png', 'B_queen.png', 'B_bishop.png', 'B_knight.png', 'B_rook.png', 'B_pawn.png',
               'W_king.png', 'W_queen.png', 'W_bishop.png', 'W_knight.png', 'W_rook.png', 'W_pawn.png']
    pieces  = []
    for name in names:
        im  = pygame.image.load(dir+name)
        pieces.append(im)
    return pieces



def crop_pieces(file):
    from PIL import Image
    dir     = "./Images/"
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
