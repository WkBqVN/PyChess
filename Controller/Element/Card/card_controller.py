# Vẽ hàng màu trắng ở dưới
#    pygame.draw.rect(window, (255, 255, 255), (0, config.WINDOW_HEIGHT - 108, config.WINDOW_WIDTH, 108))


import pygame
import Core.config as config

class CardPanel:
    def __init__(self):
        return
    def draw_card_panel(self,window):
        pygame.draw.rect(window, (255, 255, 255), (0, config.WINDOW_HEIGHT - 108, config.WINDOW_WIDTH, 108))