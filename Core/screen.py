import pygame

def create_screen(screen_mode):
    print(screen_mode)
    if screen_mode == "fullscreen":
        return pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Toàn màn hình
    if screen_mode == "1600×900":
        return pygame.display.set_mode(1600,900)
    if screen_mode == "1280x800":
        return pygame.display.set_mode(1280,720) 
    if screen_mode == "1024x768":
        return pygame.display.set_mode(1280,720) 