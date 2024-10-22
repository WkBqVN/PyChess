grass_tile = {
    "asset":{
        "asset_normal": {
            "path": "Asset\\Terrain\\hex_tiles\\Blank-Cover\\Blank-Grass.png",
            "num_of_frames": 1,
            "width":100,
            "height":100
        },
    },
    "moveable": True
}

sand_tile = {
    "asset":{
            "asset_normal": {
                "path": "Asset\\Terrain\\hex_tiles\\Blank-Cover\\Blank-Sand.png",
                "num_of_frames": 1,
                "width":100,
                "height":100
            },
        },
    "moveable": True
}

snow_tile = {
    "asset":{
            "asset_normal": {
                "path": "Asset\\Terrain\\hex_tiles\\Blank-Cover\\Blank-Snow.png",
                "num_of_frames": 1,
                "width":100,
                "height":100
            },
        },
    "moveable": True
}

def get_tile_by_name(tile_name):
    if tile_name == "grass_tile":
        return grass_tile
    if tile_name == "sand_tile":
        return sand_tile
    if tile_name == "snow_tile":
        return snow_tile
    return grass_tile