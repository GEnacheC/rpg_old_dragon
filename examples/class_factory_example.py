from factories.class_factory import ClassFactory
from models.enums import Classes

def main():
    print("=== Class Factory Example ===\n")
    
    # Listar todas as classes disponíveis
    print("Classes disponíveis:")
    available_classes = ClassFactory.get_available_classes()
    for i, class_name in enumerate(available_classes, 1):
        print(f"{i}. {class_name}")
    
    print("\n" + "="*50 + "\n")
    
    # Obter informações de cada classe
    for class_enum in Classes:
        print(f"=== {class_enum.value} ===")
        class_info = ClassFactory.get_class_info(class_enum)
        
        print(f"Nome: {class_info['name']}")
        print(f"Descrição: {class_info['description']}")
        print(f"Dado de Vida: d{class_info['hit_dice']}")
        print(f"Bônus de Ataque Base: {class_info['base_attack_bonus']}")
        print(f"Jogadas de Proteção: {', '.join(class_info['saving_throws'])}")
        print(f"Proficiências: {', '.join(class_info['proficiencies'])}")
        
        spellcasting = class_info['spellcasting']
        print(f"Conjuração: {spellcasting['type']}")
        if spellcasting['type'] != "Nenhum":
            print(f"  Habilidade de Conjuração: {spellcasting['spellcasting_ability']}")
            print(f"  Feitiços Conhecidos: {spellcasting['spells_known']}")
        
        print(f"Passivas: {', '.join(class_info['passives']) if class_info['passives'] else 'Nenhuma'}")
        print()
    
    print("="*50)
    
    # Testar criação de uma classe específica
    print("\nTestando criação de classe específica:")
    warrior = ClassFactory.create_class(Classes.WARRIOR)
    print(f"Classe criada: {warrior.name}")
    print(f"Descrição: {warrior.description}")
    print(f"Dado de Vida: d{warrior.hit_dice}")

if __name__ == "__main__":
    main()
