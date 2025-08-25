


from typing import override
from models.passives import Passive
from models.enums import PassiveOrigin, PassiveTime, PassiveTypes


class Adaptability(Passive):
    def __init__(self):
        super().__init__(
            "Adaptabilidade",
            "Humanos são muito adaptáveis e diversos entre si, fazendo com que possam escolher onde alocar um bônus nas suas Jogadas de Proteção. Humanos recebem um bônus de +1 em uma única Jogada de Proteção à sua escolha.",
            PassiveTypes.ACTIONS_MODIFIER,
            PassiveOrigin.RACE,
            PassiveTime.PERMANENT
        )
    
    @override
    def apply_passive(self, character):
        pass