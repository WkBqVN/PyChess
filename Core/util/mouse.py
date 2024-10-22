import math
import Core.config as config
def pixel_to_axial(x, y, size, origin):
    # Chuyển đổi từ pixel (x, y) sang tọa độ Axial (q, r)
    q = (math.sqrt(3) / 3 * (x - origin[0]) - 1/3 * (y - origin[1])) / size
    r = (2 / 3 * (y - origin[1])) / size
    return q, r

def axial_to_cube(q, r):
    # Chuyển từ Axial sang Cube
    x = q
    z = r
    y = -x - z
    return x, y, z

def cube_round(x, y, z):
    # Làm tròn tọa độ Cube
    rx = round(x)
    ry = round(y)
    rz = round(z)

    x_diff = abs(rx - x)
    y_diff = abs(ry - y)
    z_diff = abs(rz - z)

    if x_diff > y_diff and x_diff > z_diff:
        rx = -ry - rz
    elif y_diff > z_diff:
        ry = -rx - rz
    else:
        rz = -rx - ry

    return rx, ry, rz

def get_character_pos(pos, origin=(0,0)):
    """
    Hàm này nhận tọa độ pixel 'pos' của chuột (hoặc character) và trả về tọa độ lục giác tương ứng.
    
    - pos: Tọa độ (x, y) của chuột click hoặc nhân vật.
    - size: Kích thước của lục giác (bán kính của lục giác).
    - origin: Tọa độ gốc của bản đồ lục giác (tọa độ pixel của lục giác đầu tiên).
    """
    x, y = pos  # Tọa độ chuột click
    q, r = pixel_to_axial(x, y, config.CELL_SIZE , origin)  # Chuyển sang Axial tọa độ
    cube_x, cube_y, cube_z = axial_to_cube(q, r)  # Chuyển Axial sang Cube
    rounded_cube = cube_round(cube_x, cube_y, cube_z)  # Làm tròn tọa độ Cube để tìm lục giác gần nhất
    
    return rounded_cube
