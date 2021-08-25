def check_bounds(i1, boundMin, boundMax):
    return boundMin <= i1  and i1 < boundMax

def rescale(moves):
    i = 0
    while i<len(moves):
        if not check_bounds(moves[i][0], 0, 8) or not check_bounds(moves[i][1], 0, 8):
            del moves[i]
        else:
            i += 1


def check_row(moves, grid, mod, i1, j1, col):
    removables = []
    list = []
    for move in moves:
        move[0] += i1
        move[1] += j1
    for i in range(mod):
        list1 = []
        for j in range(int(len(moves)/mod)):
            list1.append(moves[i+j*mod])
        list.append(list1)
    for i, list1 in enumerate(list):
        for j, move in enumerate(list1):
            check_same_color = False
            check_other_color = False
            i1 = move[0]
            j1 = move[1]
            if check_bounds(i1, 0, 8) and check_bounds(j1, 0, 8):
                if check_bounds(grid[j1, i1], 1+col*6, 7+col*6):
                    check_same_color = True
                if check_bounds(grid[j1, i1], 7-col*6, 13-col*6):
                    check_other_color= True
            if check_same_color:
                for k in range(j, len(list1)):
                    removables.append(list1[k])
                break
            if check_other_color:
                for k in range(j+1, len(list1)):
                    removables.append(list1[k])
                break
    for rem in removables:
        i = 0
        while i < len(moves):
            if rem == moves[i]:
                del moves[i]
                break
            else:
                i += 1
    return moves

def checkPawnMoves(moves, grid, i1, j1, col):
    removables  = []
    for move in moves:
        move[0] += i1
        move[1] += j1
    sameColor = [check_bounds(grid[move[1], move[0]], 1+col*6,  7+col*6) for move in moves]
    diffColor = [check_bounds(grid[move[1], move[0]], 7-col*6, 13-col*6) for move in moves]
    nullColor = [grid[move[1], move[0]] == 0 for move in moves]
    if sameColor[0] or diffColor[0]:
        removables.append(moves[0])
        removables.append(moves[1])
    elif sameColor[1] or diffColor[1]:
        removables.append(moves[1])
    if nullColor[2] or sameColor[2]:
        removables.append(moves[2])
    if nullColor[3] or sameColor[3]:
        removables.append(moves[3])
    for rem in removables:
        i = 0
        while i < len(moves):
            if rem == moves[i]:
                del moves[i]
                break
            else:
                i += 1

    return moves


def checkKingMoves(moves, grid, i1, j1, col, rook1Moved, rook2Moved, kingMoved):
    if not kingMoved[col] and not rook1Moved[col]:
        if grid[col*7, 5] == 0 and grid[col*7, 6] == 0:
            moves.append([0, 2])
    if not kingMoved[col] and not rook2Moved[col]:
        if grid[col*7, 1] == 0 and grid[col*7, 2] and grid[col*7, 3] == 0:
            moves.append([0,-3])
    # for move in moves:
    #     move[0] += i1
    #     move[1] += j1
    moves = check_row(moves, grid, len(moves), i1, j1, col)
    return moves

def king(col, grid, i1, j1, rook1Moved, rook2Moved, kingMoved):
    moves = [[-1, 0],
             [ 1, 0],
             [ 1, 1],
             [-1,-1],
             [ 0, 1],
             [ 0,-1],
             [ 1,-1],
             [-1, 1]]

    moves = checkKingMoves(moves, grid, i1, j1, col, rook1Moved, rook2Moved, kingMoved)
    rescale(moves)

    return moves

def queen(col, grid, i1, j1):
    moves = []
    for i in range(1, 8):
        moves.append([ i, i])
        moves.append([-i, i])
        moves.append([-i,-i])
        moves.append([ i,-i])
        moves.append([ i, 0])
        moves.append([ 0, i])
        moves.append([ 0,-i])
        moves.append([-i, 0])
    moves = check_row(moves, grid, 8, i1, j1, col)
    rescale(moves)
    return moves

def bishop(col
, grid, i1, j1):
    moves = []
    for i in range(1,8):
        moves.append([ i, i])
        moves.append([-i, i])
        moves.append([-i,-i])
        moves.append([ i,-i])
    moves = check_row(moves, grid, 4, i1, j1, col)
    rescale(moves)
    return moves

def knight(col, grid, i1, j1):
    moves = [[ 1, 2],
             [ 2, 1],
             [-1, 2],
             [ 2,-1],
             [-1,-2],
             [-2,-1],
             [ 1,-2],
             [-2, 1]]
    moves = check_row(moves, grid, 8, i1, j1, col)
    rescale(moves)
    return moves


def rook(col, grid, i1, j1):
    moves = []
    for i in range(1, 8):
        moves.append([ i, 0])
        moves.append([ 0, i])
        moves.append([ 0,-i])
        moves.append([-i, 0])
    moves = check_row(moves, grid, 4, i1, j1, col)
    rescale(moves)
    return moves

def pawn(col, grid, i1, j1):
    moves = [[ 0, -1+col*2],
             [ 0, -2+col*4],
             [ 1, -1+col*2],
             [-1, -1+col*2]]
    moves = checkPawnMoves(moves, grid, i1, j1, col)
    return moves
