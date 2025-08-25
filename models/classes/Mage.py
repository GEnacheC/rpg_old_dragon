from interfaces.class_interface import ClassStrategy
from models.passives.Passive import Passive
from models.enums import Classes
from typing import List

class Mage(ClassStrategy):
    
    @property
    def name(self) -> str:
        return "Mago"
    
    @property
    def description(self) -> str:
        return "Magos são estudiosos da magia arcana, capazes de lançar feitiços poderosos através de anos de estudo e pesquisa."
    
    @property
    def hit_dice(self) -> int:
        return 6
    
    @property
    def base_attack_bonus(self) -> str:
        return "Fraco"
    
    @property
    def saving_throws(self) -> List[str]:
        return ["JPI", "JPS"]
    
    def get_class_passives(self) -> List[Passive]:
        return []
    
    def get_proficiencies(self) -> List[str]:
        return [
            "Adagas",
            "Bastões",
            "Varinhas",
            "Armaduras de tecido"
        ]
    
    def get_spellcasting(self) -> dict:
        return {
            "type": "Arcana",
            "spellcasting_ability": "Inteligência",
            "spells_known": 6,
            "spell_slots": {
                "1": 2,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0,
                "6": 0,
                "7": 0,
                "8": 0,
                "9": 0
            }
        }
