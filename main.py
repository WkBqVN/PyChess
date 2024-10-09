import pygame
import requests
import constant.asset_url
import constant.init_constants
import core
import rembg
import constant

from io import BytesIO

# Initialize Pygame
pygame.init()

#init size
screen = pygame.display.set_mode(
    [constant.init_constants.WIDTH,constant.init_constants.HEIGHT])

pygame.display.set_caption("Chess game")

# Load fonts
# Set up clock and FPS
timer = pygame.time.Clock()
fps = 60

abc = core.load_image(constant.asset_url.Asset_Soldier)

# Main game loop
running = True
while running:
    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    screen.fill((255, 255, 255))  # RGB: white background
    abc.show()
    # Update the display
    pygame.display.flip()

    # Tick the clock to maintain the FPS
    timer.tick(fps)

# Quit Pygame when the loop ends
pygame.quit()
