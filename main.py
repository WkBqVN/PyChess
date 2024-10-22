import pygame
import sys
from Controller.Element.Match.match_controller import Match
from Controller.Element.Match.right_panel_controller import RightPanel
from Core.screen import create_screen
import Controller.Element.Map.map_controller as map_controller
import Core.config as config
import Core.loader as loader

from Core.util.mouse import get_character_pos
from Core.networking.connect import Connector

from Model.Unit.Infantry.infantry import Infantry

from pygame.locals import *

from Model.Unit.Infantry.infantry_constant import export_to_json

# Initiate pygame
pygame.init()

# Create a display surface object of specific dimension
window = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))

# Create a new clock object to track time
clock = pygame.time.Clock()

# Boolean variable to run the game loop
run = True

# Initialize managers
connector = Connector()

# Initialize clicked tiles
clicked_tiles = {"center": [400,400], "tile": {}}
elapsed_time=0
m = Match(None)

# abc = export_to_json("./")

# Infinite loop to run the game
while run:
    # Set frames per second
    delta_time=clock.tick(120)
    elapsed_time += delta_time
    
    # Clear the screen with black color
    window.fill((0, 0, 0))

    m.start_match(window)

    # Process events (e.g., close window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
                break
        m.handleEvent(event)
    if connector:
        if elapsed_time >= 60000: # minutes cd
            connector.send_match_data('{"hello":"world"}')
            elapsed_time = 0

    # Updating the display surface
    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()  # Ensure a clean exit
