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

def raca_humano():
     vida=100
     velocidade=20
     defesa=20
     mana=0

def raca_elfo():
     vida=85
     defesa=12
     velocidade=25
     mana=60

def raca_anao():
     vida=130
     defesa=32
     velocidade=12
     mana=0

def raca_goblin():
     vida=70
     defesa=10
     velocidade=30
     mana=0

def raca_draconato():
     vida=115
     defesa=25
     velocidade=16
     mana=30
     

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
fase=0
# Atributos que mudam dependendo da raça ↓ 

vida = 0 # 100 é a vida base, dependendo da raça pode aumentar ou diminuir
velocidade = 0
defesa = 0 
mana = 0       


def exibir_inventario():
    print(f"Você tem {inventario} no seu inventário.")

def exibir_status(nome_usuario,vida,defesa,velocidade,mana):
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
            
def iniciar_jogo(nome_usuario, raca_personagem,vida,defesa,velocidade,mana): # Inicia o jogo 
    inicio_sessao = time.time() 
    
    print(f"--- INICIANDO A AVENTURA DE {nome_usuario.upper()} ---")
    print("Você acorda em uma floresta escura...")
    while True:
        entrada = input("-> ").strip().lower()

        if entrada == "/inv":
            exibir_inventario()
            
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
            exibir_status(nome_usuario,vida,defesa,velocidade,mana)

        elif entrada == "/start":
            print('Você não pode usar o comando "/start", o jogo já iniciou!')

        elif entrada=="/tabraca":
             exibir_tabeal_raca()

        else:
            print("Comando inválido! Digite /help para ver a lista de comandos.")


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
            iniciar_jogo(nome_usuario,raca_escolhida,vida,defesa,velocidade,mana)
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
