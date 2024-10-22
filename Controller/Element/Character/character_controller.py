#manager all char

class CharacterManager:
    def __init__(self):
        self.characters = []

    def draw_character(self,window):
        for character in self.characters:
            window.blit(character.update_animation(), 
                        [character.position[0],character.position[1]])

    def add_character(self, character):
        self.characters.append(character)
