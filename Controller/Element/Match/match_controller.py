
import json
import pygame
from Controller.Element.Map import map_controller
from Controller.Element.Map.map_match import MatchMap
from Controller.Element.Match.bottom_panel_controller import BottomPanel
from Controller.Element.Match.right_panel_controller import RightPanel
from Controller.player_controller import player
from Core.util.mouse import get_character_pos
from Model.Unit.Infantry.infantry import Infantry

class MatchController:
    def __init__(self,player_data, map_data):                                                    
        self.right_panel = RightPanel()
        self.bottom_panel = BottomPanel()

        self.map_data = {
            "map_data":MatchMap(map_data),
            "clicked_tiles":[350,350]
        }
        self.match = {
            "data": {
                "map_data": map_data,
                "player_data": player_data
            }
        }

        self.test()
        return

    def start_match(self,window):
        self.right_panel.draw_right_panel(window)

    def get_match(self):
        return self.match

    def handleEvent(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:  # Left click
                if mouse_pos[0] < 1600 and mouse_pos[1] < 900:                  #
                    # clicked_hex = get_character_pos(mouse_pos)
                    self.clicked_tiles = self.map_manager.find_clicked_hexagon(mouse_pos)["center"]
                elif 1600 < mouse_pos[0] < 1920 and 900 < mouse_pos[1] < 1080:
                    print("clicked left panel")
                else:
                    print("clicked card panel")
            elif event.button == 3:  # Right click
                # character_manager.characters[0].hold()
                print("right")
    
    #test
    def test(self):
        player1 = player("khoavo", 1)
        list_unit = [Infantry("infantry_roman", [200, 200]),Infantry("infantry_roman", [300, 300])]
        
        player1.load_player_units(list_unit,1,)

        player2 = player("2",2)
        list_unit = [Infantry("infantry_roman", [700, 700]),]
        player2.load_player_units(list_unit,1,)
        self.match["data"]["map_data"] = {
            "map_1" : {},
            "map_2" : {},
            "map_3" : {},
            "map_4" : {}
        }
        self.match["data"]["player_data"] = {
            "player1": player1,
            "player2": player2
        }
