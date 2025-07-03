from personagem import criar_personagem, mostrar_status
from inimigo import criar_inimigo, criar_dragao
from combate import iniciar_combate
from loja import loja
from save_load import salvar_jogo, carregar_jogo
import random
import os

# História do jogo
HISTORIA_INTRO = """
Há muito tempo, o reino de Eldoria foi amaldiçoado pelo Dragão Supremo, 
que espalhou trevas e criaturas malignas pela terra. Como {classe}, você 
é a última esperança para libertar nosso reino. Sua jornada começa agora...
"""

HISTORIA_FLORESTA = [
    "Você adentra a Floresta Sombria, onde criaturas ancestrais habitam.",
    "O ar fica mais frio conforme você avança pela trilha escura.",
    "Sussurros estranhos ecoam entre as árvores antigas da floresta.",
    "Uma névoa espessa desce sobre a floresta, limitando sua visão.",
    "Você sente uma presença maligna observando seus movimentos..."
]

HISTORIA_DRAGAO = """
====================================================================
Após derrotar 5 criaturas poderosas, você reuniu energia suficiente 
para desafiar o Dragão Supremo. A terra treme quando ele surge diante 
de você, suas escamas negras brilhando como obsidiana sob a luz 
fraca que penetra as nuvens de tempestade.

'INSOLENTE MORTAL!' - o dragão troveja - 'VOCÊ OUSA DESAFIAR O SENHOR 
DESTE REINO? SUA OUSADIA SERÁ PUNIDA COM A MORTE ETERNA!'

Prepare-se para o combate final que decidirá o destino de Eldoria!
====================================================================
"""

HISTORIA_VITORIA = """
====================================================================
COM UM GRITO FINAL DE DETERMINAÇÃO, VOCÊ DESFERIU O GOLPE DECISIVO!

O Dragão Supremo desaba no chão, seu corpo começando a se dissolver em 
milhares de partículas de luz. À medida que a escuridão se dissipa, 
a luz do sol retorna a Eldoria pela primeira vez em séculos.

O povo celebra você como herói, e suas histórias serão contadas por 
gerações. Mas novas ameaças sempre surgem... Sua jornada continua!
====================================================================
"""

def main():
    # Função principal do jogo com menu e fluxo principal
    print("Bem-vindo ao RPG de Terminal!")
    
    # Carrega jogo existente ou cria novo
    jogador = carregar_jogo()
    
    if not jogador:
        print("\nCriando novo personagem...")
        jogador = criar_personagem()
        jogador["inimigos_derrotados"] = 0
        
        # Mostra introdução da história
        print(HISTORIA_INTRO.format(classe=jogador['classe'].lower()))
    
    while True:
        print("\n=== MENU PRINCIPAL ===")
        mostrar_status(jogador)  
        print(f"Inimigos derrotados: {jogador['inimigos_derrotados']}/5")
        print("\n1. Explorar a Floresta")
        print("2. Visitar Loja")
        print("3. Salvar Jogo")
        print("4. Sair do Jogo")
        
        escolha = input("\nEscolha uma opção: ")
        
        if escolha == "1":
            # Mostra trecho aleatório da história da floresta
            print("\n" + random.choice(HISTORIA_FLORESTA))
            
            # Verifica se é hora do dragão aparecer
            if jogador["inimigos_derrotados"] >= 5:
                print(HISTORIA_DRAGAO)
                inimigo = criar_dragao(jogador.get("nivel", 1))
                vitoria = iniciar_combate(jogador, inimigo)
                if vitoria:
                    print(HISTORIA_VITORIA)
                    jogador["inimigos_derrotados"] = 0  # Reseta contador
                    jogador["nivel"] = jogador.get("nivel", 1) + 1  # Aumenta nível após vitória
                    jogador["vida_maxima"] += 20
                    jogador["ataque"] += 3
                    jogador["defesa"] += 2
                    print("Você subiu de nível! Atributos aumentados!")
                continue
            
            # Gera inimigo regular
            nivel_jogador = max(1, (jogador["ataque"] - 10) // 3 + 1)
            jogador["nivel"] = nivel_jogador
            inimigo = criar_inimigo(nivel_jogador)
            vitoria = iniciar_combate(jogador, inimigo)
            
            if vitoria:
                jogador["inimigos_derrotados"] += 1
                restantes = 5 - jogador["inimigos_derrotados"]
                print(f"\nInimigos derrotados: {jogador['inimigos_derrotados']}/5")
                
                # Mensagem de progresso na história
                if restantes > 0:
                    print(f"\nA cada criatura derrotada, você sente que está mais perto")
                    print(f"de atrair a atenção do Dragão Supremo. Faltam {restantes} derrotas.")
            
        elif escolha == "2":
            # História relacionada à loja
            print("\nVocê entra na Loja do Velho Tobias, um comerciante excêntrico")
            print("que parece saber mais sobre sua missão do que deveria...")
            print(f'"Ah, {jogador["nome"]}! Precisando de equipamentos para sua jornada?"')
            loja(jogador)
            
        elif escolha == "3":
            if salvar_jogo(jogador):
                print("\nProgresso salvo com sucesso!")
            else:
                print("\nErro ao salvar o progresso!")
            
        elif escolha == "4":
            print("\nObrigado por jogar! Até a próxima aventura em Eldoria!")
            break
            
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()