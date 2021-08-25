import pygame
import random

pygame.init()
window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Window")
black = (0,0,0)
blue = (0,0,205)



LIV =[[0,0,1,0],
      [0,0,1,0],
      [0,0,1,0],
      [0,0,1,0]]
LIH =[[0,0,0,0],
      [1,1,1,1],
      [0,0,0,0],
      [0,0,0,0]]
SQ = [[0,0,0,0],
      [0,1,1,0],
      [0,1,1,0],
      [0,0,0,0]]
TID =[[0,0,0,0],
      [0,1,1,1],
      [0,0,1,0],
      [0,0,0,0]]
TIL =[[0,0,1,0],
      [0,1,1,0],
      [0,0,1,0],
      [0,0,0,0]]
TIU =[[0,0,1,0],
      [0,1,1,1],
      [0,0,0,0],
      [0,0,0,0]]
TIR =[[0,0,1,0],
      [0,0,1,1],
      [0,0,1,0],
      [0,0,0,0]]
LRU =[[0,1,0,0],
      [0,1,0,0],
      [0,1,1,0],
      [0,0,0,0]]
LRR =[[0,0,0,0],
      [0,1,1,1],
      [0,1,0,0],
      [0,0,0,0]]
LRD =[[0,0,0,0],
      [0,1,1,0],
      [0,0,1,0],
      [0,0,1,0]]
LRL =[[0,0,0,0],
      [0,0,1,0],
      [1,1,1,0],
      [0,0,0,0]]
LLU =[[0,0,1,0],
      [0,0,1,0],
      [0,1,1,0],
      [0,0,0,0]]
LLR =[[0,0,0,0],
      [0,1,0,0],
      [0,1,1,1],
      [0,0,0,0]]
LLD =[[0,1,1,0],
      [0,1,0,0],
      [0,1,0,0],
      [0,0,0,0]]
LLL =[[0,0,0,0],
      [0,0,0,1],
      [0,1,1,1],
      [0,0,0,0]]
SRH =[[0,0,0,0],
      [1,1,0,0],
      [0,1,1,0],
      [0,0,0,0]]
SRV =[[0,0,0,0],
      [0,0,1,0],
      [0,1,1,0],
      [0,1,0,0]]
SLH =[[0,0,0,0],
      [0,1,1,0],
      [1,1,0,0],
      [0,0,0,0]]
SLV =[[0,0,0,0],
      [0,1,0,0],
      [0,1,1,0],
      [0,0,1,0]]



