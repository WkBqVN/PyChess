# file use to load all resource to run game at begining
import pygame
import sys

# Load hình ảnh
def load_image(file_path):
    try:
        image = pygame.image.load(file_path)
        return image.convert_alpha()  # Sử dụng convert_alpha() để giữ lại độ trong suốt
    except pygame.error as e:
        print(f"Không thể load hình ảnh: {e}")
        sys.exit()