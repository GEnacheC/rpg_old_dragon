from abc import ABC, abstractmethod
from typing import List
from models.enums import Classes
from models.passives.Passive import Passive

class ClassStrategy(ABC):
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        pass
    
    @property
    @abstractmethod
    def hit_dice(self) -> int:
        pass
    
    @property
    @abstractmethod
    def base_attack_bonus(self) -> str:
        pass
    
    @property
    @abstractmethod
    def saving_throws(self) -> List[str]:
        pass
    
    @abstractmethod
    def get_class_passives(self) -> List[Passive]:
        pass
    
    @abstractmethod
    def get_proficiencies(self) -> List[str]:
        pass
    
    @abstractmethod
    def get_spellcasting(self) -> dict:
        pass
