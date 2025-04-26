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


# Obtém número de jogadores
def obter_num_jogadores():
    return 3

def obter_nomes_jogadores(num_jogadores):
    #lista_jogadores = []
    # Usando nomes fixos
    nomes = ["João", "Maria", "Pedro"]
    return [[codigo, nomes[codigo], [0, 0]] for codigo in range(num_jogadores)]


# Função colocar dados no copo
def colocar_dados_copo():
    copo = []
    copo.extend([('C', 'P', 'C', 'T', 'P', 'C') for _ in range(6)])  # Verdes
    copo.extend([('T', 'P', 'C', 'T', 'P', 'C') for _ in range(4)])  # Amarelos
    copo.extend([('T', 'P', 'T', 'C', 'P', 'T') for _ in range(3)])  # Vermelhos
    return copo

# Função pegar dados
def pegar_dados_copo(copo):
    if len(copo) == 0:
        return colocar_dados_copo()[0], colocar_dados_copo()
    index = randint(0, len(copo)-1)
    dado = copo.pop(index)
    return dado, copo


# Função qual face do dado foi tirado
def lancar_dados(dado):
    face = randint(0, 5)
    resultado = dado[face]

    if resultado == 'C':
        print(f"{GREEN}Você tirou Cerebro!{RESET}")
    elif resultado == 'P':
        print(f"{YELLOW}Você tirou Passo!{RESET}")
    elif resultado == 'T':
        print(f"{RED}Você tirou Tiro!{RESET}")

    return resultado


# Função mostrar dados no copo
def mostrar_dados(copo):
    cores = []
    for dado in copo:
        if dado == ('C', 'P', 'C', 'T', 'P', 'C'):
            cores.append("Verde")
        elif dado == ('T', 'P', 'C', 'T', 'P', 'C'):
            cores.append("Amarelo")
        elif dado == ('T', 'P', 'T', 'C', 'P', 'T'):
            cores.append("Vermelho")
    print(f"Dados no copo: {cores}")


def pontuacao(faces):
    cerebro = faces.count('C')
    passo = faces.count('P')
    tiro = faces.count('T')
    return cerebro, passo, tiro


def verificar_vitoria(jogadores):
    for jogador in jogadores:
        if jogador[2][0] >= 13:
            return True
    return False


def jogar_rodada(jogador, copo):
    print(f"\n{CYAN}=== Vez do jogador: {jogador[1]} ==={RESET}")

    dados_rodada = []
    faces_rodada = []
    tiros_rodada = 0

    # Pega 3 dados iniciais
    for _ in range(3):
        dado, copo = pegar_dados_copo(copo)
        dados_rodada.append(dado)

    # Lança os dados
    for dado in dados_rodada:
        face = lancar_dados(dado)
        faces_rodada.append(face)
        if face == 'T':
            tiros_rodada += 1

    # Calcula pontos
    cerebros, passos, tiros = pontuacao(faces_rodada)
    jogador[2][0] += cerebros
    jogador[2][1] += tiros

    # Verifica se morreu (3+ tiros)
    if jogador[2][1] >= 3:
        print(f"{BG_RED}{WHITE} BOOOOM! Você levou muitos tiros e morreu! {RESET}")
        jogador[2][0] = 0  # Perde todos os cérebros
        jogador[2][1] = 0  # Reseta os tiros

    # Mostra placar
    print(f"\n{MAGENTA}Placar:{RESET}")
    print(f"{GREEN}Cérebros: {jogador[2][0]}{RESET}")
    print(f"{RED}Tiros: {jogador[2][1]}{RESET}")

    return copo


def main():# Início do jogo
    print(f'\n{BG_RED}{WHITE}{BOLD} BEM VINDO AO JOGO ZOMBIE DICE!! {RESET}')
    print(f'{BG_RED}{WHITE}=' * 33 + RESET)

    num_jogadores = obter_num_jogadores()
    jogadores = obter_nomes_jogadores(num_jogadores)
    copo = colocar_dados_copo()

    rodada = 1
    while True:
        print(f"\n{BG_BLUE}{WHITE} RODADA {rodada} {RESET}")

        for jogador in jogadores:
            copo = jogar_rodada(jogador, copo)

            if verificar_vitoria(jogadores):
                vencedores = [j for j in jogadores if j[2][0] >= 13]
                print(
                    f"\n{BG_GREEN}{WHITE}{BOLD} PARABÉNS {', '.join([v[1] for v in vencedores])}, VOCÊ(S) VENCEU(AM)! {RESET}")
                print("\nPlacar Final:")
                for j in jogadores:
                    print(f"{j[1]}: {GREEN}{j[2][0]} cérebros{RESET} | {RED}{j[2][1]} tiros{RESET}")
            return
        rodada += 1

if __name__ == "__main__":
    main()