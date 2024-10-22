import configparser

_config = configparser.ConfigParser()

#window config
_config.read(".\\Config\\Pychess.conf")

SCREEN_MODE = _config.get("screen_mode","resolution")
HEX_GENERATED_PATHS = _config.get("Paths","hex_generated")
WINDOW_WIDTH = _config.getint("Window","window_width")
WINDOW_HEIGHT = _config.getint("Window","window_height")

#map config
_config.read(".\\Config\\Map.conf")
CELL_SIZE = _config.getint("map","cell_size")

#files config
