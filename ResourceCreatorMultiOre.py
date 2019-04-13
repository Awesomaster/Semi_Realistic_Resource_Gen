import random
import time
import pygame
import math

sizex = 50
sizey = 50
quality = 4

inv = {'Rubies':0, 'Emeralds':0, 'Sapphires':0}

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
            num = int(random.randint(25,100)*orig*(0.01))
            if grid[x][y-1] < 1:
                grid[x][y-1] = num
                if num > 1:
                    queue.append([x,y-1])
        if y < (sizey-1):
            num = int(random.randint(25,100)*orig*(0.01))
            if grid[x][y+1] < 1:
                grid[x][y+1] = num
                if num > 1:
                    queue.append([x,y+1])
        if x > 0:
            num = int(random.randint(25,100)*orig*(0.01))
            if grid[x-1][y] < 1:
                grid[x-1][y] = num
                if num > 1:
                    queue.append([x-1,y])
        if x < (sizex-1):
            num = int(random.randint(25,100)*orig*(0.01))
            if grid[x+1][y] < 1:
                grid[x+1][y] = num
                if num > 1:
                    queue.append([x+1,y])

check(xred,yred,gridred)
print('Red')
check(xblue,yblue,gridblue)
print('Blue')
check(xgreen,ygreen,gridgreen)
print('Green')

print('Left Click to Mine')
print('Right Click to Print Inv')

for i in range(sizex):
    for j in range(sizey):
        if (gridred[i][j]/1000) >= 0.02:
            gridred[i][j] = gridred[i][j]/1000
        else:
            gridred[i][j] = 0
        if (gridblue[i][j]/1000) >= 0.02:
            gridblue[i][j] = gridblue[i][j]/1000
        else:
            gridblue[i][j] = 0
        if (gridgreen[i][j]/1000) >= 0.02:
            gridgreen[i][j] = gridgreen[i][j]/1000
        else:
            gridgreen[i][j] = 0

black = (0,0,0)

width = 16
height = 16
margin = 2

pygame.init()
 
window_size = [width*sizex+margin*(sizex+1), height*sizey+margin*(sizey+1)]
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Resource Distribution")
 
done = False

clock = pygame.time.Clock()

def print_inv():
    if inv['Rubies'] >= 10000:
        print('Rubies:', str(round(inv['Rubies']/1000,1))+'K')
    else:
        print('Rubies:', str(inv['Rubies']))
    if inv['Emeralds'] >= 10000:
        print('Emeralds:', str(round(inv['Emeralds']/1000,1))+'K')
    else:
        print('Emeralds:', str(inv['Emeralds']))
    if inv['Sapphires'] >= 10000:
        print('Sapphires:', str(round(inv['Sapphires']/1000,1))+'K')
    else:
        print('Sapphires:', str(inv['Sapphires']))

def draw_grid(sizex,sizey):
    screen.fill(black)

    for i in range(sizex):
        for j in range(sizey):
            draw_block(i,j,True)
    clock.tick(60)
    pygame.display.flip()
                
