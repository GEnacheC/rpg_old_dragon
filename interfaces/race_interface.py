from abc import ABC, abstractmethod
from typing import List
from models.passives.Passive import Passive
from models.enums import Alignment, Darkvision

class RaceStrategy(ABC):

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
    def movement(self) -> int:
        pass
    
    @property
    @abstractmethod
    def darkvision(self) -> Darkvision:
        pass
    
    @property
    @abstractmethod
    def alignment(self) -> Alignment:
        pass
    
    @abstractmethod
    def get_size(self) -> str:
        pass
    
    @abstractmethod
    def get_race_passives(self) -> List[Passive]:
        pass
    
