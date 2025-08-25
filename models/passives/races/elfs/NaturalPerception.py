from models.passives import Passive
from models.enums import PassiveOrigin, PassiveTime, PassiveTypes

class NaturalPerception(Passive):
    def __init__(self):
        super().__init__(
            "Percepção Natural",
            "A forma como as casas élficas são construídas, respeitando a forma natural das árvores e abrigos, dá aos elfos uma percepção especial no que diz respeito a portas e passagens não convencionais e até mesmo secretas. Ao passarem até 6 metros de uma porta secreta, mesmo que não a estejam procurando, os elfos podem detectá-la com um resultado 1 em 1d6, ou com um resultado de 1-2 em 1d6 caso estejam efetivamente procurando pela porta secreta.",
            PassiveTypes.ACTIONS_MODIFIER,
            PassiveOrigin.RACE,
            PassiveTime.PERMANENT
        )
    
    def apply_passive(self, character) -> None:
        pass
