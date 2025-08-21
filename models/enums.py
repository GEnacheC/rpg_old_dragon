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

class TiposDeAventura(Enum):
    CLASSICO = "classico"
    AVENTUREIRO = "aventureiro"
    HEROICO = "heroico"
