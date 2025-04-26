from random import randint
# Cores de Texto
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"  # Volta para a cor padrão

# Cores de fundo
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# Estilos
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

#obtem número de jogadores
def obter_num_jogadores():
    num_jogadores = 0
    while num_jogadores < 2:
        num_jogadores = int(input('Digite o número de jogadores: '))
        if num_jogadores < 2:
            print("Você precisa de no mínimo 2 jogadores")
    return num_jogadores

def obter_nomes_jogadores(num_jogadores):
    lista_jogadores = []
    for codigo in range(num_jogadores):
        nome = input(f'Escreva o nome do jogador {codigo+1}: ')
        jogador = [codigo, nome, [0, 0]]
        lista_jogadores.append(jogador)
    return lista_jogadores

#função colocar dados no copo
def colocar_dados_copo(copo):
    for i in range(6):
        copo.append(('C', 'P', 'C', 'T', 'P', 'C'))
    for i in range(4):
        copo.append(('T', 'P', 'C', 'T', 'P', 'C'))
    for i in range(3):
        copo.append(('T', 'P', 'T', 'C', 'P', 'T'))
    return copo

#função pegar dados
def pegar_dados_copo(copo):
    if len(copo) != 0:
        numero_dados = randint(0, len(copo)-1)
        dado = copo[numero_dados]
        del (copo[numero_dados])
        return dado, copo
    else:
        print('Copo Vazio!')
        return 0, copo

#função qual face do dado foi tirado
def lancar_dados(dado):
    face_dado = randint(0,5)
    if dado[face_dado] == 'C':
        print(f'{GREEN}Você tirou Cerebro!{RESET}')
        return 'C'
    elif dado[face_dado] == 'P':
        print(f'{YELLOW}Você tirou Passo!{RESET}')
        return 'P'
    elif dado[face_dado] == 'T':
        print(f'{RED}Você tirou Tiro!{RESET}')
        return 'T'

#Função sortear dados
def mostrar_dados(copo):
    lista_dado = []
    for dado in copo:
        if dado == ('C', 'P', 'C', 'T', 'P', 'C'):
            lista_dado.append('Verde')
        elif dado==('T', 'P', 'C', 'T', 'P', 'C'):
            lista_dado.append('Amarelo')
        elif dado==('T', 'P', 'T', 'C', 'P', 'T'):
            lista_dado.append('Vermelho')
    print(lista_dado)

#função qual dado foi tirado
def mostrar_cor_dado(dado):
    if dado == ('C', 'P', 'C', 'T', 'P', 'C'):
        print('Verde')
    elif dado == ('T', 'P', 'C', 'T', 'P', 'C'):
        print('Amarelo')
    elif dado == ('T', 'P', 'T', 'C', 'P', 'T'):
        print('Vermelho')

def pontuacao(primeiro_dado, segundo_dado, terceiro_dado):
    cerebro = 0
    passo = 0
    tiro = 0
    if primeiro_dado == 'C':
        cerebro += 1
    elif primeiro_dado == 'P':
        passo += 1
    elif primeiro_dado == 'T':
        tiro += 1

    if segundo_dado == 'C':
        cerebro += 1
    elif segundo_dado == 'P':
        passo += 1
    elif segundo_dado == 'T':
        tiro += 1

    if terceiro_dado == 'C':
        cerebro += 1
    elif terceiro_dado == 'P':
        passo += 1
    elif terceiro_dado == 'T':
        tiro += 1

    return cerebro, passo, tiro



from random import randint

print(f'{BG_RED}{WHITE}{BOLD} BEM VINDO AO JOGO ZOMBIE DICE!! {RESET}')
print(f'{BG_RED}{WHITE}=' * 33 + RESET)

num_jogadores = obter_num_jogadores()
lista_jogadores = obter_nomes_jogadores(num_jogadores)

#inicializando o copo de dados
copo = []
colocar_dados_copo(copo)
print('\n Vamos jogar!')


while True:
    for jogador in lista_jogadores:

#informando de qual jogador é a rodada
        mostrar_dados(copo)
        cod = jogador[0]
        nome = jogador[1]
        print(f'\n {CYAN}=== Vez do jogador: {nome} ==={RESET}')
        turno = True
        dado1 = True
        dado2 = True
        dado3 = True

        primeiro_dado = 0
        segundo_dado = 0
        terceiro_dado = 0

#sorteando dados
        while turno:
            print('Sorteando Dados')

            if dado1:
                primeiro_dado, copo = pegar_dados_copo(copo)

            if dado2:
                segundo_dado, copo = pegar_dados_copo(copo)

            if dado3:
                terceiro_dado, copo = pegar_dados_copo(copo)

#mostrando quais dados restaram no copo
            print('Mostrando dados restantes no copo: ')
            mostrar_dados(copo)

            primeira_face = ''
            segunda_face = ''
            terceira_face = ''

            if primeiro_dado != 0:
                primeira_face = lancar_dados(primeiro_dado)
            if segundo_dado != 0:
                segunda_face = lancar_dados(segundo_dado)
            if terceiro_dado != 0:
                terceira_face = lancar_dados(terceiro_dado)

#recolocando os dados no copo
            if len(copo)<3:
                esvaziar_copo = []
                copo = colocar_dados_copo(esvaziar_copo)
                mostrar_dados(copo)


            dado1 = True
            dado2 = True
            dado3 = True

            cerebro, passo, tiro = pontuacao(primeira_face, segunda_face, terceira_face)

            if passo>0:
                if primeira_face == 'P':
                    dado1 = False
                if segunda_face == 'P':
                    dado2 = False
                if terceira_face == 'P':
                    dado3 = False

            lista_jogadores[cod][2][0] = jogador[2][0] + cerebro
            lista_jogadores[cod][2][1] = jogador[2][1] + tiro

#mostrando placar
            print(f'{MAGENTA}Jogador:  {RESET}'+ lista_jogadores[cod][1])
            print(f'{GREEN}Cerebros: {RESET}' + str(lista_jogadores[cod][2][0]))
            print(f'{RED}Tiros: {RESET}' + str(lista_jogadores[cod][2][1]))

#Caso atinja a condição de 3 tiros ou mais, morre
            if lista_jogadores[cod][2][1] > 2:
                print(f'\n {BG_RED}{WHITE}{BOLD}BOOOOM! Você levou muitos tiros e morreu!!!{RESET}\n')
                lista_jogadores[cod][2][0] = 0
                lista_jogadores[cod][2][1] = 0
                esvaziar_copo = []
                copo = colocar_dados_copo(esvaziar_copo)
                mostrar_dados(copo)
                turno = False

#Caso atinja a condição de 3 cerebros ou mais, vence
            if lista_jogadores[cod][2][0] > 2:
                print(f'{BG_GREEN}{WHITE}{BOLD}PARABÉNS, ZUMBIE MESTRE! VOCÊ VENCEU!{RESET}\n')
                turno = False
                break


                print('FIM DE JOGO')
                print('=' * 14)

            # Caso o jogador queira continuar jogando
            if turno:
                continuar_turno = input('Deseja continuar jogando? (s/n)')
                if continuar_turno == 's':
                    continue

                if continuar_turno == "n":
                    lista_jogadores[cod][2][1] = 0
                    esvaziar_copo = []
                    copo = colocar_dados_copo(esvaziar_copo)
                    mostrar_dados(copo)
                    turno = False