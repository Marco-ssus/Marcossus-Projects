def mostrar_itens():
    # Retorna lista de itens disponíveis na loja
    return [
        {"nome": "Poção Pequena", "tipo": "pocao", "valor": 20, "preco": 10},
        {"nome": "Poção Média", "tipo": "pocao", "valor": 40, "preco": 18},
        {"nome": "Poção Grande", "tipo": "pocao", "valor": 60, "preco": 25},
        {"nome": "Espada Afiada", "tipo": "arma", "valor": 3, "preco": 100},
        {"nome": "Escudo Reforçado", "tipo": "defesa", "valor": 2, "preco": 80}
    ]

def loja(jogador):
    # Interface da loja para compra de itens
    itens = mostrar_itens()
    
    while True:
        print("\n=== LOJA ===")
        print(f"Seu ouro: {jogador['ouro']}")
        print("\nItens disponíveis:")
        
        for idx, item in enumerate(itens, 1):
            print(f"{idx}. {item['nome']} - ", end="")
            if item["tipo"] == "pocao":
                print(f"+{item['valor']} vida | {item['preco']} ouro")
            elif item["tipo"] == "arma":
                print(f"+{item['valor']} ataque | {item['preco']} ouro")
            else:
                print(f"+{item['valor']} defesa | {item['preco']} ouro")
        
        print("0. Voltar ao menu")
        
        try:
            escolha = int(input("\nEscolha um item: "))
            if escolha == 0:
                return
            
            item_escolhido = itens[escolha-1]
            
            if jogador["ouro"] < item_escolhido["preco"]:
                print("\nOuro insuficiente!")
                continue
                
            jogador["ouro"] -= item_escolhido["preco"]
            
            if item_escolhido["tipo"] == "pocao":
                jogador["inventario"].append(item_escolhido)
                print(f"\nComprou {item_escolhido['nome']}!")
            else:
                # Melhoria permanente
                if item_escolhido["tipo"] == "arma":
                    jogador["ataque"] += item_escolhido["valor"]
                    print(f"\nSeu ataque aumentou para {jogador['ataque']}!")
                else:
                    jogador["defesa"] += item_escolhido["valor"]
                    print(f"\nSua defesa aumentou para {jogador['defesa']}!")
                
        except (ValueError, IndexError):
            print("\nOpção inválida! Tente novamente.")