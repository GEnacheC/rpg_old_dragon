from models.character import Character
from factories.character_factory import CreateCharacterFactory
from factories.race_factory import RaceFactory
from models.enums import AdventureTypes, Races

class GameSystem:
    def __init__(self):
        self.characters = []

    def start(self):
        while True:
            self.menu()
            try:
                option = int(input("\nEscolha uma opção: "))
                if self.execute_option(option):
                    break
            except ValueError:
                print("Por favor, digite um número válido.")
            except Exception as e:
                print(f"Erro: {e}")
    
    def menu(self):
        print("\n" + "="*50)
        print("           🐉 OLD DRAGON RPG 🐉")
        print("="*50)
        print("1. Criar Novo Personagem")
        print("2. Listar Personagens")
        print("3. Apagar Personagem")
        print("4. Sair")
        print("-"*50)
    
    def execute_option(self, option):
        if option < 1 or option > 5:
            raise ValueError("Opção inválida")
            
        match option:
            case 1:
                self.create_new_character()
                return False
            case 2:
                self.list_characters()
                return False
            case 3:
                self.delete_character()
                return False
            case 4:
                print("\n👋 Obrigado por jogar Old Dragon RPG!")
                return True
    
    def create_new_character(self):
        print("\n" + "="*40)
        print("        🎭 CRIAÇÃO DE PERSONAGEM")
        print("="*40)

        name = input("📝 Nome do Personagem: ").strip()
        if not name:
            print("❌ Nome não pode estar vazio!")
            return
        
        race = self.select_race()
        if race is None:
            return

        race_instance = RaceFactory.get_race(race)

        adventure_type = self.select_adventure_type()
        if adventure_type is None:
            return
        
        print(f"\n🎲 Criando personagem '{name}'...")
        print(f"🎯 Tipo de Aventura: {adventure_type.value.upper()}")
        print(f"🏃 Raça: {race.value}")
        
        character = CreateCharacterFactory.create_character(adventure_type, name, race_instance)
        
        self.characters.append(character)
        
        print(f"\n✅ Personagem '{name}' criado com sucesso!")
        print("\n📊 RESUMO DO PERSONAGEM:")
        self.show_character(character)
        
        input("\nPressione ENTER para continuar...")
    
    def select_adventure_type(self):
        print("\n🎯 Escolha o Tipo de Aventura:")
        print("1. 🎲 Clássico - 3d6 em ordem fixa (tradicional)")
        print("2. ⚔️  Aventureiro - 3d6 com distribuição livre")
        print("3. 🏆 Heroico - 4d6 elimina menor, distribuição livre")
        print("4. ❌ Cancelar")
        
        try:
            choice = int(input("\nEscolha (1-4): "))
            match choice:
                case 1:
                    return AdventureTypes.CLASSIC
                case 2:
                    return AdventureTypes.ADVENTURER
                case 3:
                    return AdventureTypes.HEROIC
                case 4:
                    return None
                case _:
                    print("❌ Opção inválida!")
                    return None
        except ValueError:
            print("❌ Por favor, digite um número válido!")
            return None
    
    def select_race(self):
        print("\n🏃 Escolha a Raça do Personagem:")
        
        available_races = RaceFactory.get_available_races_enum()
        
        for i, race_enum in enumerate(available_races, 1):
            race_info = RaceFactory.get_race_info(race_enum)
            print(f"{i}. {race_enum.value}")
            print(f"   Movimento: {race_info['movement']}m | "
                  f"Infravisão: {race_info['darkvision']}m | "
                  f"Tamanho: {race_info['size']}")
            print(f"   Alinhamento: {race_info['alignment']}")
            print(f"   Habilidades: {', '.join(race_info['passives'])}")
            print()
        
        print(f"{len(available_races) + 1}. ❌ Cancelar")
        
        try:
            choice = int(input(f"\nEscolha (1-{len(available_races) + 1}): "))
            
            if choice == len(available_races) + 1:
                return None
            
            if 1 <= choice <= len(available_races):
                selected_race = available_races[choice - 1]
                race_instance = RaceFactory.get_race(selected_race)
                
                print(f"\n✅ Raça selecionada: {race_instance.name}")
                print(f"📝 Descrição: {race_instance.description}")
                
                return selected_race
            else:
                print("❌ Opção inválida!")
                return None
                
        except ValueError:
            print("❌ Por favor, digite um número válido!")
            return None
    
    def list_characters(self):
        print("\n" + "="*40)
        print("        📋 LISTA DE PERSONAGENS")
        print("="*40)
        
        if not self.characters:
            print("📭 Nenhum personagem criado ainda.")
            print("💡 Use a opção 1 para criar um novo personagem!")
        else:
            for i, character in enumerate(self.characters, 1):
                print(f"\n{i}. {character.name}")
                self.show_character(character, show_header=False)
        
        input("\nPressione ENTER para continuar...")
    
    def delete_character(self):
        if not self.characters:
            print("\n📭 Nenhum personagem para apagar.")
            return
        
        print("\n" + "="*40)
        print("        🗑️  APAGAR PERSONAGEM")
        print("="*40)
        
        for i, character in enumerate(self.characters, 1):
            print(f"{i}. {character.name}")
        
        try:
            choice = int(input(f"\nEscolha um personagem para apagar (1-{len(self.characters)}): "))
            if 1 <= choice <= len(self.characters):
                deleted_char = self.characters.pop(choice - 1)
                print(f"✅ Personagem '{deleted_char.name}' foi apagado!")
            else:
                print("❌ Número inválido!")
        except ValueError:
            print("❌ Por favor, digite um número válido!")
        
        input("\nPressione ENTER para continuar...")
    
    
    def show_character(self, character, show_header=True):
        if show_header:
            print(f"\n👤 {character.name}")
            print("-" * 30)
        
        # Informações básicas
        print(f"  ❤️  Vida: {character.health}")
        print(f"  ✨ Mana: {character.mana}")
    
        # Atributos
        print(f"  💪 Força: {character.strength}")
        print(f"  🏃 Destreza: {character.dextery}")
        print(f"  🛡️  Constituição: {character.constitution}")
        print(f"  🧠 Inteligência: {character.intelligence}")
        print(f"  🙏 Sabedoria: {character.wisdom}")
        print(f"  😊 Carisma: {character.charisma}")
        
        total_attributes = (character.strength + character.dextery + 
                          character.constitution + character.intelligence + 
                          character.wisdom + character.charisma)
        print(f"  📊 Total de Atributos: {total_attributes}")
        
        # Informações da raça (se disponível)
        if hasattr(character, 'race'):
            self.show_race_info(character.race)

        print(f"  ✨ Habilidades Passivas:")
        
        for passive in character.passive_abilities:
            print(f"    • {passive.name}: {passive.description}")
        
        print()
    
    def show_race_info(self, race_instance, show_header=True):
        """Show race information"""
        if show_header:
            print(f"\n🏃 INFORMAÇÕES DA RAÇA: {race_instance.name}")
            print("-" * 40)
        
        print(f"  📝 Descrição: {race_instance.description}")
        print(f"  🏃 Movimento: {race_instance.movement} metros")
        print(f"  👁️  Infravisão: {race_instance.darkvision.value} metros")
        print(f"  ⚖️  Alinhamento: {race_instance.alignment.value}")
        print(f"  📏 Tamanho: {race_instance.get_size()}")
        
        print()
