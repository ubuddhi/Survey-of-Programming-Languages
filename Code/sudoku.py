import pygame, sys, time
import random
from check_sudoku import main1
from pygame.locals import *

FPS = 10

# Size of grid
WINDOWMULTIPLIER = 5 
WINDOWSIZE = 81
WINDOWWIDTH = WINDOWSIZE * WINDOWMULTIPLIER
WINDOWH=500
WINDOWHEIGHT = WINDOWSIZE * WINDOWMULTIPLIER
SQUARESIZE = int((WINDOWSIZE * WINDOWMULTIPLIER) / 3)
CELLSIZE = int(SQUARESIZE / 3) 

input_su = [2,9,5,7,4,3,8,6,1,4,3,1,8,6,5,9,2,7,8,7,6,1,9,2,5,4,3,3,8,7,4,5,9,2,1,6,6,1,2,3,8,7,4,9,5,5,4,9,2,1,6,7,3,8,7,6,3,5,2,4,1,8,9,9,2,8,6,7,1,3,5,4,1,5,4,9,3,8,6,7,2]
currentGrid = {}

# Colours
BLACK =    (0,  0,  0)
WHITE =    (255,255,255)
LIGHTGRAY = (200, 200, 200)
BLUE      = (0  ,0  ,255)
GREEN = (155,0,255)
RED = (255,0,0)

def drawGrid():

    ### Draw Minor Lines
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, LIGHTGRAY, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, LIGHTGRAY, (0,y), (WINDOWWIDTH, y))
    
    ### Draw Major Lines
    for x in range(0, WINDOWWIDTH, SQUARESIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, BLACK, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, SQUARESIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, BLACK, (0,y), (WINDOWWIDTH, y))

    pygame.draw.line(DISPLAYSURF, BLACK, (0,405), (405, 405))
    
    return None

def initiateCells():
    i=0;
    for xCoord in range(0,9):
        for yCoord in range(0,9):
            currentGrid[yCoord,xCoord] = input_su [i]
            i=i+1
    #print (currentGrid)

    return currentGrid


def generate(currentGrid):
    disp_su = random.sample(currentGrid.keys(),20)
    temp_grid = {k: currentGrid[k] if k in currentGrid else default for k in disp_su}
    
    return temp_grid

def displayCells(Grid, temp):
    for item in Grid: 
        if item in temp:
            cellData = Grid[item]
           # print (cellData)
            populateCells(cellData,(item[0]*CELLSIZE+20),(item[1]*CELLSIZE+20),'gray')

        else:
            cellData = Grid[item]
          #  print (cellData)
            populateCells(cellData,(item[0]*CELLSIZE+20),(item[1]*CELLSIZE+20),'blue')

        
    return None

def populateCells(cellData, x, y, color):
  #  print (cellData)

    if color == 'gray':
        cellSurf = BASICFONT.render('%s' %(cellData), True, LIGHTGRAY)

    elif color == 'blue':
        cellSurf = BASICFONT.render('%s' %(cellData), True, BLUE)
        
    if cellData == 0:
        cellSurf = BASICFONT.render('%s' %(cellData), True, RED)
        
    cellRect = cellSurf.get_rect()
    cellRect.topleft = (x, y)
    DISPLAYSURF.blit(cellSurf, cellRect)

def drawBox(mousex, mousey):

    boxx =((mousex*9) / WINDOWWIDTH) * (CELLSIZE ) 
    boxy =((mousey*9) / WINDOWHEIGHT) * (CELLSIZE )
   
    pygame.draw.rect(DISPLAYSURF, BLUE, (boxx,boxy,CELLSIZE,CELLSIZE), 1)

