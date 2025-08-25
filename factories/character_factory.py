from interfaces.race_interface import RaceStrategy
from interfaces.class_interface import ClassStrategy
from models.enums import AdventureTypes
from interfaces.character_interface import CreateCharacterInterface
from factories.adventure_factories import ClassicFactory, AdventurerFactory, HeroicFactory

class CreateCharacterFactory:
    
    @staticmethod
    def get_factory(adventure_type: AdventureTypes) -> CreateCharacterInterface:
        match adventure_type:
            case AdventureTypes.CLASSIC:
                return ClassicFactory()
            case AdventureTypes.ADVENTURER:
                return AdventurerFactory()
            case AdventureTypes.HEROIC:
                return HeroicFactory()
            case _:
                raise ValueError("Invalid adventure type")
    
    @staticmethod
    def create_character(adventure_type: AdventureTypes, name: str, race: RaceStrategy, character_class: ClassStrategy):
        factory = CreateCharacterFactory.get_factory(adventure_type)
        character = factory.create(name, race, character_class)
        for passive in race.get_race_passives():
            character.add_passive(passive)
        for passive in character_class.get_class_passives():
            character.add_passive(passive)
        return factory.roll_attributes(character)
