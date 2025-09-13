def inicializar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas e colunas
    for i in range(3):
        if all([celula == jogador for celula in tabuleiro[i]]):
            return True
        if all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    # Verifica diagonais
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or \
       all([tabuleiro[i][2 - i] == jogador for i in range(3)]):
        return True
    return False

def verificar_empate(tabuleiro):
    return all(cell != " " for row in tabuleiro for cell in row)

def jogar():
    tabuleiro = inicializar_tabuleiro()
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")
        
        try:
            linha = int(input("Escolha a linha (0, 1 ou 2): "))
            coluna = int(input("Escolha a coluna (0, 1 ou 2): "))
        except ValueError:
            print("Entrada inválida. Use apenas números.")
            continue

        if linha not in range(3) or coluna not in range(3):
            print("Posição inválida! Tente novamente.")
            continue

        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já está ocupada! Tente outra.")
            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

# Iniciar o jogo
jogar()
