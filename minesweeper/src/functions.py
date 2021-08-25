class Cell:
    def __init__(self,x, y, w, h, n):
        self.x  = x
        self.y  = y
        self.w  = w
        self.h  = h
        self.n  = n
        print(x, y, w, h, n)

    def clicked(self):
        import pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        (x_mouse, y_mouse)=pygame.mouse.get_pos()
        if x_mouse-self.x <= self.w and x_mouse-self.x >= 0:
            if y_mouse-self.y <= self.h and y_mouse-self.y >= 0:
                return True
            else:
                return False
        else:
            return False

class Bar:
    def __init__(self, x, y, w, h, min, max, n):
        self.x  = x
        self.y  = y
        self.w  = w
        self.h  = h
        self.n  = n
        self.minVal = min
        self.maxVal = max
        self.val    = 20

    def clicked(self):
        import pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        (x_mouse, y_mouse) = pygame.mouse.get_pos()
        if y_mouse-self.y <= self.h and y_mouse-self.y >= 0:
            return True
        else:
            return False

    def draw(self, screen):
        import pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        (x_mouse, y_mouse)=pygame.mouse.get_pos()

        x1  = self.x
        w   = self.w
        x2  = x1 + w
        sur1    = pygame.Surface((w, self.h))
        c   = 210
        sur1.fill((c, c, c))
        if x_mouse <= x1:
            self.val = self.minVal
        elif x_mouse >= x2:
            self.val = self.maxVal
        else:
            self.val = (x_mouse-x1)*(self.maxVal-self.minVal)//w + self.minVal
        rect    = pygame.Surface(((self.val-self.minVal)*w//(self.maxVal-self.minVal),self.h))
        c       = 180
        rect.fill((c, c, c))
        screen.blit(sur1, (self.x, self.y))
        screen.blit(rect, (self.x, self.y))

def start(n1=20, n2=20, n_mines=10):
    import pygame
    imgDir  = './images/'
    WIDTH   = 960
    HEIGHT  = 540

    screen  = pygame.display.set_mode((WIDTH, HEIGHT))

    initial_image   = pygame.image.load(imgDir+'initial_minesweeper.jpg')
    initial_image   = pygame.transform.scale(initial_image, (WIDTH, HEIGHT))
    running = True
    start   = Cell(379,249,210,42,0)
    quit    = Cell(379,290,210,42,1)
    settings= Cell(836,12,60,60,2)
    quit2   = Cell(904,17,60,60,3)
    cells   = [start,quit,settings,quit2]
    screen.blit(initial_image,(0,0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        (x_mouse, y_mouse) = pygame.mouse.get_pos()
        for cell in cells:
            if pygame.mouse.get_pressed()[0]:
                if cell.clicked():
                    num = cell.n
                    print(num)
                    if num == 0:
                        game(n1, n2, n_mines)
                    elif num == 1 or num == 3:
                        pygame.quit()
                    elif num == 2:
                        n1, n2, n_mines = setting()

        pygame.display.update()


def setting():
    import pygame
    WIDTH   = 960
    HEIGHT  = 540
    screen  = pygame.display.set_mode((WIDTH, HEIGHT))
    imgDir  = './images/'
    settings_img    = pygame.image.load(imgDir+'settings_minesweeper.jpg')
    settings_img    = pygame.transform.scale(settings_img, (WIDTH, HEIGHT))
    #                 x   y   w   h  min  max  n
    n1_bar      = Bar(175, 60,611,32, 10, 100,0)
    n2_bar      = Bar(175,103,611,32, 10, 100,1)
    mines_bar   = Bar(175,146,611,32,  0, 100,2)
    back        = Cell(438,246,83,99,         3)
    bars        = [n1_bar, n2_bar, mines_bar]
    screen.blit(settings_img, (0,0))
    running = True
    # for bar in bars:
    #     bar.draw(screen)
    circle      = pygame.Surface((25,25))
    while running:
        pygame.font.init()
        myfont = pygame.font.SysFont('Times New Roman', 20)
        (x_mouse, y_mouse) = pygame.mouse.get_pos()
        print(x_mouse, y_mouse)
        blank   = pygame.Surface((55,33))
        blank.fill((255,255,255))
        textsurface = myfont.render(str(n1_bar.val), True, (0, 0, 0))
        screen.blit(blank, (830,60))
        screen.blit(textsurface,(830, 60))
        textsurface = myfont.render(str(n2_bar.val), True, (0, 0, 0))
        screen.blit(blank, (830,105))
        screen.blit(textsurface,(830, 105))
        textsurface = myfont.render(str(mines_bar.val), True, (0, 0, 0))
        screen.blit(blank, (830,150))
        screen.blit(textsurface,(830,150))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            for bar in bars:
                if bar.clicked():
                    bar.draw(screen)
            if back.clicked():
                n1 = n1_bar.val
                n2 = n2_bar.val
                n_mines = mines_bar.val
                start(n1, n2, n_mines)
                pygame.quit()


        pygame.display.update()
    return n1, n2, mines



def game(n_cell1, n_cell2, n_mines):
    import pygame
    import numpy as np
    imgDir='./images/'
    black       = (0,0,0)
    white       = (255,255,255)
    light_grey  = (200,200,200)
    dark_grey   = (130,130,130)
    darker_grey = (70,70,70)
    l1  = 15
    WIDTH   = l1*n_cell1
    HEIGHT  = l1*n_cell2
    x, y, hit, checked   = create_grid(WIDTH, HEIGHT, n_cell1, n_cell2)
    screen  = pygame.display.set_mode((WIDTH,HEIGHT))

    empty_im= pygame.Surface((l1, l1))
    empty_im.fill((180,180,180))
    numbers = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png"]
    num_im  = [pygame.image.load(imgDir+number) for number in numbers]
    num_im  = [pygame.transform.scale(im, (l1,l1)) for im in num_im]
    flag_im = pygame.image.load(imgDir+'flag.png')
    flag_im = pygame.transform.scale(flag_im, (l1,l1))
    mine_im = pygame.image.load(imgDir+'mine.png')
    mine_im = pygame.transform.scale(mine_im, (l1,l1))
    cell_im = pygame.image.load(imgDir+'cell.png')
    cell_im = pygame.transform.scale(cell_im, (l1,l1))

    for i in range(n_cell1*n_cell2):
        screen.blit(cell_im, (x[i], y[i]))
    mines   = create_mines(n_cell1, n_cell2, n_mines)
    grid    = mine_count(mines, n_cell1, n_cell2, n_mines)
    showgrid(grid, l1, screen, n_cell1, n_cell2, hit, flag_im, num_im, empty_im, mine_im, cell_im)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start()
            (x_mouse, y_mouse)=pygame.mouse.get_pos()
            x_mouse = x_mouse//l1
            y_mouse = y_mouse//l1
            # if not mine_hit:
            if pygame.mouse.get_pressed()[0]:
                checked = np.zeros((n_cell1+2, n_cell2+2), np.int32)
                hit_grid(x_mouse+1, y_mouse+1, grid, hit, checked)
                showgrid(grid, l1, screen, n_cell1, n_cell2, hit, flag_im, num_im, empty_im, mine_im, cell_im,)
                pygame.display.update()
            elif pygame.mouse.get_pressed()[2]:
                hit[x_mouse+1][y_mouse+1]   = -1
                showgrid(grid, l1, screen, n_cell1, n_cell2, hit, flag_im, num_im, empty_im, mine_im, cell_im,)
                pygame.display.update()
        pygame.display.update()

def create_grid(w, h, nx, ny):
    import numpy as np
    hit     = np.zeros((nx+2, ny+2), np.int32)
    checked = np.zeros((nx+2, ny+2), np.int32)
    x       = np.zeros(nx*ny, np.int32)
    y       = np.zeros(nx*ny, np.int32)
    for i in range(nx*ny):
        x[i]    = w/nx*(i%nx)
        y[i]    = h/ny*(i//nx)
    return (x, y, hit, checked)

def create_mines(n1, n2, n_mines):
    import pygame
    import numpy as np
    from random import randint
    x   = np.zeros(n_mines, np.int32)
    y   = np.zeros(n_mines, np.int32)
    x  += n1
    y  += n2
    for i in range(n_mines):
        x[i]    = randint(0,n1-1)
        y[i]    = randint(0,n2-1)
        new     = False
        while not new:
            new = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            for j in range(n_mines):
                if i!=j and x[i] == x[j] and y[i] == y[j]:
                    x[i]    = randint(0,n1-1)
                    y[i]    = randint(0,n2-1)
                    new = False
    mines   = np.array(list(zip(x, y)))
    return mines

def mine_count(mines, n1, n2, n_mines):
    import numpy as np
    grid    = np.zeros((n1+2, n2+2), np.int32)
    for i in range(n_mines):
        grid[mines[i][0]+1][mines[i][1]+1] = -1
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if grid[i][j] != -1:
                count = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if grid[i+k][j+l] == -1:
                            count   += 1
                grid[i][j] = count
    for i in range(0,n1+2):
        grid[i][0] = 9
        grid[i][n2+1] = 9
    for i in range(0,n2+2):
        grid[0][i] = 9
        grid[n1+1][i] = 9
    return grid

def showgrid(grid, l1, screen, n1, n2, hit, flag_im, num_im, empty_im, mine_im, cell_im):
    import pygame
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if hit[i][j] == 1:
                if grid[i][j] == -1:
                    screen.blit(mine_im, ((i-1)*l1, (j-1)*l1))
                elif grid[i][j] == 0:
                    screen.blit(empty_im, ((i-1)*l1, (j-1)*l1))
                elif grid[i][j] == -2:
                    screen.blit(flag_im, ((i-1)*l1, (j-1)*l1))
                elif grid[i][j] > 0:
                    screen.blit(num_im[grid[i][j]-1], ((i-1)*l1, (j-1)*l1))
            elif hit[i][j] == -1:
                screen.blit(flag_im, ((i-1)*l1, (j-1)*l1))
        pygame.display.update()

def hit_grid(i, j, grid, hit, checked):
    hit[i][j] = 1
    checked[i][j] = 1
    if grid[i][j] == 0:
        for k in range(-1, 2):
            for l in range(-1, 2):
                if not checked[i+k][j+l] and (k==0 or l==0):
                    hit_grid(i+k, j+l, grid, hit, checked)
    else:
        return
