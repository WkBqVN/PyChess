import pygame
from Core import loader

# parent class
class Unit: 
    def __init__(self, unit_data, position):
        self.load_attributes(unit_data["attribute"])
        self.load_images(unit_data["asset"])
        self.init_status()
        self.init_animation()
        self.position = position

    def load_attributes(self, attribute):
        self.hp = attribute["hp"]
        self.movement_speed = attribute["movement_speed"]
        self.attack_range = attribute["attack_range"]
        self.damage = attribute["damage"]
        self.armor = attribute["armor"]
        self.view_sight = attribute["view_sight"]

    def load_images(self, asset):
        # Dictionary chứa các trạng thái và các hoạt ảnh tương ứng
        self.frames_dict = {
            "is_hold": loader.load_image_frames(asset["asset_hold"]["path"], 
                                                asset["asset_hold"]["num_of_frames"], 
                                                asset["asset_hold"]["width"], 
                                                asset["asset_hold"]["height"]),
            "is_death": loader.load_image_frames(asset["asset_death"]["path"], 
                                                asset["asset_death"]["num_of_frames"], 
                                                asset["asset_death"]["width"], 
                                                asset["asset_death"]["height"]),
            "is_attacking": loader.load_image_frames(asset["asset_attack"]["path"], 
                                                asset["asset_attack"]["num_of_frames"], 
                                                asset["asset_attack"]["width"], 
                                                asset["asset_attack"]["height"]),
            "is_idle": loader.load_image_frames(asset["asset_idle"]["path"], 
                                                asset["asset_idle"]["num_of_frames"], 
                                                asset["asset_idle"]["width"], 
                                                asset["asset_idle"]["height"]),
            "is_moving": loader.load_image_frames(asset["asset_movement"]["path"], 
                                                asset["asset_movement"]["num_of_frames"], 
                                                asset["asset_movement"]["width"], 
                                                asset["asset_movement"]["height"])
        }

    def init_status(self):
        self.is_attacking = False
        self.is_idle = True  # Đặt trạng thái mặc định là idle
        self.is_death = False
        self.is_hold = False
        self.is_moving = False

    def init_animation(self):
        self.current_frame = 0
        self.frame_time = 300  # Thời gian giữa mỗi khung hình (300ms)
        self.last_update = pygame.time.get_ticks()

    def update_animation(self):
        """Cập nhật hoạt ảnh dựa trên trạng thái hiện tại"""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.frame_time:
            self.current_frame += 1
            self.last_update = current_time

        # Đảm bảo vòng lặp hoạt ảnh, không vượt quá số khung hình có sẵn
        for state, frames in self.frames_dict.items():
            if getattr(self, state):
                if self.current_frame >= len(frames):  
                    if state == "is_death":
                        self.current_frame = len(frames) - 1  # Dừng ở khung hình cuối
                    else:
                        self.current_frame = 0  # Reset hoạt ảnh về ban đầu
                        if state != "is_death":
                            self.is_idle = True
                            self.is_attacking = False
                            self.is_moving = False
                            self.is_hold = False
                return frames[self.current_frame]
        return None  # Không có trạng thái hoạt động

    def move(self):
        self.is_moving = True
        self.is_idle = False  # Vô hiệu trạng thái idle
        print(f"Unit moved with speed {self.movement_speed}")

    def attack(self):
        self.is_attacking = True
        self.is_idle = False  # Vô hiệu trạng thái idle
        print(f"Unit attacked with damage {self.damage}")

    def hold(self):
        self.is_hold = True
        self.is_idle = False  # Vô hiệu trạng thái idle
        print(f"Unit holding")

    def death(self):
        self.is_death = True
        self.is_idle = False  # Vô hiệu trạng thái idle
        self.is_attacking = False  # Ngừng các hành động khác
        self.is_moving = False
        self.is_hold = False
        print(f"Unit death")

    def get_info(self, unit_name):
        print(f"Loaded Unit: {unit_name}")
        print(f"HP: {self.hp}, Movement Speed: {self.movement_speed}")
        print(f"Attack Range: {self.attack_range}, Damage: {self.damage}")
        print(f"Armor: {self.armor}, View Sight: {self.view_sight}")
        self.print_image_status(unit_name)

    def print_image_status(self, unit_name):
        for state, frames in self.frames_dict.items():
            action = state.replace("is_", "").capitalize()  # Định dạng lại tên hành động
            if frames is not None:
                print(f"{unit_name} {action} image loaded")
            else:
                print(f"Can't load {action} image")