def draw_block(i,j,initial):
    red = gridred[i][j]
    blue = gridblue[i][j]
    green = gridgreen[i][j]
    
    if max(red,green,blue) == red:
        for minii in range(quality):
            for minij in range(quality):
                value = red*1000
                randint = random.randint(0,1100)

                if value > randint:
                    redcolour = (255-random.randint(0,20),0,0)
                    colour = redcolour
                else:
                    stonecolour = (155+random.randint(-10,10),155+random.randint(-10,10),155+random.randint(-10,10))
                    colour = stonecolour

                pygame.draw.rect(screen,
                                 colour,
                                 [(margin)*(i+1) + (width)/quality * (minii+i*quality),
                                  (margin)*(j+1) + (height)/quality * (minij+j*quality),
                                  width/quality,
                                  height/quality])
    if max(red,green,blue) == green:
        for minii in range(quality):
            for minij in range(quality):
                value = green*1000
                randint = random.randint(0,1100)

                if value > randint:
                    greencolour = (0,255-random.randint(0,20),0)
                    colour = greencolour
                else:
                    stonecolour = (155+random.randint(-10,10),155+random.randint(-10,10),155+random.randint(-10,10))
                    colour = stonecolour

                pygame.draw.rect(screen,
                                 colour,
                                 [(margin)*(i+1) + (width)/quality * (minii+i*quality),
                                  (margin)*(j+1) + (height)/quality * (minij+j*quality),
                                  width/quality,
                                  height/quality])
    if max(red,green,blue) == blue:
        for minii in range(quality):
            for minij in range(quality):
                value = blue*1000
                randint = random.randint(0,1100)

                if value > randint:
                    bluecolour = (0,0,255-random.randint(0,20))
                    colour = bluecolour
                else:
                    stonecolour = (155+random.randint(-10,10),155+random.randint(-10,10),155+random.randint(-10,10))
                    colour = stonecolour

                pygame.draw.rect(screen,
                                 colour,
                                 [(margin)*(i+1) + (width)/quality * (minii+i*quality),
                                  (margin)*(j+1) + (height)/quality * (minij+j*quality),
                                  width/quality,
                                  height/quality])
    if initial:
        if max(red,green,blue) == 0:
            for minii in range(quality):
                for minij in range(quality):
                    grasscolour = (120+random.randint(-10,10),180+random.randint(-10,10),75+random.randint(-10,10))
                    colour = grasscolour
                    pygame.draw.rect(screen,
                                     colour,
                                     [(margin)*(i+1) + (width)/quality * (minii+i*quality),
                                      (margin)*(j+1) + (height)/quality * (minij+j*quality),
                                      width/quality,
                                      height/quality])
    else:
        if max(red,green,blue) == 0:
            for minii in range(quality):
                for minij in range(quality):
                    dirtcolour = (115+random.randint(-10,10),90+random.randint(-10,10),60+random.randint(-10,10))
                    colour = dirtcolour
                    pygame.draw.rect(screen,
                                     colour,
                                     [(margin)*(i+1) + (width)/quality * (minii+i*quality),
                                      (margin)*(j+1) + (height)/quality * (minij+j*quality),
                                      width/quality,
                                      height/quality])
    clock.tick(60)
    pygame.display.flip()


objectgrid = []
for i in range(sizex):
    objectgrid.append([])
    for j in range(sizey):
        objectgrid[i].append(0)
objects = {'conveyorup':1,'conveyordown':2,'conveyorleft':3,'conveyorright':4}

draw_grid(sizex,sizey)
running = True

while running:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            column = pos[1] // (height+margin)
            row = pos[0] // (width+margin)

            if event.button == 1:
                if row >= sizex:
                    running = False
                else:
                    
                    #Add Rubies
                    if gridred[row][column] >= 0.1:
                        inv['Rubies'] += 100
                        gridred[row][column] -= 0.1
                    else:
                        inv['Rubies'] += int(gridred[row][column]*1000)
                        gridred[row][column] = 0

                    #Add Emeralds
                    if gridgreen[row][column] >= 0.1:
                        inv['Emeralds'] += 100
                        gridgreen[row][column] -= 0.1
                    else:
                        inv['Emeralds'] += int(gridgreen[row][column]*1000)
                        gridgreen[row][column] = 0

                    #Add Sapphires
                    if gridblue[row][column] >= 0.1:
                        inv['Sapphires'] += 100
                        gridblue[row][column] -= 0.1
                    else:
                        inv['Sapphires'] += int(gridblue[row][column]*1000)
                        gridblue[row][column] = 0

                    
                    
                    draw_block(row,column,False)
            elif event.button == 3:
                if row >= sizex:
                    running = False
                else:
                    print_inv()


pygame.quit()


