from abc import ABC, abstractmethod
from models.character import Character

class CreateCharacterInterface(ABC):
    @abstractmethod
    def Create(self, name: str) -> Character:
        pass
    
    @abstractmethod
    def RollAttributes(self, character: Character) -> Character:
        pass
