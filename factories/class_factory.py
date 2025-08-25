from models.classes.Warrior import Warrior
from models.classes.Mage import Mage
from models.classes.Thief import Thief
from interfaces.class_interface import ClassStrategy
from models.enums import Classes

class ClassFactory:
    
    @staticmethod
    def get_class(class_type: Classes) -> ClassStrategy:
        match class_type:
            case Classes.WARRIOR:
                return Warrior()
            case Classes.MAGE:
                return Mage()
            case Classes.THIEF:
                return Thief()
            case _:
                raise ValueError(f"Class '{class_type}' not found")
    
    @staticmethod
    def create_class(class_type: Classes) -> ClassStrategy:
        return ClassFactory.get_class(class_type)
    
    @staticmethod
    def get_available_classes() -> list[str]:
        return [class_type.value for class_type in Classes]
    
    @staticmethod
    def get_available_classes_enum() -> list[Classes]:
        return list(Classes)
    
    @staticmethod
    def is_valid_class(class_type: Classes) -> bool:
        return class_type in Classes
    
    @staticmethod
    def get_class_info(class_type: Classes) -> dict:
        class_instance = ClassFactory.create_class(class_type)
        return {
            "name": class_instance.name,
            "description": class_instance.description,
            "hit_dice": class_instance.hit_dice,
            "base_attack_bonus": class_instance.base_attack_bonus,
            "saving_throws": class_instance.saving_throws,
            "proficiencies": class_instance.get_proficiencies(),
            "spellcasting": class_instance.get_spellcasting(),
            "passives": [passive.name for passive in class_instance.get_class_passives()]
        }
    
    @staticmethod
    def get_all_classes_info() -> list[dict]:
        return [ClassFactory.get_class_info(class_type) for class_type in Classes]
