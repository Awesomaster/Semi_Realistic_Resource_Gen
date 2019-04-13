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

check(x,y,resourcegrid)
print('Resourcegrid')

for i in range(sizex):
    for j in range(sizey):
        if (resourcegrid[i][j]/1000) >= 0.02:
            resourcegrid[i][j] = resourcegrid[i][j]/1000
        else:
            resourcegrid[i][j] = 0

black = (0,0,0)

width = 16
height = 16
margin = 4

pygame.init()
 
window_size = [width*sizex+margin*(sizex+1), height*sizey+margin*(sizey+1)]
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Resource Distribution")
 
done = False

clock = pygame.time.Clock()

def draw_grid(sizex,sizey):
    screen.fill(black)

    for i in range(sizex):
        for j in range(sizey):
            block = resourcegrid[i][j]

            if block > 0:
                for minii in range(4):
                    for minij in range(4):
                        value = block*1000
                        randint = random.randint(0,1100)

                        if value > randint:
                            uraniumcolour = (0,0,255-random.randint(0,20))
                            colour = uraniumcolour
                        else:
                            stonecolour = (155+random.randint(-10,10),155+random.randint(-10,10),155+random.randint(-10,10))
                            colour = stonecolour

                        pygame.draw.rect(screen,
                                         colour,
                                         [(margin)*(i+1) + (width)/4 * (minii+i*4),
                                          (margin)*(j+1) + (height)/4 * (minij+j*4),
                                          width/4,
                                          height/4])
            else:
                for minii in range(4):
                    for minij in range(4):
                        grasscolour = (120+random.randint(-10,10),180+random.randint(-10,10),75+random.randint(-10,10))
                        colour = grasscolour
                        pygame.draw.rect(screen,
                                         colour,
                                         [(margin)*(i+1) + (width)/4 * (minii+i*4),
                                          (margin)*(j+1) + (height)/4 * (minij+j*4),
                                          width/4,
                                          height/4])
                
    
    clock.tick(60)
    pygame.display.flip()

objectgrid = []
for i in range(sizex):
    objectgrid.append([])
    for j in range(sizey):
        objectgrid[i].append(0)
objects = {'conveyorup':1,'conveyordown':2,'conveyorleft':3,'conveyorright':4}

draw_grid(sizex,sizey)
while True:
    
    time.sleep(0.01)


pygame.quit()


