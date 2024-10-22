import pygame
import math
from Controller.Element.Map import map_util
from Controller.Element.Map.map_match import MatchMap
import Core.config as config
import Core.loader as loader
from Model.Enviroment.Tile.grass import TileGrass
from Model.Enviroment.Tile.sand import TileSand
from Model.Enviroment.Tile.snow import TileSnow

class MapController:
    def __init__(self):  # Thêm tham số origin để xác định điểm gốc
        self.map_match = MatchMap()
        return
        # map_util.generate_centers(1600, 900, 32)

    def draw_match_map(self, window, map_match):
        """Vẽ bản đồ lục giác trên cửa sổ dựa trên list_hexa."""
        fog_surface = pygame.Surface((config.WINDOW_WIDTH, config.WINDOW_HEIGHT), pygame.SRCALPHA)
        fog_surface.fill((0, 0, 0, 0))
        for hex_data in map_match.list_hexa:
            hex_center = [float(hex_data[0]), float(hex_data[1])]
            tile = hex_data["tile"]
            # Tạo các điểm cho hình lục giác
            hex_points = self.create_hexagon(hex_center, config.CELL_SIZE)
            # Vẽ hình ảnh lục giác (nếu có hình ảnh tile)
            if tile:
                # Lấy hình ảnh từ tile và vẽ lên window
                # tile_image = tile.update_animation()  # Lấy hình ảnh đã cập nhật
                # rotated_image = pygame.transform.rotate(tile_image, 90)
                # resized_image = pygame.transform.scale(rotated_image, (int(70), int(70)))
                # Tính toán vị trí để căn giữa hình ảnh
                resized_image = pygame.transform.scale(pygame.transform.rotate(tile.update_animation(),90), 
                                                    (int(70), int(70)))
                tile_rect = resized_image.get_rect(center=(hex_center[0], hex_center[1]))
                # Vẽ hình ảnh ở vị trí đã tính toán
                window.blit(resized_image, tile_rect.topleft)
            # Nếu lục giác này là ô được click thì vẽ viền xanh
            if map_match.clicked_tile and hex_center == map_match.clicked_tile:
                pygame.draw.polygon(window, (0, 255, 0), hex_points, 1)
            else:
                pygame.draw.polygon(window, (255, 0, 0), hex_points, 1)
            # Kiểm tra xem ô này có phải là ô trong danh sách unit không
            if hex_center not in map_match.list_unit and hex_center != map_match.clicked_tile: 
            # Vẽ lớp mờ hình lục giác lên fog_surface
                pygame.draw.polygon(fog_surface, (0, 0, 0, 150), hex_points) 
        window.blit(fog_surface, (0, 0))  # Vẽ lớp phủ lên cửa sổ
    
    def draw_advantage_map():
        return
