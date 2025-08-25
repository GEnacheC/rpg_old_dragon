from models.passives import Passive
from models.enums import PassiveOrigin, PassiveTime, PassiveTypes

class Restrictions(Passive):
    def __init__(self):
        super().__init__(
            "Restrições",
            "Por não terem tradição na forja de armaduras, os halflings usam apenas armaduras de couro, a não ser quando confeccionada especialmente para ele. Um halfling não pode usar armas grandes, sendo restrito apenas a armas pequenas ou médias. Um halfling só consegue usar uma arma média como se fosse uma arma de duas mãos.",
            PassiveTypes.ACTIONS_MODIFIER,
            PassiveOrigin.RACE,
            PassiveTime.PERMANENT
        )
    
    def apply_passive(self, character) -> None:
        pass
