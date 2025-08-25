from interfaces.race_interface import RaceStrategy
from models.enums import Alignment, Darkvision
from models.passives.races.dwarfs.Miners import Miners
from models.passives.races.dwarfs.Vigorous import Vigorous
from models.passives.races.dwarfs.LargeWeapons import LargeWeapons
from models.passives.races.dwarfs.Enemies import Enemies
from typing import List

class Dwarf(RaceStrategy):

    @property
    def name(self) -> str:
        return "Anão"
    
    @property
    def description(self) -> str:
        return "Anões são seres robustos e resistentes, conhecidos por sua habilidade " \
               "em metalurgia, mineração e construção."
    
    @property
    def movement(self) -> int:
        return 6
    
    @property
    def darkvision(self) -> Darkvision:
        return Darkvision.GOOD
    
    @property
    def alignment(self) -> Alignment:
        return Alignment.ORDEM
    
    def get_size(self) -> str:
        return "Pequeno"
    
    def get_race_passives(self) -> List:
        return [
            Miners(),
            Vigorous(),
            LargeWeapons(),
            Enemies()
        ]
