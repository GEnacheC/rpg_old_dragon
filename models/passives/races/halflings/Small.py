from models.passives import Passive
from models.enums import PassiveOrigin, PassiveTime, PassiveTypes

class Small(Passive):
    def __init__(self):
        super().__init__(
            "Pequenos",
            "Devido à baixa estatura e agilidade, todos os ataques provenientes de criaturas grandes ou maiores são considerados ataques difíceis para acertar um halfling.",
            PassiveTypes.DEFENSE_MODIFIER,
            PassiveOrigin.RACE,
            PassiveTime.PERMANENT
        )
    
    def apply_passive(self, character) -> None:
        pass
