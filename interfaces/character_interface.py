from abc import ABC, abstractmethod
from interfaces.race_interface import RaceStrategy
from interfaces.class_interface import ClassStrategy
from models.character import Character

class CreateCharacterInterface(ABC):
    @abstractmethod
    def create(self, name: str, race: RaceStrategy, character_class: ClassStrategy) -> Character:
        pass
    
    @abstractmethod
    def roll_attributes(self, character: Character) -> Character:
        pass
