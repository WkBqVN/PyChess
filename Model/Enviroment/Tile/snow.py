from Model.Enviroment.Tile.tile_constant import get_tile_by_name
from Model.Enviroment.Tile.base_tile import Tile

class TileSnow(Tile):
    def __init__(self):
        super().__init__(get_tile_by_name("snow_tile")) #hardcore name
        return