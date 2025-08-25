from models.passives import Passive
from models.enums import PassiveOrigin, PassiveTime, PassiveTypes

class Stealthy(Passive):
    def __init__(self):
        super().__init__(
            "Furtivos",
            "São especialistas em se esconder e em passar despercebidos, conseguindo se esconder com uma chance de 1-2 em 1d6. Se o halfling adotar a classe Ladrão, ele acrescenta ainda um bônus de 1 no seu talento Furtividade.",
            PassiveTypes.ACTIONS_MODIFIER,
            PassiveOrigin.RACE,
            PassiveTime.PERMANENT
        )
    
    def apply_passive(self, character) -> None:
        pass
