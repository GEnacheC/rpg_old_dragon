from interfaces.race_interface import RaceStrategy
from models.enums import Alignment, Darkvision
from models.passives.races.elfs.NaturalPerception import NaturalPerception
from models.passives.races.elfs.Graceful import Graceful
from models.passives.races.elfs.RacialWeapon import RacialWeapon
from models.passives.races.elfs.Immunities import Immunities
from typing import List

class Elf(RaceStrategy):

    @property
    def name(self) -> str:
        return "Elfo"
    
    @property
    def description(self) -> str:
        return "Elfos são seres graciosos e longevos, conhecidos por sua beleza, " \
               "agilidade e conexão com a magia e a natureza."
    
    @property
    def movement(self) -> int:
        return 9
    
    @property
    def darkvision(self) -> Darkvision:
        return Darkvision.GOOD
    
    @property
    def alignment(self) -> Alignment:
        return Alignment.NEUTRAL
    
    def get_size(self) -> str:
        return "Médio"
    
    def get_race_passives(self) -> List:
        return [
            NaturalPerception(),
            Graceful(),
            RacialWeapon(),
            Immunities()
        ]
