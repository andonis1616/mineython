#Libraries to include
import random
import pygame,sys
from pygame.locals import *

#Materials
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
LAVA = 5
CLOUD = 6
BIRD = 7
resources = [DIRT, GRASS, WATER, COAL, ROCK, LAVA]

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
RED = (255, 0, 0)

#Assigning each material a color
textures = {
	DIRT : pygame.image.load('DIRT.png'),
	GRASS : pygame.image.load('GRASS.png'),
	WATER : pygame.image.load('WATER.png'),
	COAL : pygame.image.load('COAL.png'),
	ROCK : pygame.image.load('ROCK.png'),
	LAVA : pygame.image.load('LAVA.png'),
	CLOUD : pygame.image.load('CLOUD.png'),
	BIRD : pygame.image.load('BIRD.png')
}

#Game dimentions
TILESIZE = 40
MAPWIDTH = 15
MAPHEIGHT = 15
INVENTORY_START_POSITION = 10
INVENTORY_HEIGHT = 70
INVENTORY_SPACE_BETWEEN = 20
INVENTORY_SPACE_WIDTH = 30

#Generate a tilemap randomly
# 20 - 100%
# 1/20 - 5%
# GRASS - 15%
# ROCK, WATER - 10%
# LAVA, COAL - 5%
tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]
for w in range(MAPHEIGHT):
	for c in range(MAPWIDTH):
		randomNumber = random.randint(1,20)
		if randomNumber == 1:
			tile = LAVA
		elif randomNumber == 2:
			tile = COAL
		elif randomNumber == 3 or randomNumber == 4:
			tile = ROCK
		elif randomNumber == 5 or randomNumber == 6:
			tile = WATER
		elif randomNumber >= 7 and randomNumber <= 9:
			tile = GRASS
		else:
			tile = DIRT
		tilemap[w][c] = tile
