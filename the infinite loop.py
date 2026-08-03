import os
import time

def limpar():
    os.system("clear" if os.name != "nt" else "cls")

def menu(): # Mostra o menu
    print("""------------------------------
         THE INFINITE LOOP 
              v.1.0
    Digite "/start" para começar
    ou "/help" para ver os comandos
------------------------------""")

def obter_nickname(): # Pega o nick do usuário
    while True:
        nick = input("Insira seu nome de usuário: ").strip() # .strip serve para tirar espaços em branco e descontar o caractere dele, exemplo "    ola  " fica "ola"
        tamanho = len(nick)
        
        if tamanho == 0:
            print("O nome de usuário não pode ser vazio.")
        elif tamanho > 15:
            print("O nome de usuário deve ter menos de 15 caracteres.")
        else:
            os.system("clear" if os.name != "nt" else "cls")
        
            print(f"""
Olá, aventureiro(a) {nick}! Bem-vindo ao THE INFINITE LOOP!
Este é um RPG de texto focado em uma temática medieval, com criaturas, magias e espadas,
estimulando sua criatividade ao decorrer da história.
O jogo pode conter alguns erros, então leve isso em consideração.
Esperamos que se divirta jogando o nosso text-based RPG!
            \n""")

            return nick 
        
def trocar_nickname(antigo_nick): # Troca o nick do usuário com o comando /renick
    while True:
         
        novo_nick = input("Insira seu novo nome de usuário: ").strip() # .strip serve para tirar espaços em branco e descontar o caractere dele, exemplo "    ola  " fica "ola"
        tamanho = len(novo_nick)
        
        if tamanho == 0:
            print("O novo nome de usuário não pode ser vazio.")
        elif tamanho > 15:
            print("O novo nome de usuário deve ter menos de 15 caracteres.")
        else:
            print(f"Nick antigo: {antigo_nick}")
            print(f"Nick novo: {novo_nick}")
            return novo_nick
        
def exibir_help(): # Exibe o comando /help
    print("""
------------ COMANDOS GLOBAIS ----------------
/start  : Inicia a criação de personagem e o jogo;
/sair   : Fecha o programa;
/help   : Mostra a lista de comandos;
/devs   : Mostra a gamedev e os devs do jogo;
/renick : Troca o nome de usuário já existente;
/clear  : Limpa o terminal;
/tabraca: Mostra a tabela das racas;

----------- COMANDOS GAMEPLAY ----------------
/inv : Mostra o inventário do jogador;
/nick: Mostra o nick atual do jogador;
/sts : Mostra os status do jogador;
/raca: Mostra a raca do jogador;

""")

def exibir_devs(): # Exibe os devs e a gamedev
    print("""
THE INFINITE LOOP é um jogo de RPG feito exclusivamente com Python. Ele veio de uma ideia de trabalho proposta
pelo professor Alison Borges, do Instituto Federal Catarinense — Campus Concórdia. O jogo foi produzido pelos
alunos Ramon Petry e Davi Patzlaff em 2026, no primeiro ano do Ensino Médio integrado ao Técnico em Informáti-
ca para Internet. O jogo foi inspirado em RPGs de texto (Text-based RPG), especialmente em jogos como Zork.
""")
     

def obter_raca():
    print("""
         
                            Escolha sua raca
           --=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--          
           |------------  vida | defesa | velocidade | mana |
           | Humano    |  100  |   20   |     20     |   0  |
           | Elfo      |   85  |   12   |     25     |  60  |
           | Anao      |  130  |   32   |     12     |   0  |
           | Goblin    |   70  |   10   |     30     |   0  |
           | Draconato |  115  |   25   |     16     |  30  |
           --=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--
           """)
    while True:
        raca = input("->").lower()

        if raca=="humano":
             print(f"\nRaca escolhida: Humano\n")
             return "Humano"

        elif raca=="elfo":
             print(f"\nRaca escolhida: Elfo\n")
             return "Elfo"

        elif raca=="anao":
             print(f"\nRaca escolhida: Anao\n")
             return "Anao"

        elif raca=="goblin":
             print(f"\nRaca escolhida: Goblin\n")
             return "Goblin"

        elif raca=="draconato":
             print(f"\nRaca escolhida: Draconato\n")
             return "Draconato"

        else:
             print("\nRaca nao identificada, veja a tebela a cima e escolha sua raca.\n")

        