def validate(mx, my, disp_su):
    check = disp_su[mx,my]
   # print (check)

    for xCoord in range (0,9):
      #  print (check)
       # print (xCoord)
        if (xCoord, my) not in disp_su.keys():
          #  print ("hello1")
            continue
     
        if disp_su[xCoord, my] == check and xCoord != mx:
           # print ("hello2")
            disp_su[mx,my]=0                  

  #  print ("leaving 1")

    for yCoord in range (0,9):
        if (mx, yCoord) not in disp_su.keys():
         #   print ("hello4")
            continue
        
        if disp_su[mx, yCoord] == check and yCoord != my:
		#print("hello5");
            disp_su[mx,my]=0            
         
   # print ("leaving 2")

    modxNum = mx
    modyNum = my

  #  print (modxNum)
  #  print (modyNum)

    if modxNum >= 0 and modxNum < 3:                # 1st quad
        if modyNum >= 0 and modyNum < 3:
            for xCoord in range(0,3):
                for yCoord in range(0,3):
                    if (xCoord, yCoord) not in disp_su.keys():
                      #  print ("byee")
                        continue
        
                    if check == disp_su[xCoord, yCoord] and xCoord != mx and yCoord != my:
                      #  print("checked")
                        disp_su[mx,my]=0

    if modxNum >= 3 and modxNum < 6:                # 2nd quad      
        if modyNum >= 0 and modyNum < 3:
            for xCoord in range(3,6):
                for yCoord in range(0,3):
                    if (xCoord, yCoord) not in disp_su.keys():
                     #   print ("byee")
                        continue
        
                    if check == disp_su[xCoord, yCoord] and xCoord != mx and yCoord != my:
                    #    print("checked")
                        disp_su[mx,my]=0
                        

    if modxNum >= 6 and modxNum < 9:                # 3rd quad
        if modyNum >= 0 and modyNum < 3:
            for xCoord in range(6,9):
                for yCoord in range(0,3):
                    if (xCoord, yCoord) not in disp_su.keys():
                    #    print ("byee")
                        continue
        
                    if check == disp_su[xCoord, yCoord] and xCoord != mx and yCoord != my:
                     #   print("checked")
                        disp_su[mx,my]=0

    if modxNum >= 0 and modxNum < 3:                # 4th quad
        if modyNum >= 3 and modyNum < 6:
            for xCoord in range(0,3):
                for yCoord in range(3,6):
                    if (xCoord, yCoord) not in disp_su.keys():
                   #     print ("byee")
                        continue
        
                    if check == disp_su[xCoord, yCoord] and xCoord != mx and yCoord != my:
                   #     print("checked")
                        disp_su[mx,my]=0

    if modxNum >= 3 and modxNum < 6:                # 5th quad
        if modyNum >= 3 and modyNum < 6:
            for xCoord in range(3,6):
                for yCoord in range(3,6):
                    if (xCoord, yCoord) not in disp_su.keys():
                       # print ("byee")
                        continue
        
                    if check == disp_su[xCoord, yCoord] and xCoord != mx and yCoord != my:
                       # print("checked")
                        disp_su[mx,my]=0

    if modxNum >= 6 and modxNum < 9:                # 6th quad
        if modyNum >= 3 and modyNum < 6:
            for xCoord in range(6,9):
                for yCoord in range(3,6):
                    if (xCoord, yCoord) not in disp_su.keys():
                     #   print ("byee")
                        continue
        
                    if check == disp_su[xCoord, yCoord] and xCoord != mx and yCoord != my:
                     #   print("checked")
                        disp_su[mx,my]=0

    if modxNum >= 0 and modxNum < 3:                # 7th quad
        if modyNum >= 6 and modyNum < 9:
            for xCoord in range(0,3):
                for yCoord in range(6,9):
                    if (xCoord, yCoord) not in disp_su.keys():
                     #   print ("byee")
                        continue
        
                    if check == disp_su[xCoord, yCoord] and xCoord != mx and yCoord != my:
                      #  print("checked")
                        disp_su[mx,my]=0

    if modxNum >= 3 and modxNum < 6:                # 8th quad
        if modyNum >= 6 and modyNum < 9:
            for xCoord in range(3,6):
                for yCoord in range(6,9):
                    if (xCoord, yCoord) not in disp_su.keys():
                   #     print ("byee")
                        continue
        
                    if check == disp_su[xCoord, yCoord] and xCoord != mx and yCoord != my:
                    #    print("checked")
                        disp_su[mx,my]=0

    if modxNum >= 6 and modxNum < 9:                  # 9th quad
        if modyNum >= 6 and modyNum < 9:
            for xCoord in range(6,9):
                for yCoord in range(6,9):
                    if (xCoord, yCoord) not in disp_su.keys():
                   #     print ("byee")
                        continue
        
                    if check == disp_su[xCoord, yCoord] and xCoord != mx and yCoord != my:
                    #    print("checked")
                        disp_su[mx,my]=0

