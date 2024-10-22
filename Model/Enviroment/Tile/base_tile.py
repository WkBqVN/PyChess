#base for tile
from Core import loader
import pygame

class Tile:
    def __init__(self,data):
        self.tile_data = data
        self.load_images(self.tile_data["asset"])
        self.init_animation()
        return

    def init_animation(self):
        self.current_frame = 0
        self.frame_time = 300                                                   # Thời gian giữa mỗi khung hình (300ms)
        self.last_update = pygame.time.get_ticks()

    def load_images(self,asset):
        self.frame_dict = {
            "is_normal": loader.load_image_frames(asset["asset_normal"]["path"]) 
        }
        return
    def update_animation(self):
        return pygame.transform.scale(self.frame_dict["is_normal"][self.current_frame], (32, 32)) 
    
    def get_tile(self):
        return