# Atributos globais ↓

xp = 0 # Dá para fazer um sistema em que a cada 100 de xp ele reseta e ganha um nível, ganhando mais atributos
nivel = 0
fase=1
inventario = {'item_de_exemplo'}
items_no_inv = len(inventario)
# Talvez adicionar mais alguma coisa

# Tem que fazer todos os itens do jogo e seus respectivos pesos, ex: (adaga=5) adaga pesa 5 pontos
item_de_exemplo = 10 
# Fazendo isso, dá para saber quanto peso o personagem está carregando
ouro=0
fome = 100
armadura = 0 # A armadura aqui vem do que ele está vestindo
peso = 0 + item_de_exemplo # Quanto peso o personagem carrega (fiz a soma do item de exemplo só para ver como fica)
# Atributos que mudam dependendo da raça ↓ 

vida = 0 # 100 é a vida base, dependendo da raça pode aumentar ou diminuir
velocidade = 0
defesa = 0 
mana = 0       




def retirar_item_inv():
    while True:
        entrada_inv = str(input("""
    ---Voce deseja tirar algum item do inventario?---
                sim                nao

    """)).strip().lower()
            
        if entrada_inv == "sim":
            item = str(input("Qual(is) item(s) vc deseja retirar do seu inventario? "))
            
            if item in inventario:
                inventario.remove(item)
                print(f"Seu inventario ficou assim: {inventario}")
            else:
                print("Esse item não está no seu inventário.")
                
            break
        elif entrada_inv == "nao":
            print("\nVoltando")
            break
        else:
            print('Comando errado digite "sim" ou "nao".')
            
        
def exibir_inventario():
    print(f"""
    Você tem {inventario} no seu inventário.
    """)
    retirar_item_inv()


def exibir_status(nome_usuario,vida,defesa,velocidade,mana,items_no_inv,fase):
    print(f"""              
            - STATUS DE {nome_usuario.upper()} -
            Fase:..........{fase}/100
            Vida:..........{vida}
            Fome:..........{fome}/100
            Ouro:..........{ouro}
            Peso:..........{peso}
            XP:............{xp}/100
            Nível:.........{nivel}
            Itens no inv:..{items_no_inv}/100
            Armadura:......{armadura}
            Defesa:........{armadura+defesa}
            Velocidade:....{velocidade}
            Mana...........{mana}
""") 

def exibir_raca(raca_personagem):
     print(f"Sua raca e: {raca_personagem}")

def definir_atributos(raca):
    if raca == "Humano":
        return 100, 20, 20, 0 # vida, defesa, velocidade, mana
    elif raca == "Elfo":
        return 85, 12, 25, 60
    elif raca == "Anao":
        return 130, 32, 12, 0
    elif raca == "Goblin":
        return 70, 10, 30, 0
    elif raca == "Draconato":
        return 115, 25, 16, 30
    else:
        return 100, 10, 10, 0

def exibir_tabeal_raca():
         print("""
         
                          Tabela de racas
           --=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--          
           |------------  vida | defesa | velocidade | mana |
           | Humano    |  100  |   20   |     20     |   0  |
           | Elfo      |   85  |   12   |     25     |  60  |
           | Anao      |  130  |   32   |     12     |   0  |
           | Goblin    |   70  |   10   |     30     |   0  |
           | Draconato |  115  |   25   |     16     |  30  |
           --=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--
           """)

