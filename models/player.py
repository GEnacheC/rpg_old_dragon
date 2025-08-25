from models.enums import BaseStatus

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 20

    def heal(self, heal):
        self.health += heal

    def damage(self, damage):
        self.health -= damage

    def cast_skill(self, mana):
        if self.mana >= mana:
            self.mana -= mana
            return True
        return False

    def mana_regen(self, regen):
        self.mana += regen
