from factories.character_interface import CreateCharacterInterface
from models.enums import TiposDeAventura
from factories.adventure_factories import (
    ClassicoCharacterFactory, 
    AventureiroCharacterFactory, 
    HeroicoCharacterFactory
)

class CreateCharacterFactory:
    @staticmethod
    def GetFactory(tipo_aventura: TiposDeAventura) -> CreateCharacterInterface:
        match tipo_aventura:
            case TiposDeAventura.CLASSICO:
                return ClassicoCharacterFactory()
            case TiposDeAventura.AVENTUREIRO:
                return AventureiroCharacterFactory()
            case TiposDeAventura.HEROICO:
                return HeroicoCharacterFactory()
            case _:
                raise ValueError(f"Tipo de aventura não suportado: {tipo_aventura}")
    
    @staticmethod
    def CreateCharacter(tipo_aventura: TiposDeAventura, name: str):
        factory = CreateCharacterFactory.GetFactory(tipo_aventura)
        character = factory.Create(name)
        factory.RollAttributes(character)
        return character
