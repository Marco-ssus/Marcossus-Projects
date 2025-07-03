import os
import re

SAVE_DIR = "saves"

def sanitize_filename(nome):
    # Remove caracteres inválidos para nomes de arquivo
    return re.sub(r'[^\w\s-]', '', nome).strip().replace(' ', '_')

def salvar_jogo(jogador):
    # Salva estado do jogo em arquivo específico para o usuário
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
    
    safe_name = sanitize_filename(jogador['nome'])
    if not safe_name:
        safe_name = "save"
    
    save_path = os.path.join(SAVE_DIR, f"{safe_name}.txt")
    
    try:
        with open(save_path, 'w') as f:
            f.write(f"nome={jogador['nome']}\n")
            f.write(f"classe={jogador['classe']}\n")
            f.write(f"vida={jogador['vida']}\n")
            f.write(f"vida_maxima={jogador['vida_maxima']}\n")
            f.write(f"ataque={jogador['ataque']}\n")
            f.write(f"defesa={jogador['defesa']}\n")
            f.write(f"ouro={jogador['ouro']}\n")
            f.write(f"inimigos_derrotados={jogador['inimigos_derrotados']}\n")
            f.write(f"nivel={jogador.get('nivel', 1)}\n")
            
            f.write("inventario_inicio\n")
            for item in jogador["inventario"]:
                f.write(f"item={item['nome']},{item['tipo']},{item['valor']},{item['preco']}\n")
            f.write("inventario_fim\n")
            
        return True
    except Exception as e:
        print(f"Erro ao salvar o jogo: {e}")
        return False

def listar_saves():
    # Lista todos os jogos salvos disponíveis
    if not os.path.exists(SAVE_DIR):
        return []
        
    saves = []
    for arquivo in os.listdir(SAVE_DIR):
        if arquivo.endswith('.txt'):
            caminho = os.path.join(SAVE_DIR, arquivo)
            try:
                with open(caminho, 'r') as f:
                    primeira_linha = f.readline().strip()
                    if primeira_linha.startswith("nome="):
                        nome_personagem = primeira_linha.split('=')[1]
                        saves.append((caminho, nome_personagem))
            except:
                continue
    return saves

def carregar_arquivo(caminho):
    # Carrega um arquivo de save específico
    try:
        jogador = {"inventario": []}
        inventario = False
        
        with open(caminho, 'r') as f:
            for linha in f:
                linha = linha.strip()
                
                if linha == "inventario_inicio":
                    inventario = True
                    continue
                elif linha == "inventario_fim":
                    inventario = False
                    continue
                
                if inventario:
                    partes = linha.split('=')
                    if len(partes) < 2:
                        continue
                    
                    dados = partes[1].split(',')
                    if len(dados) < 4:
                        continue
                        
                    item = {
                        "nome": dados[0],
                        "tipo": dados[1],
                        "valor": int(dados[2]),
                        "preco": int(dados[3])
                    }
                    jogador["inventario"].append(item)
                else:
                    partes = linha.split('=')
                    if len(partes) < 2:
                        continue
                    
                    chave = partes[0]
                    valor = partes[1]
                    
                    if chave in ["vida", "vida_maxima", "ataque", "defesa", "ouro", "inimigos_derrotados", "nivel"]:
                        try:
                            valor = int(valor)
                        except ValueError:
                            valor = 0
                    
                    jogador[chave] = valor
        
        campos_obrigatorios = ["nome", "classe", "vida", "vida_maxima", "ataque", "defesa", "ouro"]
        for campo in campos_obrigatorios:
            if campo not in jogador:
                return None
                
        return jogador
        
    except Exception as e:
        print(f"Erro ao carregar arquivo: {e}")
        return None

def carregar_jogo():
    # Interface para carregar jogo existente ou criar novo
    saves = listar_saves()
    
    if not saves:
        return None
        
    print("\nEscolha um personagem para carregar:")
    for i, (_, nome) in enumerate(saves, 1):
        print(f"{i}. {nome}")
    print("0. Criar novo personagem")
    
    while True:
        try:
            escolha = int(input("\nDigite o número do personagem: "))
            if escolha == 0:
                return None
            if 1 <= escolha <= len(saves):
                return carregar_arquivo(saves[escolha-1][0])
            print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")