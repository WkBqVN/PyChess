import pygame
import math
from Controller.Element.Map import map_util
import Core.config as config
import Core.loader as loader
from Model.Enviroment.Tile.grass import TileGrass
from Model.Enviroment.Tile.sand import TileSand
from Model.Enviroment.Tile.snow import TileSnow

class MapManager:
    def __init__(self, hex_size, origin=(0, 0)):  # Thêm tham số origin để xác định điểm gốc
        self.hex_size = hex_size
        self.origin = origin  # Lưu tọa độ gốc của bản đồ
        self.grid_size = int(hex_size * 1.5)  # Đặt kích thước ô lưới
        self.grid = {}  # Khởi tạo lưới
        self.list_hexa = self.load_hex_data(loader.load_hex_map_data(config.HEX_GENERATED_PATHS))
        self.populate_grid()

        self.map_offset_x = 0
        self.map_offset_y =0
        self.map_move = 10

        map_util.generate_centers(1600, 900, 32)
    def populate_grid(self):
        """Tạo lưới từ các lục giác."""
        for hex_data in self.list_hexa:
            hex_center = hex_data["center"]
            grid_x = int(hex_center[0] // self.grid_size)
            grid_y = int(hex_center[1] // self.grid_size)

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

    def load_hex_data(self, map_hex):
        list_hex = []
        for line in map_hex[1:]:  # Bỏ qua dòng đầu tiên
            data = line.strip().split(",")
            list_hex.append(
                {"center": [float(data[0].strip()), float(data[1].strip())],
                    "tile": self.load_tile(data[2].strip())})
        return list_hex

    def load_tile(self, tile_name):
        if tile_name == "grass_tile":
            return TileGrass()
        if tile_name == "snow_tile":
            return TileSnow()
        if tile_name == "sand_tile":
            return TileSand()
        return None

    def draw_match_map(self, window,list_unit,clicked_tile=None):
        """Vẽ bản đồ lục giác trên cửa sổ dựa trên list_hexa."""
        fog_surface = pygame.Surface((config.WINDOW_WIDTH, config.WINDOW_HEIGHT), pygame.SRCALPHA)
        fog_surface.fill((0, 0, 0, 0))
        for hex_data in self.list_hexa:
            hex_center = [float(hex_data["center"][0]), float(hex_data["center"][1])]
            tile = hex_data["tile"]
            # Tạo các điểm cho hình lục giác
            hex_points = self.create_hexagon(hex_center, self.hex_size)
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
            if clicked_tile and hex_center == clicked_tile:
                pygame.draw.polygon(window, (0, 255, 0), hex_points, 1)
            else:
                pygame.draw.polygon(window, (255, 0, 0), hex_points, 1)
            # Kiểm tra xem ô này có phải là ô trong danh sách unit không
            if hex_center not in list_unit and hex_center != clicked_tile: 
            # Vẽ lớp mờ hình lục giác lên fog_surface
                pygame.draw.polygon(fog_surface, (0, 0, 0, 150), hex_points) 
        window.blit(fog_surface, (0, 0))  # Vẽ lớp phủ lên cửa sổ
