from Model.Enviroment.Tile.tile_constant import get_tile_by_name
from Model.Enviroment.Tile.base_tile import Tile

class TileSand(Tile):
    def __init__(self):
        super().__init__(get_tile_by_name("sand_tile")) #hardcore name
        return