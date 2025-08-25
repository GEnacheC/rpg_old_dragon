import random
from interfaces.character_interface import CreateCharacterInterface
from interfaces.race_interface import RaceStrategy
from interfaces.class_interface import ClassStrategy
from models.character import Character
from models.enums import Dices, Attributes

class InteractiveDistributionMixin:
    
    def _distribute_points_interactive(self, character: Character, points_pool: list):
        attributes_info = [
            (Attributes.STRENGTH, "Força"),
            (Attributes.DEXTERY, "Destreza"),
            (Attributes.CONSTITUTION, "Constituição"),
            (Attributes.INTELLIGENCE, "Inteligência"),
            (Attributes.WISDOM, "Sabedoria"),
            (Attributes.CHARISMA, "Carisma")
        ]
        
        for attribute, display_name in attributes_info:
            if not points_pool:
                print(f"\n❌ Sem pontos restantes para {display_name}")
                character.add_attribute_points(attribute, 0)
                continue
                
            print(f"\n📋 Distribuindo para {display_name}")
            print(f"   Pontos disponíveis: {points_pool}")
            print(f"   Total restante: {sum(points_pool)}")
            
            while True:
                try:
                    if len(points_pool) == 1:
                        choice = input(f"   Usar {points_pool[0]} pontos em {display_name}? (s/n): ").lower().strip()
                        if choice in ['s', 'sim', 'y', 'yes']:
                            points_to_assign = points_pool[0]
                        else:
                            points_to_assign = 0
                    else:
                        print(f"   Opções: {points_pool} ou 0 para pular")
                        points_input = input(f"   Quantos pontos para {display_name}? ").strip()
                        points_to_assign = int(points_input)
                    
                    if points_to_assign == 0:
                        character.add_attribute_points(attribute, 0)
                        print(f"   ⏭️  Pulando {display_name}")
                        break
                    elif points_to_assign in points_pool:
                        points_pool.remove(points_to_assign)
                        character.add_attribute_points(attribute, points_to_assign)
                        print(f"   ✅ {points_to_assign} pontos atribuídos a {display_name}")
                        break
                    else:
                        print(f"   ❌ Valor {points_to_assign} não está disponível!")
                        
                except ValueError:
                    print("   ❌ Por favor, digite um número válido!")
        
        if points_pool:
            print(f"\n⚠️  Pontos não utilizados: {points_pool} (Total: {sum(points_pool)})")
        else:
            print(f"\n✅ Todos os pontos foram distribuídos!")
        
        print("\n📊 RESUMO DA DISTRIBUIÇÃO:")
        print("-" * 30)

class ClassicFactory(CreateCharacterInterface):
    def create(self, name: str, race: RaceStrategy, character_class: ClassStrategy) -> Character:
        character = Character(name, race, character_class)
        return character
    
    def roll_attributes(self, character: Character) -> Character:
        print(f"🎲 Criando personagem CLÁSSICO: {character.name}")
        print("   Rolando 3d6 em ordem fixa...")
        
        attribute_order = [
            Attributes.STRENGTH,     # Força
            Attributes.DEXTERY,      # Destreza  
            Attributes.CONSTITUTION, # Constituição
            Attributes.INTELLIGENCE, # Inteligência
            Attributes.WISDOM,       # Sabedoria
            Attributes.CHARISMA      # Carisma
        ]
        
        for attribute in attribute_order:
            rolls = [random.randint(1, Dices.D6.value) for _ in range(3)]
            roll_result = sum(rolls)
            character.add_attribute_points(attribute, roll_result)
            print(f"  {attribute.name}: {rolls} = {roll_result}")
        
        return character

class AdventurerFactory(CreateCharacterInterface, InteractiveDistributionMixin):
    def create(self, name: str, race: RaceStrategy, character_class: ClassStrategy) -> Character:
        character = Character(name, race, character_class)
        return character
    
    def roll_attributes(self, character: Character) -> Character:
        print(f"⚔️ Criando personagem AVENTUREIRO: {character.name}")
        print("   Rolando 3d6 seis vezes para distribuição livre...")
        
        rolled_values = []
        for i in range(6):
            rolls = [random.randint(1, Dices.D6.value) for _ in range(3)]
            roll_result = sum(rolls)
            rolled_values.append(roll_result)
            print(f"  Rolagem {i+1}: {rolls} = {roll_result}")
        
        print(f"\n   Valores disponíveis: {sorted(rolled_values, reverse=True)}")
        print("   Total de pontos: {}".format(sum(rolled_values)))
        
        self._distribute_points_interactive(character, rolled_values)
        
        return character

class HeroicFactory(CreateCharacterInterface, InteractiveDistributionMixin):
    def create(self, name: str, race: RaceStrategy, character_class: ClassStrategy) -> Character:
        character = Character(name, race, character_class)
        return character
    
    def roll_attributes(self, character: Character) -> Character:
        print(f"🏆 Criando personagem HEROICO: {character.name}")
        print("   Rolando 4d6 elimina menor seis vezes para distribuição livre...")
        
        rolled_values = []
        for i in range(6):
            rolls = [random.randint(1, Dices.D6.value) for _ in range(4)]
            rolls.sort(reverse=True)
            roll_result = sum(rolls[:3])
            rolled_values.append(roll_result)
            print(f"  Rolagem {i+1}: {rolls} (elimina {rolls[3]}) = {roll_result}")
        
        print(f"\n   Valores disponíveis: {sorted(rolled_values, reverse=True)}")
        print("   Total de pontos: {}".format(sum(rolled_values)))
        
        self._distribute_points_interactive(character, rolled_values)
        
        return character