def text_obj(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface,textSurface.get_rect()

def button():
    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()
    
    #print(click)

    if 150+100 > mouse[0] > 150 and 420+50 > mouse[1] > 420:
        pygame.draw.rect(DISPLAYSURF, GREEN, (150, 420, 100, 50))

        if click[0]==1:
            main1()
       
    textSurf, textRect = text_obj("Solution", smallText)
    textRect.center = (200,445)
    DISPLAYSURF.blit(textSurf, textRect)    
    
def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWH))

    mouseClicked = False
    mousex = 0
    mousey = 0
    
    pygame.display.set_caption('Sudoku Solver')

    global BASICFONT, BASICFONTSIZE, smallText
    BASICFONTSIZE = 15
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    smallText = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    currentGrid = initiateCells()
    disp_su=generate(currentGrid)
   # print (disp_su)
    
    temp=list(disp_su.keys())
  #  print('temp')
  #  print(temp)


    DISPLAYSURF.fill(WHITE)
    displayCells(disp_su,temp)
    drawGrid()

    while True: 
        mouseClicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos

            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

            elif event.type == KEYDOWN and event.key == K_KP1:
            #    print('i')
            #    print(i)
                if i not in temp:
                    disp_su [mx,my] = 1
                    validate(mx,my,disp_su)
               #     print (disp_su)

            elif event.type == KEYDOWN and event.key == K_KP2:
                if i not in temp:
                    disp_su [mx,my] = 2
                    validate(mx,my,disp_su)
              #      print (disp_su)

            elif event.type == KEYDOWN and event.key == K_KP3:
                if i not in temp:
                    disp_su [mx,my] = 3
                    validate(mx,my,disp_su)
               #     print (disp_su)
			   
            elif event.type == KEYDOWN and event.key == K_KP4:
                if i not in temp:
                    disp_su [mx,my] = 4
                    validate(mx,my,disp_su)
               #     print (disp_su)
			   
            elif event.type == KEYDOWN and event.key == K_KP5:
                if i not in temp:
                    disp_su [mx,my] = 5
                    validate(mx,my,disp_su)
              #      print (disp_su)
					
            elif event.type == KEYDOWN and event.key == K_KP6:
                if i not in temp:
                    disp_su [mx,my] = 6
                    validate(mx,my,disp_su)
               #     print (disp_su)
					
            elif event.type == KEYDOWN and event.key == K_KP7:
                if i not in temp:
                    disp_su [mx,my] = 7
                    validate(mx,my,disp_su)
               #     print (disp_su)
					
            elif event.type == KEYDOWN and event.key == K_KP8:
                if i not in temp:
                    disp_su [mx,my] = 8
                    validate(mx,my,disp_su)
              #      print (disp_su)
			  
            elif event.type == KEYDOWN and event.key == K_KP9:
                if i not in temp:
                    disp_su [mx,my] = 9
                    validate(mx,my,disp_su)
                #    print (disp_su)
                
        if mouseClicked == True:
            mx = int(mousex/45)
            my = int(mousey/45)

            i=(mx,my)
       #     print ('i')
        #    print (i)
		
        DISPLAYSURF.fill(WHITE)
     
        displayCells(disp_su, temp)
        drawGrid()
        drawBox(mousex,mousey)

        button()

        pygame.display.update()    
        FPSCLOCK.tick(FPS)
        
if __name__=='__main__':
    main()
