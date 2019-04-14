#Gets the constants and other libraries
import pygame,sys
from pygame.locals import *
import constant as const

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
	#Making the player
	global PLAYER
	global playerPos
	PLAYER = pygame.image.load('PLAYER.png').convert_alpha()
	playerPos = [0,0]
	#font for our inventory
	global INVFONT
	INVFONT = pygame.font.Font('FreeSansBold.ttf', 18)

def game():
	while True:
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
					print(inventory)

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

		#update the display
		pygame.display.update()

inital()
game()