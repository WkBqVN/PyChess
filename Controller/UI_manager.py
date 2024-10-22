import pygame
from Controller.Element.Map import map_controller
from Core import config

class UIManager:
    def __init__(self):
        self.DashBoard = None
        self.map_controller= map_controller.MapController()
        return

    def draw_match(self,window,match_data,map_name):
        self.map_controller.draw_match_map(window,match_data)
        #draw unit
        for unit in match_data:
                    window.blit(unit.update_animation(), 
                                    [unit.position[0],unit.position[1]])
        #draw map
        for player in match_data.keys():                              # get each player data
            self.draw_units(window,player.player_match_data[player].list_units)
            if map_name == "map_1":
                self.draw_map(window,map_controller.list_map["map"]["map_1"])
            elif map_name == "map_2":
                self.draw_map(window,map_controller.list_map["map"]["map_2"])
            elif map_name == "map_3":
                self.draw_map(window,map_controller.list_map["map"]["map_3"])
            elif map_name == "map_4":
                self.draw_map(window,map_controller.list_map["map"]["map_4"])
            elif map_name == "map_5":
                self.draw_map(window,map_controller.list_map["map"]["map_5"])
