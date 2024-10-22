import pygame
import math
from Controller.Element.Map import map_util
import Core.config as config
import Core.loader as loader
from Model.Enviroment.Tile.grass import TileGrass
from Model.Enviroment.Tile.sand import TileSand
from Model.Enviroment.Tile.snow import TileSnow

class MatchMap:
    def __init__(self, maps, origin=(0, 0)):
        #delete later
        # map_util.generate_centers(1600,900,32,"map_1")
        # map_util.generate_centers(1600,900,32,"map_2")

        self.clicked_tile = None
        self.origin = origin  # Lưu tọa độ gốc của bản đồ
        self.grid_size = int(config.CELL_SIZE * 1.5)  # Đặt kích thước ô lưới
        self.grid = {}  # Khởi tạo lưới
        self.list_map = maps                                                    #total 15 map
        self.list_hexa = loader.load_hex_data_from_config(config.HEX_GENERATED_PATHS + "Hex_generated.conf")
        print(self.list_hexa)
        self.populate_grid()
        return

    def set_clicked_tile(self,clicked_point):
        self.clicked_tile = clicked_point

    def populate_grid(self):
        """Tạo lưới từ các lục giác."""
        for hex_data in self.list_hexa:
            grid_x = int(hex_data[0] // self.grid_size)
            grid_y = int(hex_data[1] // self.grid_size)

            if (grid_x, grid_y) not in self.grid:
                self.grid[(grid_x, grid_y)] = []
            self.grid[(grid_x, grid_y)].append(hex_data)

    def find_clicked_hexagon(self, click_pos):
        """Tìm lục giác được click gần nhất."""
        grid_x = int(click_pos[0] // self.grid_size)
        grid_y = int(click_pos[1] // self.grid_size)

        # Kiểm tra ô lưới và các ô lân cận
        for dx in range(-1, 2):  # Kiểm tra ô hiện tại và 1 ô lân cận
            for dy in range(-1, 2):
                grid_cell = (grid_x + dx, grid_y + dy)
                if grid_cell in self.grid:
                    for hex_data in self.grid[grid_cell]:
                        hex_center = hex_data["center"]
                        if self.distance_between_points(click_pos, hex_center) <= self.hex_size:
                            return hex_data  # Trả về lục giác được click
        return None

    def distance_between_points(self, p1, p2):
        """Tính khoảng cách giữa hai điểm."""
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    
    def create_hexagon(self, center, size):
        """ Tạo một hình lục giác với bán kính `size` tại vị trí `center`. """
        points = []
        for i in range(6):  # 6 cạnh của lục giác
            angle = math.radians(60 * i)  # Góc giữa các đỉnh
            x = center[0] + size * math.cos(angle)
            y = center[1] + size * math.sin(angle)
            points.append((x, y))
        return points  # Có tổng cộng 6 points