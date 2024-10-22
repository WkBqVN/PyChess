import pygame
import Core.config as config

class RightPanel:
    def __init__(self):
        return

    def draw_right_panel(self,window):
        pygame.draw.rect(window, (255,255,255), (1590, 0, 320, config.WINDOW_HEIGHT))  # Cột trắng dài 320px