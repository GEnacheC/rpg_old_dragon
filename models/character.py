from typing import List
from interfaces.race_interface import RaceStrategy
from models.passives.Passive import Passive
from models.player import Player
from models.enums import Attributes

class Character(Player):

    def __init__(self, name, race: RaceStrategy):
        super().__init__(name)
        self.race = race
        self.passive_abilities = []
        self.reset_attributes()
    
    #region Attributes Methods
    
    def add_attribute_points(self, attribute, points):
        if not isinstance(attribute, Attributes):
            raise ValueError("Invalid attribute")

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
    
    def reset_attributes(self):
        self.strength = 0
        self.dextery = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0

    def add_passive(self, passive: Passive):
        self.passive_abilities.append(passive)

    def get_all_passives(self) -> List[str]:
        return [str(passive) for passive in self.passive_abilities]
    
    def has_passive(self, passive_name: str) -> bool:
        return any(passive.name.lower() == passive_name.lower() for passive in self.passive_abilities)

    #endregion
