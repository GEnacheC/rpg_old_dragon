from interfaces.class_interface import ClassStrategy
from models.passives.Passive import Passive
from models.enums import Classes
from typing import List

class Warrior(ClassStrategy):
    
    @property
    def name(self) -> str:
        return "Guerreiro"
    
    @property
    def description(self) -> str:
        return "Guerreiros são especialistas em combate corpo a corpo, usando armas e armaduras pesadas para proteger seus aliados e derrotar inimigos."
    
    @property
    def hit_dice(self) -> int:
        return 10
    
    @property
    def base_attack_bonus(self) -> str:
        return "Bom"
    
    @property
    def saving_throws(self) -> List[str]:
        return ["JPC", "JPS"]
    
    def get_class_passives(self) -> List[Passive]:
        return []
    
    def get_proficiencies(self) -> List[str]:
        return [
            "Todas as armas simples",
            "Todas as armas marciais",
            "Todas as armaduras",
            "Escudos"
        ]
    
    def get_spellcasting(self) -> dict:
        return {
            "type": "Nenhum",
            "spellcasting_ability": None,
            "spells_known": 0,
            "spell_slots": {}
        }
