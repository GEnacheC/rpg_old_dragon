import random
from enum import Enum

#region ENUMs

class Dices(Enum):
    D3 = 3
    D6 = 6
    D12 = 12

class Attributes(Enum):
    STRENGTH = 0
    DEXTERY = 1
    CONSTITUTION = 2
    INTELLIGENCE = 3
    KNOWLEDGE = 4
    CHARISMA = 5

class BaseStatus(Enum):
    HEALTH = 100
    MANA = 20

#endregion

class Player:
    def __init__(self, name):
        self.name = name
        self.health = BaseStatus.HEALTH
        self.mana = BaseStatus.MANA

    def Heal(self, heal):
        self.health += heal
    
    def Damage(self, damage):
        self.health -= damage

    def CastSkill(self, mana):
        if mana > self.mana:
            raise ValueError("Sem Mana suficiente para usar a skill")
        self.mana -= mana

    def ManaRegen(self, regen):
        self.mana += regen
    
class Character(Player):

    def __init__(self, name):
        super().__init__(name)
        self.ResetAttributes()
    
    #region Attributes Methods
    
    def AddAttributePoints(self, attribute, points):
        if not isinstance(attribute, Attributes):
            raise ValueError("Tributo inválido")

        match attribute:
            case Attributes.STRENGTH:
                self.strength = points
                return
            case Attributes.DEXTERY:
                self.dextery = points
                return
            case Attributes.CONSTITUTION:
                self.constitution = points
                return
            case Attributes.INTELLIGENCE:
                self.intelligence = points
                return
            case Attributes.KNOWLEDGE:
                self.knowledge = points
                return
            case Attributes.CHARISMA:
                self.charisma = points
                return
    
    def ResetAttributes(self):
        self.strength = 0
        self.dextery = 0
        self.constitution = 0
        self.intelligence = 0
        self.knowledge = 0
        self.charisma = 0

    #endregion     


class GameSystem:
    def __init__(self):
        self.characters = []

    def Start():
        while True:
            return
    
    def Menu():
        print("\n--- Menu ---")
        print("1. Criar Novo Personagem")
        print("2. Carregar Personagem")
        print("3. Apagar Personagem")
        print("4. Sair")
        print("-----------------")
    
    def ExecuteOption(option):
        if option <= 0 and option > 4:
            raise ValueError("Opção inválida")
            
        match option:
            case 1:
                return
            case 2:
                return
            case 3:
                return
            case 4:
                return
    
    def CreateNewCharacter(self):
        new_char_name = str(input("\nNome do Personagem:\n"))
        
    
    
new_player = Character("Leo")

game_system = GameSystem()


