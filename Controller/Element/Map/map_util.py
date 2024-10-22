import Core.config as config
import random
import math

def random_tile_type():
    return random.choice(["grass_tile", "snow_tile", "sand_tile"])

def generate_centers(width, height, size):
    """ Tạo một danh sách chứa các tâm lục giác đều trong hình chữ nhật và ghi vào file config. """
    centers = []  # Bắt đầu với danh sách trống

    # Tính toán khoảng cách giữa các tâm lục giác
    hex_width = 1.57 * size  # Chiều ngang giữa các tâm lục giác
    hex_height = 1.7 * size  # Chiều dọc giữa các hàng lục giác

    count = 0
    for x in range(0, width, int(hex_width)):  # Khoảng cách giữa các cột là hex_width
        start = 0
        if count % 2 == 1:
            start += hex_height / 2  # Dịch các hàng lẻ xuống nửa chiều cao của lục giác

        for y in range(int(start), height, int(hex_height)):
            centers.append([x, y])
        count += 1

    try:
        print("Writing map to Config file")
        with open(config.HEX_GENERATED_PATHS, 'w') as f:
            f.write('[1280x800]\n')
            for center in centers:
                f.write(f'{center[0]},{center[1]},{random_tile_type()}\n')
        print("Centers successfully written to file.")
    except Exception as e:
        print(f"Error writing centers to file: {e}")
    
    return centers
