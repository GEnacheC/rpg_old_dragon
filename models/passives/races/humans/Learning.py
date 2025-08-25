


from typing import override
from models.passives import Passive
from models.enums import PassiveOrigin, PassiveTime, PassiveTypes


class Learning(Passive):
    def __init__(self):
        super().__init__(
            "Aprendizado",
            "Humanos aprendem tudo o que se propõem a fazer de forma muito mais rápida que as outras raças. Com isso, um humano recebe um bônus de 10% sobre toda experiência (XP) recebida.",
            PassiveTypes.ATTRIBUTES_MODIFIER,
            PassiveOrigin.RACE,
            PassiveTime.PERMANENT
        )
    
    @override
    def apply_passive(self, character):
        pass