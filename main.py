# Importing the pygame module
import pygame
import sys 
import Core.util.mouse
import Controller.Map.map_controller
import Core.config as config
import Core.loader as loader

from Model.Unit.Infantry.infantry import Infantry
from Controller.Character.character_controller import CharacterManager
from pygame.locals import *

# Initiate pygame
pygame.init()

# Create a display surface object of specific dimension
window = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))

# Create a new clock object to track time
clock = pygame.time.Clock()

# Boolean variable to run the game loop
run = True
###############################################

character_manager = CharacterManager()
map_manager = Controller.Map.map_controller.MapManager()

u = Infantry("infantry_roman",[300,300])
character_manager.add_character(u)

###############################################
map_1 = [
    [0,0,0,0,0,2,0,0],
    [1,0,0,0,0,0,0,0],
    [0,2,1,0,0,1,3,0],
    [0,0,0,3,0,0,0,0],
    [0,0,3,0,2,0,0,0],
    [0,2,0,0,0,2,3,0],
    [1,0,0,2,0,0,2,0],
    [0,2,0,0,0,1,0,0],
    [0,1,0,3,0,0,0,0],
]

# Load terrain tiles
grass_1_tile = loader.load_image_frames('C:\\Work\\PyChess\\Asset\\Terrain\\grass-fall.png', None, 100, 100)[0]
grass_2_tile = loader.load_image_frames('C:\\Work\\PyChess\\Asset\\Terrain\\grass-spring.png', None, 100, 100)[0]
grass_3_tile = loader.load_image_frames('C:\\Work\\PyChess\\Asset\\Terrain\\grass-summer.png', None, 100, 100)[0]
grass_4_tile = loader.load_image_frames('C:\\Work\\PyChess\\Asset\\Terrain\\grass-winter.png', None, 100, 100)[0]


clicked_tiles=[None,None]

# Infinite loop to run the game
while run:
    # fps
    clock.tick(120)
    # Process events (e.g., close window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:
                clicked_tiles=[mouse_pos[0]//100, mouse_pos[1]//100]
                character_manager.characters[0].move()
            elif event.button == 3:
                character_manager.characters[0].hold()
                print("right")

    # Clear the screen with black color
    window.fill((0, 0, 0))

    # Draw the map
    map_manager.draw_map(window, map_1, {
        0: grass_1_tile,
        1: grass_2_tile,
        2: grass_3_tile,
        3: grass_4_tile
    },clicked_tiles)

    # Displaying the image in our game window
    #window.blit(image, character_pos)
    character_manager.draw_character(window)

    # Updating the display surface
    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()  # Ensure a clean exit
