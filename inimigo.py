import random

def criar_inimigo(nivel_jogador):
    # Cria inimigo baseado no nível do jogador com atributos balanceados
    # Lista de dicionários com tipos de inimigos
    tipos_inimigos = [
        {"nome": "Aranha Gigante", "dificuldade": 2},
        {"nome": "Lobisomem", "dificuldade": 2},
        {"nome": "Esqueleto", "dificuldade": 1},
        {"nome": "Goblin", "dificuldade": 1}
    ]
    
    # Seleciona inimigo aleatório
    inimigo_base = random.choice(tipos_inimigos)
    nivel = max(1, nivel_jogador - 1 + random.randint(0, 2))
    fator = inimigo_base["dificuldade"]
    
    return {
        "nome": f"{inimigo_base['nome']} Nv.{nivel}",
        "vida": 20 + (nivel * 5 * fator),
        "ataque": 5 + (nivel * fator),
        "defesa": 2 + (nivel * fator),
        "recompensa_ouro": 10 * nivel * fator,
        "boss": False
    }

def criar_dragao(nivel_jogador):
    # Cria o dragão final com atributos balanceados
    nivel = max(3, nivel_jogador) 
    return {
        "nome": f"Dragão Supremo Nv.{nivel}",
        "vida": 50 + (nivel * 10), 
        "ataque": 10 + (nivel * 2), 
        "defesa": 5 + (nivel * 1),  
        "recompensa_ouro": 200 * nivel,  
        "boss": True
    }

def mostrar_inimigo(inimigo):
    # Exibe status do inimigo
    print(f"\nINIMIGO: {inimigo['nome']}")
    print(f"Vida: {inimigo['vida']}")
    print(f"Ataque: {inimigo['ataque']}")
    print(f"Defesa: {inimigo['defesa']}")