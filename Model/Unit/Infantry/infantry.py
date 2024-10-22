# infantry base class 
from Model import base_unit
from Model.Unit.Infantry.infantry_constant import get_infantry_by_name

class Infantry(base_unit.Unit):
    def __init__(self,infantry_name,position):
        infantry_data = get_infantry_by_name(infantry_name)
        super().__init__(infantry_data,position)
        # log
        self.unit_name = infantry_name
        return

    def get_image():
        return
    
    def get_info(self):
        super().get_info(self.unit_name)