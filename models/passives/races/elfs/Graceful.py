from models.passives import Passive
from models.enums import PassiveOrigin, PassiveTime, PassiveTypes

class Graceful(Passive):
    def __init__(self):
        super().__init__(
            "Graciosos",
            "Os elfos controlam com precisão seus movimentos no espaço ao redor do seu corpo, recebendo um bônus de +1 em qualquer teste de JPD (Jogada de Proteção contra Destreza).",
            PassiveTypes.DEFENSE_MODIFIER,
            PassiveOrigin.RACE,
            PassiveTime.PERMANENT
        )
    
    def apply_passive(self, character) -> None:
        pass

