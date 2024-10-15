import pygame
import sys

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