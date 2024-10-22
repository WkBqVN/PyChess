
import json
import pygame
from Controller.Element.Character.character_controller import CharacterManager
from Controller.Element.Map import map_controller
from Controller.Element.Match.bottom_panel_controller import BottomPanel
from Controller.Element.Match.right_panel_controller import RightPanel
from Core.util.mouse import get_character_pos
from Model.Unit.Infantry.infantry import Infantry

def start_match():
    return

class Match:
    def __init__(self,data):                                                    #data is unit_list and map list
        self.right_panel = RightPanel()
        self.bottom_panel = BottomPanel()
        self.map_manager= map_controller.MapManager(32,[[0,0],[350,351]])
        self.character_manager = CharacterManager()
        self.data = data
        self.clicked_tiles = [350,350]
        self.test()
        return

    def start_match(self,window):
        self.map_manager.draw_match_map(window, [400,400],self.clicked_tiles)
        self.right_panel.draw_right_panel(window)
        self.character_manager.draw_character(window)
    
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
        # abc = {
        #     "unit": (Infantry("infantry_roman")).to_dict(),
        #     "position" : [300, 300],
        #     "map" : 1
        # }
        # print(json.dumps(abc))
        self.character_manager.add_character(Infantry("infantry_roman", [300, 300]))
        # self.character_manager.add_character(Infantry("infantry_roman", [800, 200]))
    

