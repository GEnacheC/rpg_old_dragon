from models.races.Human import Human
from models.races.Elf import Elf
from models.races.Dwarf import Dwarf
from models.races.Halfling import Halfling
from interfaces.race_interface import RaceStrategy
from models.enums import Races

class RaceFactory:
    
    @staticmethod
    def get_race(race_type: Races) -> RaceStrategy:
        match race_type:
            case Races.HUMAN:
                return Human()
            case Races.ELF:
                return Elf()
            case Races.DWARF:
                return Dwarf()
            case Races.HALFLING:
                return Halfling()
            case _:
                raise ValueError(f"Race '{race_type}' not found")
    
    @staticmethod
    def create_race(race_type: Races) -> RaceStrategy:
        return RaceFactory.get_race(race_type)
    
    @staticmethod
    def get_available_races() -> list[str]:
        return [race.value for race in Races]
    
    @staticmethod
    def get_available_races_enum() -> list[Races]:
        return list(Races)
    
    @staticmethod
    def is_valid_race(race_type: Races) -> bool:
        return race_type in Races
    
    @staticmethod
    def get_race_info(race_type: Races) -> dict:
        race = RaceFactory.create_race(race_type)
        return {
            "name": race.name,
            "description": race.description,
            "movement": race.movement,
            "darkvision": race.darkvision.value,
            "alignment": race.alignment.value,
            "size": race.get_size(),
            "passives": [passive.name for passive in race.get_race_passives()]
        }
    
    @staticmethod
    def get_all_races_info() -> list[dict]:
        return [RaceFactory.get_race_info(race) for race in Races]
