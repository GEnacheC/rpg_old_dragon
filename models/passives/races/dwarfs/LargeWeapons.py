from models.passives import Passive
from models.enums import PassiveOrigin, PassiveTime, PassiveTypes

class LargeWeapons(Passive):
    def __init__(self):
        super().__init__(
            "Armas grandes",
            "São restritas para anões que podem usar apenas armas médias e pequenas. Armas grandes forjadas como um item racial anão são consideradas armas médias para um anão.",
            PassiveTypes.ACTIONS_MODIFIER,
            PassiveOrigin.RACE,
            PassiveTime.PERMANENT
        )
    
    def apply_passive(self, character) -> None:
        pass
