from models.passives import Passive
from models.enums import PassiveOrigin, PassiveTime, PassiveTypes

class Fearless(Passive):
    def __init__(self):
        super().__init__(
            "Destemidos",
            "Os halflings são muito resistentes a efeitos que afetem sua força de vontade, recebendo um bônus de +1 em qualquer teste de JPS (Jogada de Proteção contra Sabedoria).",
            PassiveTypes.DEFENSE_MODIFIER,
            PassiveOrigin.RACE,
            PassiveTime.PERMANENT
        )
    
    def apply_passive(self, character) -> None:
        pass
