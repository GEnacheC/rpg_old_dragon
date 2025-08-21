from models.character import Character
from factories.character_factory import CreateCharacterFactory
from models.enums import TiposDeAventura

class GameSystem:
    def __init__(self):
        self.characters = []

    def Start(self):
        while True:
            self.Menu()
            try:
                option = int(input("\nEscolha uma opção: "))
                if self.ExecuteOption(option):
                    break
            except ValueError:
                print("Por favor, digite um número válido.")
            except Exception as e:
                print(f"Erro: {e}")
    
    def Menu(self):
        print("\n" + "="*50)
        print("           🐉 OLD DRAGON RPG 🐉")
        print("="*50)
        print("1. Criar Novo Personagem")
        print("2. Listar Personagens")
        print("3. Apagar Personagem")
        print("4. Sair")
        print("-"*50)
    
    def ExecuteOption(self, option):
        if option < 1 or option > 5:
            raise ValueError("Opção inválida")
            
        match option:
            case 1:
                self.CreateNewCharacter()
                return False
            case 2:
                self.ListCharacters()
                return False
            case 3:
                self.DeleteCharacter()
                return False
            case 4:
                print("\n👋 Obrigado por jogar Old Dragon RPG!")
                return True
    
    def CreateNewCharacter(self):
        print("\n" + "="*40)
        print("        🎭 CRIAÇÃO DE PERSONAGEM")
        print("="*40)

        name = input("📝 Nome do Personagem: ").strip()
        if not name:
            print("❌ Nome não pode estar vazio!")
            return
        
        tipo_aventura = self.SelectAdventureType()
        if tipo_aventura is None:
            return
        
        print(f"\n🎲 Criando personagem '{name}' no estilo {tipo_aventura.value.upper()}...")
        character = CreateCharacterFactory.CreateCharacter(tipo_aventura, name)
        
        self.characters.append(character)
        
        print(f"\n✅ Personagem '{name}' criado com sucesso!")
        print("\n📊 RESUMO DO PERSONAGEM:")
        self.MostrarPersonagem(character)
        
        input("\nPressione ENTER para continuar...")
    
    def SelectAdventureType(self):
        print("\n🎯 Escolha o Tipo de Aventura:")
        print("1. 🎲 Clássico - 3d6 em ordem fixa (tradicional)")
        print("2. ⚔️  Aventureiro - 3d6 com distribuição livre")
        print("3. 🏆 Heroico - 4d6 elimina menor, distribuição livre")
        print("4. ❌ Cancelar")
        
        try:
            choice = int(input("\nEscolha (1-4): "))
            match choice:
                case 1:
                    return TiposDeAventura.CLASSICO
                case 2:
                    return TiposDeAventura.AVENTUREIRO
                case 3:
                    return TiposDeAventura.HEROICO
                case 4:
                    return None
                case _:
                    print("❌ Opção inválida!")
                    return None
        except ValueError:
            print("❌ Por favor, digite um número válido!")
            return None
    
    def ListCharacters(self):
        print("\n" + "="*40)
        print("        📋 LISTA DE PERSONAGENS")
        print("="*40)
        
        if not self.characters:
            print("📭 Nenhum personagem criado ainda.")
            print("💡 Use a opção 1 para criar um novo personagem!")
        else:
            for i, character in enumerate(self.characters, 1):
                print(f"\n{i}. {character.name}")
                self.MostrarPersonagem(character, show_header=False)
        
        input("\nPressione ENTER para continuar...")
    
    def DeleteCharacter(self):
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
    
    
    def MostrarPersonagem(self, personagem, show_header=True):
        if show_header:
            print(f"\n👤 {personagem.name}")
            print("-" * 30)
        
        print(f"  ❤️  Vida: {personagem.health}")
        print(f"  ✨ Mana: {personagem.mana}")
        print(f"  💪 Força: {personagem.strength}")
        print(f"  🏃 Destreza: {personagem.dextery}")
        print(f"  🛡️  Constituição: {personagem.constitution}")
        print(f"  🧠 Inteligência: {personagem.intelligence}")
        print(f"  🙏 Sabedoria: {personagem.wisdom}")
        print(f"  😊 Carisma: {personagem.charisma}")
        
        total_attributes = (personagem.strength + personagem.dextery + 
                          personagem.constitution + personagem.intelligence + 
                          personagem.wisdom + personagem.charisma)
        print(f"  📊 Total de Atributos: {total_attributes}")
        print()
