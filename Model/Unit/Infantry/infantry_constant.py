#list of infantry base on type

infantry_roman = {
    "attribute":{
        "hp": 10,
        "movement_speed": 2,
        "armor" : 1,
        "attack_range" : 1,
        "damage": 20 ,
        "view_sight":2,
    },
    "asset":{
        "asset_attack": {
            "path": ".\\Asset\\Unit\\infantry_roman\\infantry_roman_attack_01.png",
            "num_of_frames": 6,
            "width":100,
            "height":100
        },
        "asset_movement":{
            "path": ".\\Asset\\Unit\\infantry_roman\\infantry_roman_movement.png",
            "num_of_frames": 8,
            "width":100,
            "height":100
        },
        "asset_hold":{
            "path": ".\\Asset\\Unit\\infantry_roman\\infantry_roman_hold.png",
            "num_of_frames": 4,
            "width":100,
            "height":100
        },
        "asset_death":{
            "path": ".\\Asset\\Unit\\infantry_roman\\infantry_roman_death.png",
            "num_of_frames": 4,
            "width":100,
            "height":100
        },
        "asset_idle":{
            "path": ".\\Asset\\Unit\\infantry_roman\\infantry_roman_idle.png",
            "num_of_frames": 6,
            "width":100,
            "height":100
        }
    }
}

infantry_chinese = {
    "attribute":{
        "hp": 8,
        "movement_speed": 2,
        "armor" : 0,
        "attack_range": 1,
        "damage": 10 ,
        "view_sight":2,
    },
    "asset":{
            "asset_attack": {
                    "path":"C:\\Work\\PyChess\\Asset\\Unit\\infantry_roman\\infantry_roman_attack_01.png",
                    "num_of_frames": 6,
                    "width":100,
                    "height":100
                },
            "asset_path_movement":"",
            "asset_path_hold":"",
            "asset_path_die":"",
            "asset_path_idle":""
        }
}

infantry_basic = {
    "hp": 1,
    "movement_speed": 1,
    "armor" : 1,
    "attack_range" : 1,
    "damage": 1 ,
    "view_sight":2
}

def get_infantry_by_name(infantry_name):
    if infantry_name == "infantry_roman":
        return infantry_roman
    if infantry_name == "infantry_chinese":
        return infantry_chinese
    return infantry_basic