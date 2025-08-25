from enum import Enum

class Dices(Enum):
    D3 = 3
    D6 = 6
    D12 = 12

class Attributes(Enum):
    STRENGTH = 0      # Força
    DEXTERY = 1       # Destreza
    CONSTITUTION = 2  # Constituição
    INTELLIGENCE = 3  # Inteligência
    WISDOM = 4        # Sabedoria
    CHARISMA = 5      # Carisma

class BaseStatus(Enum):
    HEALTH = 100
    MANA = 20

class AdventureTypes(Enum):
    CLASSIC = "classico"
    ADVENTURER = "aventureiro"
    HEROIC = "heroico"

class Alignment(Enum):
    ORDEM = "ORDEM"
    NEUTRAL_GOOD = "Neutro e Bom"
    CHAOTIC_GOOD = "Caótico e Bom"
    LAWFUL_NEUTRAL = "Leal e Neutro"
    NEUTRAL = "Neutro"
    CHAOTIC_NEUTRAL = "Caótico e Neutro"
    LAWFUL_EVIL = "Leal e Mau"
    NEUTRAL_EVIL = "Neutro e Mau"
    CHAOTIC_EVIL = "Caótico e Mau"
    ANY = "Qualquer"

class Darkvision(Enum):
    NONE = 0
    MODERATE = 9
    GOOD = 18

class PassiveTypes(Enum):
    ATTRIBUTES_MODIFIER = "Attributes Modifier"
    ACTIONS_MODIFIER = "Actions Modifier"
    DEFENSE_MODIFIER = "Defense Modifier"

class PassiveOrigin(Enum):
    RACE = "Race"
    CLASS = "Class"
    BACKGROUND = "Background"
    ITEM = "Item"
    SPELL = "Spell"

class PassiveTime(Enum):
    PERMANENT = 0

class Races(Enum):
    HUMAN = "Humano"
    ELF = "Elfo"
    DWARF = "Anão"
    HALFLING = "Halfling"

class Classes(Enum):
    WARRIOR = "Guerreiro"
    MAGE = "Mago"
    THIEF = "Ladrão"