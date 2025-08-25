from interfaces.class_interface import ClassStrategy
from models.passives.Passive import Passive
from models.enums import Classes
from typing import List

class Thief(ClassStrategy):
    
    @property
    def name(self) -> str:
        return "Ladrão"
    
    @property
    def description(self) -> str:
        return "Ladrões são especialistas em furtividade, destreza e habilidades sociais, capazes de se infiltrar em locais inacessíveis e obter informações valiosas."
    
    @property
    def hit_dice(self) -> int:
        return 8
    
    @property
    def base_attack_bonus(self) -> str:
        return "Médio"
    
    @property
    def saving_throws(self) -> List[str]:
        return ["JPD", "JPS"]
    
    def get_class_passives(self) -> List[Passive]:
        return []
    
    def get_proficiencies(self) -> List[str]:
        return [
            "Armas simples",
            "Espadas curtas",
            "Arcos curtos",
            "Armaduras leves"
        ]
    
    def get_spellcasting(self) -> dict:
        return {
            "type": "Nenhum",
            "spellcasting_ability": None,
            "spells_known": 0,
            "spell_slots": {}
        }
