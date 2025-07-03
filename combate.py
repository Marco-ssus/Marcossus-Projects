import random
from personagem import mostrar_status
from inimigo import mostrar_inimigo

def atacar(atacante, defensor):
    # Calcula dano do ataque e verifica se o defensor morreu
    # Baixa chance de acerto crítico
    critico = random.random() < 0.1
    dano_base = max(1, atacante["ataque"] - (defensor["defesa"] // 2))
    dano = dano_base * 2 if critico else dano_base
    
    defensor["vida"] -= dano
    msg = f"{atacante['nome']} acerto crítico!" if critico else f"{atacante['nome']} atacou"
    print(f"\n{msg} causando {dano} de dano!")
    return defensor["vida"] <= 0

def usar_pocao(jogador):
    # Usa uma poção do inventário se disponível
    for idx, item in enumerate(jogador["inventario"]):
        if item["tipo"] == "pocao":
            cura = min(item["valor"], jogador["vida_maxima"] - jogador["vida"])
            jogador["vida"] += cura
            print(f"\nUsou {item['nome']}! +{cura} de vida")
            jogador["inventario"].pop(idx)
            return True
    print("\nVocê não tem poções!")
    return False

def iniciar_combate(jogador, inimigo):
    # Gerencia o fluxo de combate com opções de ataque, poção e fuga
    print(f"\n===== COMBATE CONTRA {inimigo['nome']} =====")
    
    while True:
        mostrar_status(jogador)
        mostrar_inimigo(inimigo)
        
        print("\nO que você fará?")
        print("1. Atacar")
        print("2. Usar Poção")
        print("3. Tentar Fugir")
        
        acao = input("\nEscolha sua ação: ")
        
        if acao == "1":
            # Jogador ataca
            if atacar(jogador, inimigo):
                print(f"\nVocê derrotou {inimigo['nome']}!")
                jogador["ouro"] += inimigo["recompensa_ouro"]
                print(f"Encontrou {inimigo['recompensa_ouro']} moedas de ouro!")
                
                # Recompensa especial para o dragão
                if inimigo.get("boss"):
                    jogador["ouro"] += 1000
                    print("Você encontrou o tesouro lendário! +1000 moedas")
                return True
            
            # Inimigo contra-ataca
            if atacar(inimigo, jogador):
                print("\nVocê foi derrotado!")
                jogador["vida"] = jogador["vida_maxima"] // 2
                print("Você acorda na cidade com metade da vida")
                return False
            
        elif acao == "2":
            # Tenta usar poção
            if usar_pocao(jogador):
                # Inimigo ataca após uso da poção
                if atacar(inimigo, jogador):
                    print("\nVocê foi derrotado!")
                    jogador["vida"] = jogador["vida_maxima"] // 2
                    print("Você acorda na cidade com metade da vida")
                    return False
                    
        elif acao == "3":
            # Tentativa de fuga
            if random.random() < 0.4:
                print("\nVocê fugiu com sucesso!")
                return True
            else:
                print("\nFalha ao fugir! O inimigo ataca!")
                if atacar(inimigo, jogador):
                    print("\nVocê foi derrotado!")
                    jogador["vida"] = jogador["vida_maxima"] // 2
                    print("Você acorda na cidade com metade da vida")
                    return False
        else:
            print("\nOpção inválida. Tente novamente.")