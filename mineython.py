#Gets the constants and other libraries
import random
import pygame,sys
from pygame.locals import *
import constant as const

#Declaring a key press inventory
key = {
	const.DIRT : K_1,
	const.GRASS : K_2,
	const.WATER : K_3,
	const.COAL : K_4,
	const.ROCK : K_5,
	const.LAVA : K_6
}


#Declaring an inventory
inventory = {
	const.DIRT : 0,
	const.GRASS : 0,
	const.WATER : 0,
	const.COAL : 0,
	const.ROCK : 0,
	const.LAVA : 0
}

def inital():
	#Initializes the game and display part
	pygame.init()
	global screen
	screen = pygame.display.set_mode((const.MAPWIDTH * const.TILESIZE, const.MAPHEIGHT * const.TILESIZE + const.INVENTORY_HEIGHT))
	pygame.display.set_caption('Mineython')
	pygame.display.set_icon(pygame.image.load('PLAYER.png'))
	#Making the player
	global PLAYER
	global playerPos
	PLAYER = pygame.image.load('PLAYER.png').convert_alpha()
	playerPos = [0,0]
	#font for our inventory
	global INVFONT
	INVFONT = pygame.font.Font('FreeSansBold.ttf', 18)

def animate(speed,texture,coord):
	screen.blit(const.textures[texture].convert_alpha(),coord)
	coord[0] += speed
	if coord[0] > const.MAPWIDTH * const.TILESIZE:
		coord[1] = random.randint(0, const.MAPHEIGHT * const.TILESIZE - const.TILESIZE)
		coord[0] = -200

cloudy = [-200,0]
cloudy2 = [300,2]
bird = [-100,2]

def game():
	while True:
		screen.fill(const.BLACK)
		#Fps counter set to 24 frames
		fpsClock = pygame.time.Clock()
		#Getting curent events and responding
		for event in pygame.event.get():
			#print(event)
			#If the player wants to quit
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				#Player movement
				if event.key == K_RIGHT and playerPos[0] < const.MAPWIDTH - 1:
					playerPos[0] += 1
				elif event.key == K_LEFT and playerPos[0] > 0:
					playerPos[0] -= 1
				elif event.key == K_DOWN and playerPos[1] < const.MAPHEIGHT - 1:
					playerPos[1] += 1
				elif event.key == K_UP  and playerPos[1] > 0:
					playerPos[1] -= 1
				#Player inventory logic
				elif event.key == K_SPACE:
					curentTile = const.tilemap[playerPos[1]][playerPos[0]]
					if curentTile != const.DIRT and curentTile != const.LAVA:
						inventory[curentTile] += 1
						const.tilemap[playerPos[1]][playerPos[0]] = const.DIRT
				for item in const.resources:
					if event.key == key[item]:
						curentTile = const.tilemap[playerPos[1]][playerPos[0]]
						if inventory[item] > 0:
							inventory[item] -= 1
							const.tilemap[playerPos[1]][playerPos[0]] = item
							if curentTile !=const.LAVA:
								inventory[curentTile] += 1
		#Drawing the map
		for row in range(const.MAPHEIGHT):
			for column in range(const.MAPWIDTH):
				screen.blit(const.textures[const.tilemap[row][column]], (column*const.TILESIZE, row*const.TILESIZE, const.TILESIZE, const.TILESIZE))
		
		#Displaying the player
		screen.blit(PLAYER,(playerPos[0] * const.TILESIZE, playerPos[1] * const.TILESIZE))

		#Displaying the inventory
		placePosition = const.INVENTORY_START_POSITION
		for item in const.resources:
			screen.blit(const.textures[item], (placePosition, const.MAPHEIGHT * const.TILESIZE + const.INVENTORY_SPACE_BETWEEN))
			placePosition += const.INVENTORY_SPACE_WIDTH
			textObj = INVFONT.render(str(inventory[item]), True, const.WHITE, const.BLACK)
			screen.blit(textObj, (placePosition + const.INVENTORY_SPACE_BETWEEN, const.MAPHEIGHT * const.TILESIZE + const.INVENTORY_SPACE_WIDTH))
			placePosition += const.INVENTORY_HEIGHT

		#Displaying the cloud
		animate(1, const.CLOUD, cloudy)
		animate(3, const.BIRD, bird)
		animate(2, const.CLOUD, cloudy2)

		#update the display
		pygame.display.update()
		fpsClock.tick(24)

inital()
game()
