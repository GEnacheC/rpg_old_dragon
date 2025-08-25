from models.passives import Passive
from models.enums import PassiveOrigin, PassiveTime, PassiveTypes

class Immunities(Passive):
    def __init__(self):
        super().__init__(
            "Imunidades",
            "Os elfos são imunes a efeitos ou magias que envolvam sono e também contra a paralisia causada por um Ghoul.",
            PassiveTypes.DEFENSE_MODIFIER,
            PassiveOrigin.RACE,
            PassiveTime.PERMANENT
        )
    
    def apply_passive(self, character) -> None:
        pass
