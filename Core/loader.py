import pygame
import sys
import json
from Model.Enviroment.Tile.grass import TileGrass
from Model.Enviroment.Tile.sand import TileSand
from Model.Enviroment.Tile.snow import TileSnow

# Hàm để load và chia nhỏ ảnh thành các frame hoặc load ảnh tĩnh
def load_image_frames(file_path, num_frames=None, frame_width=None, frame_height=None):
    try:
        # Load toàn bộ ảnh
        image = pygame.image.load(file_path).convert_alpha()

        # Nếu num_frames được cung cấp, tức là chúng ta đang làm việc với một spritesheet
        if num_frames is not None and frame_width is not None and frame_height is not None:
            frames = []
            for i in range(num_frames):
                frame_x = i * frame_width  # Tính vị trí x của mỗi frame
                frame = image.subsurface((frame_x, 0, frame_width, frame_height))
                frames.append(frame)
            return frames
        else:
            # Nếu không có spritesheet, trả về ảnh tĩnh
            return [image]

    except pygame.error as e:
        print(f"Không thể load hình ảnh: {e}")
        sys.exit()


def load_hex_data_from_json(file_path):
    list_hex = []
    
    # Mở và load dữ liệu từ file JSON
    with open(file_path, 'r') as f:
        map_hex = json.load(f)
    
    # Duyệt qua các phần tử trong JSON
    for item in map_hex.values():
        for hex_data in item:
            # Thêm vào danh sách với cấu trúc mong muốn
            list_hex.append({
                "center": [float(hex_data["position"]["x"]), float(hex_data["position"]["y"])],
                "tile": load_tile(hex_data["tile"])
            })
    return list_hex

def load_hex_data_from_config(file_path):
    list_hex = []
    lines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Đọc tất cả các dòng
    for line in lines[1:]:  # Bỏ qua dòng đầu tiên
        data = line.strip().split(",")
        list_hex.append([float(data[0].strip()), float(data[1].strip())])
    return list_hex

def load_tile(tile_name):
    if tile_name == "grass_tile":
        return TileGrass()
    if tile_name == "snow_tile":
        return TileSnow()
    if tile_name == "sand_tile":
        return TileSand()
    return None


