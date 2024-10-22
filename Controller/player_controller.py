class player: 
    def __init__(self,player_name,player_id):
        self.player_name = player_name
        self.player_id = player_id
        self.list_units = {
            "map_unit_1":[],
            "map_unit_2":[],
            "map_unit_3":[],
            "map_unit_4":[]
        }
        return

    def load_player_units(self,units,map):
        for unit in units:
            if map == 1:
                self.list_units["map_unit_1"].append(unit)
            if map == 2:
                self.list_units["map_unit_2"].append(unit)
            if map == 3:
                self.list_units["map_unit_3"].append(unit)
            if map == 4:
                self.list_units["map_unit_4"].append(unit)
