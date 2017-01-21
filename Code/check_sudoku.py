import pygame, sys
import random
from pygame.locals import *

WINDOWMULTIPLIER = 5 
WINDOWSIZE = 81
WINDOWWIDTH = WINDOWSIZE * WINDOWMULTIPLIER
WINDOWHEIGHT = WINDOWSIZE * WINDOWMULTIPLIER
SQUARESIZE = int((WINDOWSIZE * WINDOWMULTIPLIER) / 3) 
CELLSIZE = int(SQUARESIZE / 3)

input_su = [2,9,5,7,4,3,8,6,1,4,3,1,8,6,5,9,2,7,8,7,6,1,9,2,5,4,3,3,8,7,4,5,9,2,1,6,6,1,2,3,8,7,4,9,5,5,4,9,2,1,6,7,3,8,7,6,3,5,3,4,1,8,9,9,2,8,6,7,1,3,5,4,1,5,4,9,3,8,6,7,2]

LIGHTGRAY = (200, 200, 200)
BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)

def drawGrid():

    for x in range(0, WINDOWWIDTH, CELLSIZE): 
        pygame.draw.line(DISPLAYSURF1, LIGHTGRAY, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, CELLSIZE): 
        pygame.draw.line(DISPLAYSURF1, LIGHTGRAY, (0,y), (WINDOWWIDTH, y))
    
    for x in range(0, WINDOWWIDTH, SQUARESIZE): 
        pygame.draw.line(DISPLAYSURF1, BLACK, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, SQUARESIZE): 
        pygame.draw.line(DISPLAYSURF1, BLACK, (0,y), (WINDOWWIDTH, y))

    return None

def initiateCells():
    currentGrid = {}

    i=0;
    for xCoord in range(0,9):
        for yCoord in range(0,9):
            currentGrid[yCoord,xCoord] = input_su[i]
            i=i+1

    return currentGrid


def displayCells(currentGrid):
   
    for item in currentGrid: 
        cellData = currentGrid[item] 
        populateCells(cellData,(item[0]*CELLSIZE+20),(item[1]*CELLSIZE+20))
    return None


def populateCells(cellData, x, y):
    cellSurf = BASICFONT.render('%s' %(cellData), True, LIGHTGRAY)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = (x, y)
    DISPLAYSURF1.blit(cellSurf, cellRect)

def drawBox(mousex, mousey):

    boxx =((mousex*9) / WINDOWWIDTH) * (CELLSIZE ) 
    boxy =((mousey*9) / WINDOWHEIGHT) * (CELLSIZE ) 
   
    pygame.draw.rect(DISPLAYSURF1, BLUE, (boxx,boxy,CELLSIZE,CELLSIZE), 1)

    
def main1():
    global FPSCLOCK, DISPLAYSURF1
    #pygame.init()
    DISPLAYSURF1 = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

    pygame.display.set_caption('Solution')

    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 15
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    currentGrid = initiateCells()

    DISPLAYSURF1.fill(WHITE)
    displayCells(currentGrid)
    drawGrid()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        
        DISPLAYSURF1.fill(WHITE)
        displayCells(currentGrid)
        drawGrid()
        
        pygame.display.update()    

if __name__=='__main__':
    main1()

