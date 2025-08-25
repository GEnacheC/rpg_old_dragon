from models.passives import Passive
from models.enums import PassiveOrigin, PassiveTime, PassiveTypes

class GoodAim(Passive):
    def __init__(self):
        super().__init__(
            "Bons de Mira",
            "Pela tradição racial de jogos de arremesso, para os halflings qualquer ataque à distância com uma arma de arremesso é considerado um ataque fácil.",
            PassiveTypes.ACTIONS_MODIFIER,
            PassiveOrigin.RACE,
            PassiveTime.PERMANENT
        )
    
    def apply_passive(self, character) -> None:
        pass
