import random
import time
import pygame
import math

sizex = 50
sizey = 50

resourcegrid = []
for i in range(sizex):
    resourcegrid.append([])
    for j in range(sizey):
        resourcegrid[i].append(0)

x = random.randint(0,sizex-1)
y = random.randint(0,sizey-1)


resourcegrid[x][y] = 1000

gridred = []
for i in range(sizex):
    gridred.append([])
    for j in range(sizey):
        gridred[i].append(0)
xred = random.randint(0,sizex-1)
yred = random.randint(0,sizey-1)
'''
xred = x
yred = y
'''
gridred[xred][yred] = 1000

gridblue = []
for i in range(sizex):
    gridblue.append([])
    for j in range(sizey):
        gridblue[i].append(0)
xblue = random.randint(0,sizex-1)
yblue = random.randint(0,sizey-1)
'''
xblue = x
yblue = y
'''
gridblue[xblue][yblue] = 1000

gridgreen = []
for i in range(sizex):
    gridgreen.append([])
    for j in range(sizey):
        gridgreen[i].append(0)
xgreen = random.randint(0,sizex-1)
ygreen = random.randint(0,sizey-1)
'''
xgreen = x
ygreen = y
'''
gridgreen[xgreen][ygreen] = 1000

def check(i,j,grid):
    checked = []
    queue = []
    current = [i,j]
    queue.append(current)
    print(current)
    while queue:
        current = queue.pop(0)
        checked.append(current)
        #print(current)
        x = current[0]
        y = current[1]
        orig = grid[x][y]
        if y > 0:
            num = int(random.randint(50,100)*orig*(0.01))
            if grid[x][y-1] < 1:
                grid[x][y-1] = num
                if num > 1:
                    queue.append([x,y-1])
        if y < (sizey-1):
            num = int(random.randint(50,100)*orig*(0.01))
            if grid[x][y+1] < 1:
                grid[x][y+1] = num
                if num > 1:
                    queue.append([x,y+1])
        if x > 0:
            num = int(random.randint(50,100)*orig*(0.01))
            if grid[x-1][y] < 1:
                grid[x-1][y] = num
                if num > 1:
                    queue.append([x-1,y])
        if x < (sizex-1):
            num = int(random.randint(50,100)*orig*(0.01))
            if grid[x+1][y] < 1:
                grid[x+1][y] = num
                if num > 1:
                    queue.append([x+1,y])

check(x,y,resourcegrid)
print('Resourcegrid')


check(xred,yred,gridred)
print('Red')
check(xblue,yblue,gridblue)
print('Blue')
check(xgreen,ygreen,gridgreen)
print('Green')

for i in range(sizex):
    for j in range(sizey):
        resourcegrid[i][j] = resourcegrid[i][j]/1000
        gridred[i][j] = gridred[i][j]/1000
        gridblue[i][j] = gridblue[i][j]/1000
        gridgreen[i][j] = gridgreen[i][j]/1000

black = (0,0,0)

WIDTH = 10
HEIGHT = 10
MARGIN = 2

pygame.init()
 
WINDOW_SIZE = [WIDTH*sizex+MARGIN*(sizex+1), HEIGHT*sizey+MARGIN*(sizey+1)]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Resource Distribution")
 
done = False

clock = pygame.time.Clock()

def draw_grid(sizex,sizey):
    screen.fill(black)
    redcolour = (255,0,0)
    greencolour = (0,255,0)
    bluecolour = (0,0,255)
    grasscolour = (120,180,75)
    stonecolour = (155,155,155)

    for i in range(sizex):
        for j in range(sizey):
            block = resourcegrid[i][j]
            red = gridred[i][j]
            blue = gridblue[i][j]
            green = gridgreen[i][j]

            colour = (255*red, 255*green, 255*blue)
            
            pygame.draw.rect(screen,
                             colour,
                             [(MARGIN + WIDTH) * i + MARGIN,
                              (MARGIN + HEIGHT) * j + MARGIN,
                              WIDTH,
                              HEIGHT])
    
    clock.tick(60)
    pygame.display.flip()

objectgrid = []
for i in range(sizex):
    objectgrid.append([])
    for j in range(sizey):
        objectgrid[i].append(0)
objects = {'conveyorup':1,'conveyordown':2,'conveyorleft':3,'conveyorright':4}


while True:
    draw_grid(sizex,sizey)
    time.sleep(0.01)


pygame.quit()


