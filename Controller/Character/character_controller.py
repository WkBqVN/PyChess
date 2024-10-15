#manager all char

class CharacterManager:
    def __init__(self):
        self.characters = []

    def draw_character(self,window):
        for character in self.characters:
            window.blit(character.update_animation(), character.position)

    def add_character(self, character):
        self.characters.append(character)
