import pygame
import math

class MapManager:
    def __init__(self):
        return
    
    def create_hexagon(self,center, size):
        """ Tạo một hình lục giác với bán kính `size` tại vị trí `center`. """
        points = []
        for i in range(6):  # 6 cạnh của lục giác
            angle = math.radians(60 * i)  # Góc giữa các đỉnh
            x = center[0] + size * math.cos(angle)
            y = center[1] + size * math.sin(angle)
            points.append((x, y))
        return points # có tổng cộng 6 points
    
    def hex_to_pixel(self,row, col, hex_size):
        """ Tính toán vị trí pixel cho lục giác tại hàng và cột trong lưới. """
        x_offset = hex_size * 3 / 2 * col
        y_offset = hex_size * math.sqrt(3) * (row + 0.5 * (col % 2))
        return (x_offset, y_offset)

    def draw_map(self,window, map_data, tiles, clicked_tiles):
        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                if tile in tiles:
                    # Tính toán vị trí pixel cho ô lục giác
                    hex_center = self.hex_to_pixel(y, x, 10)
                    hex_points = self.create_hexagon(hex_center, 10)
                    window.blit(tiles[tile], hex_center)  # Vẽ hình ảnh lục giác

                # Vẽ hình chữ nhật xung quanh ô được click
                if clicked_tiles and x == clicked_tiles[0] and y == clicked_tiles[1]:
                    pygame.draw.polygon(window, (0, 255, 0), self.create_hexagon(hex_center, 10), 3)