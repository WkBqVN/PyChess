import Core.config as config

def get_character_pos(pos):
    return ((2*(pos[0]//config.CELL_SIZE)+1)*config.CELL_SIZE/2
,(2*(pos[0]//config.CELL_SIZE)+1)*config.CELL_SIZE/2) # 100 x 100 per square