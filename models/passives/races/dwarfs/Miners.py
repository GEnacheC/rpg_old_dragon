from models.passives import Passive
from models.enums import PassiveOrigin, PassiveTime, PassiveTypes

class Miners(Passive):
    def __init__(self):
        super().__init__(
            "Mineradores",
            "Por milênios, anões aprendem desde cedo a avaliar passagens e condições de muralhas e portais. Por isso são capazes de detectar, mesmo que não estejam analisando ativamente, com um resultado de 1 em 1d6, anomalias em pedras, como armadilhas em cavernas ou fossos escondidos, ou com um resultado de 1-2 em 1d6 caso estejam efetivamente procurando.",
            PassiveTypes.ACTIONS_MODIFIER,
            PassiveOrigin.RACE,
            PassiveTime.PERMANENT
        )
    
    def apply_passive(self, character) -> None:
        pass
