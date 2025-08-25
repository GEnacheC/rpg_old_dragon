from models.enums import PassiveOrigin, PassiveTypes

class Passive:
    
    def __init__(self, name: str, description: str, type: PassiveTypes, origin: PassiveOrigin, time):
        self.name = name
        self.description = description
        self.type = type
        self.origin = origin
        self.time = time

    def apply_passive(self, character):
        pass
    
    def __str__(self) -> str:
        return f"{self.name} ({self.type}): {self.description}"
    
    def __repr__(self) -> str:
        return f"Passive(name='{self.name}', type='{self.type}', description='{self.description}', origin='{self.origin}', time='{self.time}')"
