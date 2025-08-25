from models.passives import Passive
from models.enums import PassiveOrigin, PassiveTime, PassiveTypes

class Enemies(Passive):
    def __init__(self):
        super().__init__(
            "Inimigos",
            "Anões são inimigos naturais e disputam território com orcs, ogros e hobgoblins e, por isso, os ataques dos anões contra essas criaturas são considerados ataques fáceis.",
            PassiveTypes.ACTIONS_MODIFIER,
            PassiveOrigin.RACE,
            PassiveTime.PERMANENT
        )
    
    def apply_passive(self, character) -> None:
        pass
