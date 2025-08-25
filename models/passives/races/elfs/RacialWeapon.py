from models.passives import Passive
from models.enums import PassiveOrigin, PassiveTime, PassiveTypes

class RacialWeapon(Passive):
    def __init__(self):
        super().__init__(
            "Arma Racial",
            "Os elfos possuem familiaridade com o arqueirismo, o qual consideram uma arte marcial, recebendo um bônus de +1 nos danos causados em seus ataques à distância com os arcos.",
            PassiveTypes.ACTIONS_MODIFIER,
            PassiveOrigin.RACE,
            PassiveTime.PERMANENT
        )
    
    def apply_passive(self, character) -> None:
        pass
