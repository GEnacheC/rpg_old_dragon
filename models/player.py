from models.enums import BaseStatus

class Player:
    def __init__(self, name):
        self.name = name
        self.health = BaseStatus.HEALTH.value
        self.mana = BaseStatus.MANA.value

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
