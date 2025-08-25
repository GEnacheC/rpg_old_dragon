from interfaces.race_interface import RaceStrategy
from models.enums import Alignment, Darkvision
from models.passives.races.halflings.Stealthy import Stealthy
from models.passives.races.halflings.Fearless import Fearless
from models.passives.races.halflings.GoodAim import GoodAim
from models.passives.races.halflings.Small import Small
from models.passives.races.halflings.Restrictions import Restrictions
from typing import List

class Halfling(RaceStrategy):

    @property
    def name(self) -> str:
        return "Halfling"
    
    @property
    def description(self) -> str:
        return "Halflings são pessoas pequenas e alegres que amam conforto e segurança. " \
               "São conhecidos por sua sorte, furtividade e resistência ao medo."
    
    @property
    def movement(self) -> int:
        return 7
    
    @property
    def darkvision(self) -> Darkvision:
        return Darkvision.NONE
    
    @property
    def alignment(self) -> Alignment:
        return Alignment.NEUTRAL
    
    def get_size(self) -> str:
        return "Muito Pequeno"
    
    def get_race_passives(self) -> List:
        return [
            Stealthy(),
            Fearless(),
            GoodAim(),
            Small(),
            Restrictions()
        ]
