import pygame
import random
from tkinter import messagebox
import tkinter as tk
width   = 500
height  = width
rows    = 20
screen  = pygame.display.set_mode((width, height))

# Cube
class Cube(object):
    def __init__(self, position, dirx=1, diry=0, color = (255,0,0)):
        self.pos = position
        self.dirX = dirx
        self.dirY = diry
        self.color = color

    def move(self, dirx, diry):
        self.dirX = dirx
        self.dirY = diry
        self.pos  = (self.pos[0] + self.dirX, self.pos[1] + self.dirY)

    def draw(self, surface, eyes = False):
        dis = width // rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle    = (i*dis+centre - radius,  j*dis+8)
            circleMiddle2   = (i*dis+dis-radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)

# Snake
class Snake(object):
    body    = []
    turns   = {}
    def __init__(self, color, pos):
        self.color  = color
        self.dirX   = 0
        self.dirY   = 1
        self.head   = Cube(pos, dirx=0, diry=1, color=color)
        self.body.append(self.head)

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # Check keys
        keys    = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.dirX != 1:
            print("left")
            self.dirX = -1
            self.dirY = 0
            self.turns[self.head.pos[:]] = [self.dirX, self.dirY]
            # break

        elif keys[pygame.K_RIGHT] and self.dirX != -1:
            print("right")
            self.dirX = 1
            self.dirY = 0
            self.turns[self.head.pos[:]] = [self.dirX, self.dirY]
            # break

        elif keys[pygame.K_UP] and self.dirY != 1:
            print("up")
            self.dirX = 0
            self.dirY = -1
            self.turns[self.head.pos[:]] = [self.dirX, self.dirY]
            # break

        elif keys[pygame.K_DOWN] and self.dirY != -1:
            print("down")
            self.dirX = 0
            self.dirY = 1
            self.turns[self.head.pos[:]] = [self.dirX, self.dirY]
            # break
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                # Boundary conditions
                if c.dirX == -1 and c.pos[0] <= 0: c.pos = (rows-1, c.pos[1])
                elif c.dirX == 1 and c.pos[0] >= rows-1: c.pos = (0, c.pos[1])
                elif c.dirY == 1 and c.pos[1] >= rows-1: c.pos = (c.pos[0], 0)
                elif c.dirY == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], rows-1)
                else: c.move(c.dirX, c.dirY)


    def reset(self, pos):
        self.body   = []
        self.turns  = {}
        self.dirX   = 0
        self.diry   = 1
        self.head   = Cube(pos, dirx=0, diry=1, color=color)
        self.body.append(self.head)

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirX, tail.dirY
        if dx == 1:
            self.body.append(Cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1:
            self.body.append(Cube((tail.pos[0]+1, tail.pos[1])))
        elif dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]-1)))
        else:
            self.body.append(Cube((tail.pos[0], tail.pos[1]+1)))

        self.body[-1].dirX = dx
        self.body[-1].dirY = dy


    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i==0: c.draw(surface, True)
            else: c.draw(surface)

def randomSnack(item):
    positions   = item.body
    while True:
        x   = random.randrange(rows)
        y   = random.randrange(rows)
        # if len(list(filter(lambda z:z.pos == (x, y), positions))) > 0:
        if [x, y] in positions:
            continue
        else:
            break
    return (x, y)

def drawGrid(surface):
    sizeBtwn    = width // rows
    x           = 0
    y           = 0
    for l in range(rows):
        x = x+sizeBtwn
        y = y+sizeBtwn
        pygame.draw.line(surface, (255,255,255), (x, 0), (x, height))
        pygame.draw.line(surface, (255,255,255), (0, y), (width, y))


def redrawWindow(surface):
    global s, snack
    surface.fill((0,0,0))
    drawGrid(surface)
    s.draw(surface)
    snack.draw(surface)
    pygame.display.update()

def messageBox(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def start():
    global s, snack
    s       = Snake((255, 0, 0), (10, 10))
    snack   = Cube(randomSnack(s), color=(0,255,0))
    print(randomSnack(s))
    pygame.init()
    pygame.display.set_caption("Snake")
    running = True

    clock   = pygame.time.Clock()


    while running:
        pygame.time.delay(50)
        clock.tick(10)              # max FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        s.move()
        if s.body[0].pos == snack.pos:
            snack   = Cube(randomSnack(s), color=(0,255,0))
            s.addCube()

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos, s.body[x+1:])):
            # if s.body[x].pos in s.body[x+1:].pos:
                print("score" + str(len(s.body)))
                messageBox("You Lost!", "Play again..")
                s.reset((10, 10))
                break



        redrawWindow(screen)