gameLoop = True
while gameLoop:
      for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                  gameLoop = False
            if (event.type==pygame.KEYDOWN):

                  shapes=(LIV,LIH,SQ,TID,TIL,TIU,TIR,LRU,LRR,LRD,LRL,LLU,LLR,LLD,LLL,SLH,SLV,SRH,SRV)

                  A=random.choice(shapes)

                  if A == LIV:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10)),
                        pygame.draw.rect(window,blue,(395,20,10,10)),
                        pygame.draw.rect(window,blue,(395,30,10,10))
                        print(A)
                        if(event.key==pygame.K_RIGHT):
                              A = LIH
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(405,0,10,10)),
                              pygame.draw.rect(window,blue,(415,0,10,10)),
                              pygame.draw.rect(window,blue,(425,0,10,10))
                              print(A)
                  if A == LIH:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(405,0,10,10)),
                        pygame.draw.rect(window,blue,(415,0,10,10)),
                        pygame.draw.rect(window,blue,(425,0,10,10))
                        print(A)
                        if(event.key==pygame.K_RIGHT):
                              A = LIV
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10)),
                              pygame.draw.rect(window,blue,(395,20,10,10)),
                              pygame.draw.rect(window,blue,(395,30,10,10))
                              print(A)

                  if A == LIV:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10)),
                        pygame.draw.rect(window,blue,(395,20,10,10)),
                        pygame.draw.rect(window,blue,(395,30,10,10))
                        print(A)
                        if(event.key==pygame.K_LEFT):
                              A = LIH
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(405,0,10,10)),
                              pygame.draw.rect(window,blue,(415,0,10,10)),
                              pygame.draw.rect(window,blue,(425,0,10,10))
                              print(A)
                  if A == LIH:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(405,0,10,10)),
                        pygame.draw.rect(window,blue,(415,0,10,10)),
                        pygame.draw.rect(window,blue,(425,0,10,10))
                        print(A)
                        if(event.key==pygame.K_LEFT):
                              A = LIV
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10)),
                              pygame.draw.rect(window,blue,(395,20,10,10)),
                              pygame.draw.rect(window,blue,(395,30,10,10))
                              print(A)

                  if A == TID:
                        pygame.draw.rect(window,blue,(385,0,10,10)),
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(405,0,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10))
                        print(A)
                        if(event.key==pygame.K_RIGHT):
                              A = TIL
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10)),
                              pygame.draw.rect(window,blue,(395,20,10,10)),
                              pygame.draw.rect(window,blue,(385,10,10,10))
                              print(A)
                  if A == TIL:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10)),
                        pygame.draw.rect(window,blue,(395,20,10,10)),
                        pygame.draw.rect(window,blue,(385,10,10,10))
                        print(A)
                        if(event.key==pygame.K_RIGHT):
                              A = TIU
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(385,10,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10)),
                              pygame.draw.rect(window,blue,(405,10,10,10))
                              print(A)
                  if A == TIU:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(385,10,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10)),
                        pygame.draw.rect(window,blue,(405,10,10,10))
                        print(A)
                        if(event.key==pygame.K_RIGHT):
                              A = TIR
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10)),
                              pygame.draw.rect(window,blue,(395,20,10,10)),
                              pygame.draw.rect(window,blue,(405,10,10,10))
                              print(A)
                  if A == TIR:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10)),
                        pygame.draw.rect(window,blue,(395,20,10,10)),
                        pygame.draw.rect(window,blue,(405,10,10,10))
                        print(A)
                        if(event.key==pygame.K_RIGHT):
                              A = TID
                              pygame.draw.rect(window,blue,(385,0,10,10)),
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(405,0,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10))
                              print(A)

                  if A == TID:
                        pygame.draw.rect(window,blue,(385,0,10,10)),
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(405,0,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10))
                        print(A)
                        if(event.key==pygame.K_LEFT):
                              A = TIL
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10)),
                              pygame.draw.rect(window,blue,(395,20,10,10)),
                              pygame.draw.rect(window,blue,(385,10,10,10))
                              print(A)
                  if A == TIL:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10)),
                        pygame.draw.rect(window,blue,(395,20,10,10)),
                        pygame.draw.rect(window,blue,(385,10,10,10))
                        print(A)
                        if(event.key==pygame.K_LEFT):
                              A = TIU
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(385,10,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10)),
                              pygame.draw.rect(window,blue,(405,10,10,10))
                              print(A)
                  if A == TIU:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(385,10,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10)),
                        pygame.draw.rect(window,blue,(405,10,10,10))
                        print(A)
                        if(event.key==pygame.K_LEFT):
                              A = TIR
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10)),
                              pygame.draw.rect(window,blue,(395,20,10,10)),
                              pygame.draw.rect(window,blue,(405,10,10,10))
                              print(A)
                  if A == TIR:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10)),
                        pygame.draw.rect(window,blue,(395,20,10,10)),
                        pygame.draw.rect(window,blue,(405,10,10,10))
                        print(A)
                        if(event.key==pygame.K_LEFT):
                              A = TID
                              pygame.draw.rect(window,blue,(385,0,10,10)),
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(405,0,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10))
                              print(A)

                  if A == LRU:
                        pygame.draw.rect(window, blue, (395, 0, 10, 10)),
                        pygame.draw.rect(window, blue, (395, 10, 10, 10)),
                        pygame.draw.rect(window, blue, (395, 20, 10, 10)),
                        pygame.draw.rect(window, blue, (405, 20, 10, 10))
                        print(A)
                        if (event.key == pygame.K_RIGHT):
                              A = LRR
                              pygame.draw.rect(window, blue, (385, 0, 10, 10)),
                              pygame.draw.rect(window, blue, (385, 10, 10, 10)),
                              pygame.draw.rect(window, blue, (395, 0, 10, 10)),
                              pygame.draw.rect(window, blue, (405, 0, 10, 10))
                              print(A)
                  if A == LRR:
                        pygame.draw.rect(window, blue, (385, 0, 10, 10)),
                        pygame.draw.rect(window, blue, (385, 10, 10, 10)),
                        pygame.draw.rect(window, blue, (395, 0, 10, 10)),
                        pygame.draw.rect(window, blue, (405, 0, 10, 10))
                        print(A)
                        if (event.key == pygame.K_RIGHT):
                              A = LRD
                              pygame.draw.rect(window, blue, (395, 0, 10, 10)),
                              pygame.draw.rect(window, blue, (405, 10, 10, 10)),
                              pygame.draw.rect(window, blue, (405, 20, 10, 10)),
                              pygame.draw.rect(window, blue, (405, 30, 10, 10))
                              print(A)
                  if A == LRD:
                        pygame.draw.rect(window, blue, (395, 0, 10, 10)),
                        pygame.draw.rect(window, blue, (405, 10, 10, 10)),
                        pygame.draw.rect(window, blue, (405, 20, 10, 10)),
                        pygame.draw.rect(window, blue, (405, 30, 10, 10))
                        print(A)
                        if (event.key == pygame.K_RIGHT):
                              A = LRL
                              pygame.draw.rect(window, blue, (415, 0, 10, 10)),
                              pygame.draw.rect(window, blue, (415, 10, 10, 10)),
                              pygame.draw.rect(window, blue, (405, 10, 10, 10)),
                              pygame.draw.rect(window, blue, (395, 10, 10, 10))
                              print(A)
                  if A == LRL:
                        pygame.draw.rect(window, blue, (415, 0, 10, 10)),
                        pygame.draw.rect(window, blue, (415, 10, 10, 10)),
                        pygame.draw.rect(window, blue, (405, 10, 10, 10)),
                        pygame.draw.rect(window, blue, (395, 10, 10, 10))
                        print(A)
                        if (event.key == pygame.K_RIGHT):
                              A = LRU
                              pygame.draw.rect(window, blue, (395, 0, 10, 10)),
                              pygame.draw.rect(window, blue, (395, 10, 10, 10)),
                              pygame.draw.rect(window, blue, (395, 20, 10, 10)),
                              pygame.draw.rect(window, blue, (405, 20, 10, 10))
                              print(A)

                  if A == LRU:
                        pygame.draw.rect(window, blue, (395, 0, 10, 10)),
                        pygame.draw.rect(window, blue, (395, 10, 10, 10)),
                        pygame.draw.rect(window, blue, (395, 20, 10, 10)),
                        pygame.draw.rect(window, blue, (405, 20, 10, 10))
                        print(A)
                        if (event.key == pygame.K_LEFT):
                              A = LRR
                              pygame.draw.rect(window, blue, (385, 0, 10, 10)),
                              pygame.draw.rect(window, blue, (385, 10, 10, 10)),
                              pygame.draw.rect(window, blue, (395, 0, 10, 10)),
                              pygame.draw.rect(window, blue, (405, 0, 10, 10))
                              print(A)
                  if A == LRR:
                        pygame.draw.rect(window, blue, (385, 0, 10, 10)),
                        pygame.draw.rect(window, blue, (385, 10, 10, 10)),
                        pygame.draw.rect(window, blue, (395, 0, 10, 10)),
                        pygame.draw.rect(window, blue, (405, 0, 10, 10))
                        print(A)
                        if (event.key == pygame.K_LEFT):
                              A = LRD
                              pygame.draw.rect(window, blue, (395, 0, 10, 10)),
                              pygame.draw.rect(window, blue, (405, 10, 10, 10)),
                              pygame.draw.rect(window, blue, (405, 20, 10, 10)),
                              pygame.draw.rect(window, blue, (405, 30, 10, 10))
                              print(A)

                  if A == LRD:
                        pygame.draw.rect(window, blue, (395, 0, 10, 10)),
                        pygame.draw.rect(window, blue, (405, 10, 10, 10)),
                        pygame.draw.rect(window, blue, (405, 20, 10, 10)),
                        pygame.draw.rect(window, blue, (405, 30, 10, 10))
                        print(A)
                        if (event.key == pygame.K_LEFT):
                              A = LRL
                              pygame.draw.rect(window, blue, (415, 0, 10, 10)),
                              pygame.draw.rect(window, blue, (415, 10, 10, 10)),
                              pygame.draw.rect(window, blue, (405, 10, 10, 10)),
                              pygame.draw.rect(window, blue, (395, 10, 10, 10))
                              print(A)
                  if A == LRL:
                        pygame.draw.rect(window, blue, (415, 0, 10, 10)),
                        pygame.draw.rect(window, blue, (415, 10, 10, 10)),
                        pygame.draw.rect(window, blue, (405, 10, 10, 10)),
                        pygame.draw.rect(window, blue, (395, 10, 10, 10))
                        print(A)
                        if (event.key == pygame.K_LEFT):
                              A = LRU
                              pygame.draw.rect(window, blue, (395, 0, 10, 10)),
                              pygame.draw.rect(window, blue, (395, 10, 10, 10)),
                              pygame.draw.rect(window, blue, (395, 20, 10, 10)),
                              pygame.draw.rect(window, blue, (405, 20, 10, 10))
                              print(A)

                  if A == LLU:
                        pygame.draw.rect(window, blue, (400, 0, 10, 30)),
                        pygame.draw.rect(window, blue, (390, 30, 10, 10))
                        print(A)
                        if (event.key == pygame.K_RIGHT):
                              A = LLL
                              pygame.draw.rect(window, blue, (410, 10, 10, 10)),
                              pygame.draw.rect(window, blue, (390, 20, 30, 10))
                  if A == LLL:
                        pygame.draw.rect(window, blue, (410, 10, 10, 10)),
                        pygame.draw.rect(window, blue, (390, 20, 30, 10))
                        print(A)
                        if (event.key == pygame.K_RIGHT):
                              A = LLD
                              pygame.draw.rect(window, blue, (390, 0, 20, 10)),
                              pygame.draw.rect(window, blue, (390, 10, 10, 20))
                  if A == LLD:
                        pygame.draw.rect(window, blue, (390, 0, 20, 10)),
                        pygame.draw.rect(window, blue, (390, 10, 10, 20))
                        print(A)
                        if (event.key == pygame.K_RIGHT):
                              A = LLR
                              pygame.draw.rect(window, blue, (390, 10, 10, 10)),
                              pygame.draw.rect(window, blue, (390, 20, 30, 10))
                  if A == LLR:
                        pygame.draw.rect(window, blue, (390, 10, 10, 10)),
                        pygame.draw.rect(window, blue, (390, 20, 30, 10))
                        print(A)
                        if (event.key == pygame.K_RIGHT):
                              A = LLU
                              pygame.draw.rect(window, blue, (400, 0, 10, 30)),
                              pygame.draw.rect(window, blue, (390, 30, 10, 10))

                  if A == LLU:
                        pygame.draw.rect(window, blue, (400, 0, 10, 30)),
                        pygame.draw.rect(window, blue, (390, 30, 10, 10))
                        print(A)
                        if (event.key == pygame.K_LEFT):
                              A = LLR
                              pygame.draw.rect(window, blue, (390, 10, 10, 10)),
                              pygame.draw.rect(window, blue, (390, 20, 30, 10))
                  if A == LLR:
                        pygame.draw.rect(window, blue, (390, 10, 10, 10)),
                        pygame.draw.rect(window, blue, (390, 20, 30, 10))
                        print(A)
                        if (event.key == pygame.K_LEFT):
                              A = LLD
                              pygame.draw.rect(window, blue, (390, 0, 20, 10)),
                              pygame.draw.rect(window, blue, (390, 10, 10, 20))
                  if A == LLD:
                        pygame.draw.rect(window, blue, (390, 0, 20, 10)),
                        pygame.draw.rect(window, blue, (390, 10, 10, 20))
                        print(A)
                        if (event.key == pygame.K_LEFT):
                              A = LLL
                              pygame.draw.rect(window, blue, (410, 10, 10, 10)),
                              pygame.draw.rect(window, blue, (390, 20, 30, 10))
                  if A == LLL:
                        pygame.draw.rect(window, blue, (410, 10, 10, 10)),
                        pygame.draw.rect(window, blue, (390, 20, 30, 10))
                        print(A)
                        if (event.key == pygame.K_LEFT):
                              A = LLU
                              pygame.draw.rect(window, blue, (400, 0, 10, 30)),
                              pygame.draw.rect(window, blue, (390, 30, 10, 10))

                  if A == SLV:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10)),
                        pygame.draw.rect(window,blue,(405,10,10,10)),
                        pygame.draw.rect(window,blue,(405,20,10,10))
                        print(A)
                        if(event.key==pygame.K_RIGHT):
                              A = SLH
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10)),
                              pygame.draw.rect(window,blue,(405,10,10,10)),
                              pygame.draw.rect(window,blue,(405,20,10,10))
                              print(A)
                  if A == SLH:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10)),
                        pygame.draw.rect(window,blue,(405,10,10,10)),
                        pygame.draw.rect(window,blue,(405,20,10,10))
                        print(A)
                        if(event.key==pygame.K_RIGHT):
                              A = SLV
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10)),
                              pygame.draw.rect(window,blue,(405,10,10,10)),
                              pygame.draw.rect(window,blue,(405,20,10,10))
                              print(A)

                  if A == SLV:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10)),
                        pygame.draw.rect(window,blue,(405,10,10,10)),
                        pygame.draw.rect(window,blue,(405,20,10,10))
                        print(A)
                        if(event.key==pygame.K_LEFT):
                              A = SLH
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10)),
                              pygame.draw.rect(window,blue,(405,10,10,10)),
                              pygame.draw.rect(window,blue,(405,20,10,10))
                              print(A)
                  if A == SLH:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10)),
                        pygame.draw.rect(window,blue,(405,10,10,10)),
                        pygame.draw.rect(window,blue,(405,20,10,10))
                        print(A)
                        if(event.key==pygame.K_LEFT):
                              A = SLV
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10)),
                              pygame.draw.rect(window,blue,(405,10,10,10)),
                              pygame.draw.rect(window,blue,(405,20,10,10))
                              print(A)

                  if A == SRV:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10)),
                        pygame.draw.rect(window,blue,(385,10,10,10)),
                        pygame.draw.rect(window,blue,(385,20,10,10))
                        print(A)
                        if(event.key==pygame.K_RIGHT):
                              A = SRH
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10)),
                              pygame.draw.rect(window,blue,(385,0,10,10)),
                              pygame.draw.rect(window,blue,(405,10,10,10))
                              print(A)
                  if A == SRH:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10)),
                        pygame.draw.rect(window,blue,(385,0,10,10)),
                        pygame.draw.rect(window,blue,(405,10,10,10))
                        print(A)
                        if(event.key==pygame.K_RIGHT):
                              A = SRV
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10)),
                              pygame.draw.rect(window,blue,(385,10,10,10)),
                              pygame.draw.rect(window,blue,(385,20,10,10))
                              print(A)

                  if A == SRV:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10)),
                        pygame.draw.rect(window,blue,(385,10,10,10)),
                        pygame.draw.rect(window,blue,(385,20,10,10))
                        print(A)
                        if(event.key==pygame.K_LEFT):
                              A = SRH
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10)),
                              pygame.draw.rect(window,blue,(385,0,10,10)),
                              pygame.draw.rect(window,blue,(405,10,10,10))
                              print(A)
                  if A == SRH:
                        pygame.draw.rect(window,blue,(395,0,10,10)),
                        pygame.draw.rect(window,blue,(395,10,10,10)),
                        pygame.draw.rect(window,blue,(385,0,10,10)),
                        pygame.draw.rect(window,blue,(405,10,10,10))
                        print(A)
                        if(event.key==pygame.K_LEFT):
                              A = SRV
                              pygame.draw.rect(window,blue,(395,0,10,10)),
                              pygame.draw.rect(window,blue,(395,10,10,10)),
                              pygame.draw.rect(window,blue,(385,10,10,10)),
                              pygame.draw.rect(window,blue,(385,20,10,10))
                              print(A)
      window.fill(black)
      pygame.draw.rect(window,blue,(395,0,10,10)),
      pygame.draw.rect(window,blue,(395,10,10,10)),
      pygame.draw.rect(window,blue,(395,20,10,10)),
      pygame.draw.rect(window,blue,(395,30,10,10))
      pygame.display.flip()
pygame.quit()