def monstros(entrada_monstro): #aq temos um dicionario que funciona como um tipo de lista, mais facil para fazer um return de varias coisas
         
    monstro = {
        "Nome_monstro":"Nenhum",
        "vida_monstro":0,
        "dano_monstro":0,
        "velocidade_monstro":0,
        "defesa_monstro":0,
        "xp_monstro":0,
        "drop_moeda":0,
        "drops_100%_monstro":[]
    }

    # ato 1 floresta dos susuros fases 1 a 12 ↓

    if entrada_monstro=="slime_verde":
        monstro= {
            "nome_monstro":"Slime Verde",
            "vida_monstro":30,
            "dano_monstro":5,
            "velocidade_monstro":8,
            "defesa_monstro":2,
            "xp_montro":25,
            "drop_moeda":5,
            "drops_100%_monstro":[]
        }

    elif entrada_monstro=="lobo_solitario":
        monstro = {
            "nome_monstro":"Lobo Solitario",
            "vida_monstro":45,
            "dano_monstro":10,
            "velocidade_monstro":22,
            "defesa_monstro":4,
            "xp_monstro":35,
            "drop_moeda":10,
            "drops_100%_monstro":[]
        }

    elif entrada_monstro=="goblin_sequestrador":
        monstro = {
            "nome_monstro":"Goblin Sequestrador",
            "vida_mostro":40,
            "dano_monstro":8,
            "velocidade_montro":18,
            "defesa_monstro":5,
            "xp_montro":30,
            "drop_moeda":15,
            "drops_100%_monstro":[]
        }

    elif entrada_monstro=="rato_gigante":
        monstro = {    
            "nome_monstro":"Rato Gigante",
            "vida_mostro":35,
            "dano_monstro":7,
            "velocidade_montro":20,
            "defesa_monstro":3,
            "xp_montro":25,
            "drop_moeda":8,
            "drops_100%_monstro":[]
        } 

    elif entrada_monstro=="":
        monstro = {    
            "nome_monstro":"Aranha Caçadora",
            "vida_mostro":50,
            "dano_monstro":12,
            "velocidade_montro":24,
            "defesa_monstro":6,
            "xp_montro":40,
            "drop_moeda":18,
            "drops_100%_monstro":[]
        } 

    elif entrada_monstro == "goblin_guerreiro":
            monstro = {
                "nome_monstro": "Goblin Guerreiro",
                "vida_monstro": 60,
                "dano_monstro": 14,
                "velocidade_monstro": 15,
                "defesa_monstro": 12,
                "xp_monstro": 50,
                "drop_moeda": 25,
                "drops_100_monstro": []
            }
    elif entrada_monstro == "javali_enfurecido":
        monstro = {
            "nome_monstro": "Javali Enfurecido",
            "vida_monstro": 70,
            "dano_monstro": 16,
            "velocidade_monstro": 18,
            "defesa_monstro": 8,
            "xp_monstro": 55,
            "drop_moeda": 20,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "planta_carnivora":
        monstro = {
            "nome_monstro": "Planta Carnívora",
            "vida_monstro": 80,
            "dano_monstro": 15,
            "velocidade_monstro": 10,
            "defesa_monstro": 10,
            "xp_monstro": 60,
            "drop_moeda": 30,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "esqueleto_errante":
        monstro = {
            "nome_monstro": "Esqueleto Errante",
            "vida_monstro": 55,
            "dano_monstro": 11,
            "velocidade_monstro": 12,
            "defesa_monstro": 10,
            "xp_monstro": 45,
            "drop_moeda": 12,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "kobold_espiao":
        monstro = {
            "nome_monstro": "Kobold Espião",
            "vida_monstro": 45,
            "dano_monstro": 9,
            "velocidade_monstro": 26,
            "defesa_monstro": 5,
            "xp_monstro": 40,
            "drop_moeda": 22,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "ent_menor":
        monstro = {
            "nome_monstro": "Ent Menor",
            "vida_monstro": 90,
            "dano_monstro": 13,
            "velocidade_monstro": 8,
            "defesa_monstro": 18,
            "xp_monstro": 70,
            "drop_moeda": 28,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "urso_de_pedra":
        monstro = {
            "nome_monstro": "Urso de Pedra",
            "vida_monstro": 180,
            "dano_monstro": 22,
            "velocidade_monstro": 12,
            "defesa_monstro": 25,
            "xp_monstro": 200,
            "drop_moeda": 80,
            "drops_100_monstro": []
        }

    #ato 2 as minas esquecidas fases 13 a 25 ↓

    elif entrada_monstro == "morcego_vampiro":
        monstro = {
            "nome_monstro": "Morcego Vampiro",
            "vida_monstro": 50,
            "dano_monstro": 12,
            "velocidade_monstro": 28,
            "defesa_monstro": 4,
            "xp_monstro": 50,
            "drop_moeda": 15,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "goblin_minerador":
        monstro = {
            "nome_monstro": "Goblin Minerador",
            "vida_monstro": 65,
            "dano_monstro": 15,
            "velocidade_monstro": 16,
            "defesa_monstro": 10,
            "xp_monstro": 65,
            "drop_moeda": 35,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "larva_escavadora":
        monstro = {
            "nome_monstro": "Larva Escavadora",
            "vida_monstro": 75,
            "dano_monstro": 14,
            "velocidade_monstro": 10,
            "defesa_monstro": 15,
            "xp_monstro": 60,
            "drop_moeda": 20,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "esqueleto_armado":
        monstro = {
            "nome_monstro": "Esqueleto Armado",
            "vida_monstro": 85,
            "dano_monstro": 18,
            "velocidade_monstro": 14,
            "defesa_monstro": 18,
            "xp_monstro": 75,
            "drop_moeda": 30,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "necrofago":
        monstro = {
            "nome_monstro": "Necrófago",
            "vida_monstro": 90,
            "dano_monstro": 20,
            "velocidade_monstro": 18,
            "defesa_monstro": 12,
            "xp_monstro": 80,
            "drop_moeda": 32,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "aranha_das_cavernas":
        monstro = {
            "nome_monstro": "Aranha das Cavernas",
            "vida_monstro": 80,
            "dano_monstro": 17,
            "velocidade_monstro": 25,
            "defesa_monstro": 10,
            "xp_monstro": 70,
            "drop_moeda": 28,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "gargula_de_pedra":
        monstro = {
            "nome_monstro": "Gárgula de Pedra",
            "vida_monstro": 110,
            "dano_monstro": 16,
            "velocidade_monstro": 12,
            "defesa_monstro": 28,
            "xp_monstro": 90,
            "drop_moeda": 40,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "zumbi_de_mina":
        monstro = {
            "nome_monstro": "Zumbi de Mina",
            "vida_monstro": 120,
            "dano_monstro": 15,
            "velocidade_monstro": 6,
            "defesa_monstro": 8,
            "xp_monstro": 85,
            "drop_moeda": 25,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "espectro_de_minerio":
        monstro = {
            "nome_monstro": "Espectro de Minério",
            "vida_monstro": 95,
            "dano_monstro": 22,
            "velocidade_monstro": 22,
            "defesa_monstro": 14,
            "xp_monstro": 95,
            "drop_moeda": 45,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "cobra_cuspideira":
        monstro = {
            "nome_monstro": "Cobra Cuspideira",
            "vida_monstro": 70,
            "dano_monstro": 19,
            "velocidade_monstro": 24,
            "defesa_monstro": 8,
            "xp_monstro": 75,
            "drop_moeda": 30,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "troll_das_cavernas":
        monstro = {
            "nome_monstro": "Troll das Cavernas",
            "vida_monstro": 160,
            "dano_monstro": 26,
            "velocidade_monstro": 10,
            "defesa_monstro": 20,
            "xp_monstro": 130,
            "drop_moeda": 60,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "basilisco_jovem":
        monstro = {
            "nome_monstro": "Basilisco Jovem",
            "vida_monstro": 130,
            "dano_monstro": 24,
            "velocidade_monstro": 20,
            "defesa_monstro": 22,
            "xp_monstro": 110,
            "drop_moeda": 55,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "golem_de_cristal":
        monstro = {
            "nome_monstro": "Golem de Cristal",
            "vida_monstro": 280,
            "dano_monstro": 30,
            "velocidade_monstro": 10,
            "defesa_monstro": 38,
            "xp_monstro": 350,
            "drop_moeda": 150,
            "drops_100_monstro": []
        }
 
    #ato 3 as ruinas arcanas 26 a 37 ↓

    elif entrada_monstro == "constructo_magico":
        monstro = {
            "nome_monstro": "Constructo Mágico",
            "vida_monstro": 130,
            "dano_monstro": 22,
            "velocidade_monstro": 14,
            "defesa_monstro": 25,
            "xp_monstro": 120,
            "drop_moeda": 50,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "cultista_novato":
        monstro = {
            "nome_monstro": "Cultista Novato",
            "vida_monstro": 100,
            "dano_monstro": 26,
            "velocidade_monstro": 18,
            "defesa_monstro": 12,
            "xp_monstro": 110,
            "drop_moeda": 45,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "elementar_de_fogo":
        monstro = {
            "nome_monstro": "Elementar de Fogo",
            "vida_monstro": 120,
            "dano_monstro": 30,
            "velocidade_monstro": 22,
            "defesa_monstro": 15,
            "xp_monstro": 135,
            "drop_moeda": 55,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "elementar_de_gelo":
        monstro = {
            "nome_monstro": "Elementar de Gelo",
            "vida_monstro": 140,
            "dano_monstro": 22,
            "velocidade_monstro": 16,
            "defesa_monstro": 24,
            "xp_monstro": 135,
            "drop_moeda": 55,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "lamina_vazia":
        monstro = {
            "nome_monstro": "Lâmina Vazia",
            "vida_monstro": 90,
            "dano_monstro": 32,
            "velocidade_monstro": 32,
            "defesa_monstro": 10,
            "xp_monstro": 125,
            "drop_moeda": 40,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "mago_renegado":
        monstro = {
            "nome_monstro": "Mago Renegado",
            "vida_monstro": 110,
            "dano_monstro": 28,
            "velocidade_monstro": 20,
            "defesa_monstro": 14,
            "xp_monstro": 140,
            "drop_moeda": 60,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "cavaleiro_espectral":
        monstro = {
            "nome_monstro": "Cavaleiro Espectral",
            "vida_monstro": 160,
            "dano_monstro": 34,
            "velocidade_monstro": 18,
            "defesa_monstro": 30,
            "xp_monstro": 160,
            "drop_moeda": 70,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "sombra_faminta":
        monstro = {
            "nome_monstro": "Sombra Faminta",
            "vida_monstro": 105,
            "dano_monstro": 35,
            "velocidade_monstro": 30,
            "defesa_monstro": 8,
            "xp_monstro": 130,
            "drop_moeda": 50,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "gorgona_mistica":
        monstro = {
            "nome_monstro": "Górgona Mística",
            "vida_monstro": 170,
            "dano_monstro": 32,
            "velocidade_monstro": 25,
            "defesa_monstro": 22,
            "xp_monstro": 175,
            "drop_moeda": 85,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "quimera_arcana":
        monstro = {
            "nome_monstro": "Quimera Arcana",
            "vida_monstro": 210,
            "dano_monstro": 38,
            "velocidade_monstro": 22,
            "defesa_monstro": 26,
            "xp_monstro": 210,
            "drop_moeda": 100,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "mago_corrompido":
        monstro = {
            "nome_monstro": "Mago Corrompido",
            "vida_monstro": 350,
            "dano_monstro": 45,
            "velocidade_monstro": 24,
            "defesa_monstro": 20,
            "xp_monstro": 500,
            "drop_moeda": 250,
            "drops_100_monstro": []
        }

    # ato 4 a cidade do caos 38 a 50 ↓

    elif entrada_monstro == "guarda_de_ferro":
        monstro = {
            "nome_monstro": "Guarda de Ferro",
            "vida_monstro": 220,
            "dano_monstro": 38,
            "velocidade_monstro": 12,
            "defesa_monstro": 42,
            "xp_monstro": 220,
            "drop_moeda": 80,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "sabujo_do_caos":
        monstro = {
            "nome_monstro": "Sabujo do Caos",
            "vida_monstro": 160,
            "dano_monstro": 42,
            "velocidade_monstro": 35,
            "defesa_monstro": 18,
            "xp_monstro": 200,
            "drop_moeda": 75,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "cavaleiro_negro":
        monstro = {
            "nome_monstro": "Cavaleiro Negro",
            "vida_monstro": 250,
            "dano_monstro": 45,
            "velocidade_monstro": 20,
            "defesa_monstro": 38,
            "xp_monstro": 260,
            "drop_moeda": 110,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "algoz_do_caos":
        monstro = {
            "nome_monstro": "Algoz do Caos",
            "vida_monstro": 200,
            "dano_monstro": 50,
            "velocidade_monstro": 28,
            "defesa_monstro": 22,
            "xp_monstro": 240,
            "drop_moeda": 100,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "feiticeiro_sombrio":
        monstro = {
            "nome_monstro": "Feiticeiro Sombrio",
            "vida_monstro": 180,
            "dano_monstro": 48,
            "velocidade_monstro": 24,
            "defesa_monstro": 20,
            "xp_monstro": 250,
            "drop_moeda": 120,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "demonio_de_fogo":
        monstro = {
            "nome_monstro": "Demônio de Fogo",
            "vida_monstro": 230,
            "dano_monstro": 46,
            "velocidade_monstro": 22,
            "defesa_monstro": 28,
            "xp_monstro": 280,
            "drop_moeda": 130,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "golem_de_sangue":
        monstro = {
            "nome_monstro": "Golem de Sangue",
            "vida_monstro": 300,
            "dano_monstro": 40,
            "velocidade_monstro": 10,
            "defesa_monstro": 35,
            "xp_monstro": 300,
            "drop_moeda": 140,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "general_de_elite":
        monstro = {
            "nome_monstro": "General de Elite",
            "vida_monstro": 280,
            "dano_monstro": 52,
            "velocidade_monstro": 24,
            "defesa_monstro": 40,
            "xp_monstro": 320,
            "drop_moeda": 180,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "comandante":
        monstro = {
            "nome_monstro": "Comandante",
            "vida_monstro": 320,
            "dano_monstro": 55,
            "velocidade_monstro": 26,
            "defesa_monstro": 45,
            "xp_monstro": 350,
            "drop_moeda": 220,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "dragao_de_sombras":
        monstro = {
            "nome_monstro": "Dragão de Sombras",
            "vida_monstro": 500,
            "dano_monstro": 65,
            "velocidade_monstro": 28,
            "defesa_monstro": 50,
            "xp_monstro": 800,
            "drop_moeda": 400,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "lorde_loop_f1":
        monstro = {
            "nome_monstro": "Lorde Loop (Fase 1)",
            "vida_monstro": 650,
            "dano_monstro": 70,
            "velocidade_monstro": 30,
            "defesa_monstro": 40,
            "xp_monstro": 1000,
            "drop_moeda": 0,
            "drops_100_monstro": []
        }
    elif entrada_monstro == "lorde_loop_f2":
        monstro = {
            "nome_monstro": "Lorde Loop (Fase 2)",
            "vida_monstro": 850,
            "dano_monstro": 85,
            "velocidade_monstro": 35,
            "defesa_monstro": 55,
            "xp_monstro": 2000,
            "drop_moeda": 1000,
            "drops_100_monstro": []
        }

    return monstro

    
     
def iniciar_jogo(nome_usuario, raca_personagem,vida,defesa,velocidade,mana,items_no_inv,fase): # Inicia o jogo 
    limpar()
    inicio_sessao = time.time() 
    
    print(f"--- INICIANDO A AVENTURA DE {nome_usuario.upper()} ---")
    print("Você acorda em uma floresta escura...")
    while True:
        entrada = input("-> ").strip().lower()

        if entrada == "/inv":
            exibir_inventario()

        elif entrada == "1" or entrada== "2":
            fase+=1

        elif entrada == "a":
            print(fase)

        elif entrada == "/help":
            exibir_help()
        elif entrada =="/raca":
             exibir_raca(raca_personagem)

        elif entrada == "/sair":
            fim_sessao = time.time()
            tempo_total = int(fim_sessao - inicio_sessao)  

            os.system("clear" if os.name != "nt" else "cls")


            horas = tempo_total // 3600
            minutos = (tempo_total % 3600) // 60
            segundos = tempo_total % 60
            
            print("Saindo do programa...")
            print(f"Obrigado por jogar, {nome_usuario}!")
            print(f"Tempo total da sua aventura: {horas}h {minutos}m {segundos}s")
            print(f"Fase final alcansada: {fase}")
            print(f"Nivel maximo alcansado: {nivel}")
            print(f"XP final alcansado: {xp}/100")
            break
            
        elif entrada == "/devs":
           exibir_devs()

        elif entrada == "/renick" and nome_usuario is not None:
                    nome_usuario = trocar_nickname(nome_usuario) 

        elif entrada == "/clear":
            os.system('cls' if os.name == 'nt' else 'clear')

        elif entrada == "/nick":
            print(f"Seu nick atual é: {nome_usuario}")    

        elif entrada == "/sts":
            exibir_status(nome_usuario,vida,defesa,velocidade,mana,items_no_inv,fase)

        elif entrada == "/start":
            print('Você não pode usar o comando "/start", o jogo já iniciou!')

        elif entrada=="/tabraca":
             exibir_tabeal_raca()

        else:
            print("Comando inválido! Digite /help para ver a lista de comandos.")
    return fase

def main(): # Parte do menu
    limpar()
    menu()
    
    nome_usuario = None
    while True:
        entrada = input("-> ").strip().lower()
        
        if entrada == "/help":
            exibir_help()
            
        elif entrada == "/start":
            nome_usuario = obter_nickname()
            raca_escolhida= obter_raca()
            vida,defesa,velocidade,mana=definir_atributos(raca_escolhida)
            iniciar_jogo(nome_usuario,raca_escolhida,vida,defesa,velocidade,mana,items_no_inv,fase)
            break 
            
        elif entrada == "/sair":
            print("Saindo do programa...")
            break

        elif entrada == "/devs":
            exibir_devs()

        elif entrada == "/renick" and nome_usuario == None:
                    print("Você não pode trocar um nome de usuário inexistente.")

        elif entrada == "/nick" and nome_usuario == None:
                    print("Você ainda não tem um nome de usuário.")

        elif entrada == "/clear":
            print('Você não pode usar o comando "/clear" no menu.')

        elif entrada == "/nick":
            print('Você ainda não tem um nick.')

        elif entrada == "/inv":
            print('Você não pode usar o comando "/inv" no menu.')

        elif entrada == "/sts":
            print('Você não pode usar o comando "/sts" no menu.')

        elif entrada == "/raca":
            print('Você não pode usar o comando "/raca" no menu.')

        elif entrada=="/tabraca":
             exibir_tabeal_raca()

        else:
            print("Comando inválido! Digite /help ou /start.")

if __name__ == "__main__":
    main()
