def mostrar_status(jogador):
    # Exibe status completo do jogador
    print(f"\nJOGADOR: {jogador['nome']} ({jogador['classe']})")
    print(f"Nível: {jogador.get('nivel', 1)}")
    print(f"Vida: {jogador['vida']}/{jogador['vida_maxima']}")
    print(f"Ataque: {jogador['ataque']} | Defesa: {jogador['defesa']}")
    print(f"Ouro: {jogador['ouro']}")
    
    # Mostra inventário (lista de dicionários)
    if jogador["inventario"]:
        print("\nInventário:")
        for item in jogador["inventario"]:
            if item["tipo"] == "pocao":
                print(f"- {item['nome']} (+{item['valor']} vida)")
    else:
        print("\nInventário: Vazio")

def criar_personagem():
    # Cria novo personagem com escolha de classe e atributos iniciais
    print("\n=== Criação de Personagem ===")
    nome = input("Nome do herói: ").strip()
    while not nome:
        print("Nome não pode ser vazio!")
        nome = input("Nome do herói: ").strip()
    
    print("\nEscolha sua classe:")
    print("1. Guerreiro - Força bruta e resistência")
    print("2. Mago - Poder mágico impressionante")
    print("3. Ladino - Agilidade e astúcia")
    
    classes = {
        "1": "Guerreiro",
        "2": "Mago",
        "3": "Ladino"
    }
    
    while True:
        escolha = input("\nDigite o número da sua escolha: ")
        classe = classes.get(escolha)
        
        if classe:
            break
        print("Escolha inválida. Por favor, tente novamente.")
    
    # Cria personagem com inventário vazio (lista de dicionários)
    personagem = {
        "nome": nome,
        "classe": classe,
        "vida": 100,
        "vida_maxima": 100,
        "ataque": 10,
        "defesa": 5,
        "ouro": 50,
        "inventario": [],
        "inimigos_derrotados": 0,
        "nivel": 1  # Nível inicial corrigido para 1
    }
    
    # Ajustes de classe
    if classe == "Guerreiro":
        personagem["ataque"] += 5
        personagem["vida_maxima"] += 20
        personagem["vida"] += 20
        print(f"\nBem-vindo, {nome}! Sua força é lendária!")
    elif classe == "Mago":
        personagem["ataque"] += 8
        print(f"\n{nome}, a magia corre em suas veias!")
    elif classe == "Ladino":
        personagem["defesa"] += 3
        print(f"\n{nome}, suas habilidades furtivas são impressionantes!")
    
    return personagem