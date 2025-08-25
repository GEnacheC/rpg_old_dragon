from models.passives import Passive
from models.enums import PassiveOrigin, PassiveTime, PassiveTypes

class Vigorous(Passive):
    def __init__(self):
        super().__init__(
            "Vigoroso",
            "Os anões são muito resistentes aos efeitos que afetem seu corpo, recebendo um bônus de +1 em qualquer teste de JPC (Jogada de Proteção contra Constituição).",
            PassiveTypes.DEFENSE_MODIFIER,
            PassiveOrigin.RACE,
            PassiveTime.PERMANENT
        )
    
    def apply_passive(self, character) -> None:
        pass
