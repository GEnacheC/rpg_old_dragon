from interfaces.race_interface import RaceStrategy
from models.enums import Alignment, Darkvision
from models.passives.races.humans.Learning import Learning
from models.passives.races.humans.Adaptability import Adaptability
from typing import List

class Human(RaceStrategy):

    @property
    def name(self) -> str:
        return "Humano"
    
    @property
    def description(self) -> str:
            return "Com enorme variabilidade cultural e " \
            "disseminados por todos os cantos do " \
            "mundo, os humanos possuem muita " \
            "facilidade em assumir o lugar central na maioria " \
            "dos cenários e, quando analisados sob essa ótica, " \
            "revelam sua verdadeira força."
    
    @property
    def movement(self) -> int:
        return 9
    
    @property
    def darkvision(self) -> Darkvision:
        return Darkvision.NONE
    
    @property
    def alignment(self) -> Alignment:
        return Alignment.ANY
    
    
    def get_size(self) -> str:
        return "Médio"
    
    def get_race_passives(self) -> List:
        return [
            Learning(),
            Adaptability()
        ]
