import configparser

_config = configparser.ConfigParser()

#window config
_config.read(".\\Config\\Pychess.conf")

WINDOW_WIDTH = _config.getint("Window","window_width")
WINDOW_HEIGHT = _config.getint("Window","window_height")


#map config
_config.read(".\\Config\\Map.conf")

CELL_SIZE = _config.getint("map","cell_size")

