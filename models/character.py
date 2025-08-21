from models.player import Player
from models.enums import Attributes

class Character(Player):

    def __init__(self, name):
        super().__init__(name)
        self.ResetAttributes()
    
    #region Attributes Methods
    
    def AddAttributePoints(self, attribute, points):
        if not isinstance(attribute, Attributes):
            raise ValueError("Tributo inválido")

        match attribute:
            case Attributes.STRENGTH:
                self.strength = points
                return
            case Attributes.DEXTERY:
                self.dextery = points
                return
            case Attributes.CONSTITUTION:
                self.constitution = points
                return
            case Attributes.INTELLIGENCE:
                self.intelligence = points
                return
            case Attributes.WISDOM:
                self.wisdom = points
                return
            case Attributes.CHARISMA:
                self.charisma = points
                return
    
    def ResetAttributes(self):
        self.strength = 0
        self.dextery = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0

    #endregion
