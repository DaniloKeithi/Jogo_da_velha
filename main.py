## Cria a função com o parametro "tabuleiro" que irá imprimir as linhas do tabuleiro na tela

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))

def verificar_vitoria(tabuleiro, jogador):

    ##laço de repetição que percorre a matriz e verifica se as condições de vitória são verdadeiras


    for i in range (3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador: ##linhas 
            return True
        
    for i in range (3):
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador: ## colunas
            return True
        
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador: ## diagonal \
            return True    
        
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador: ## diagonal /
            return True    

    return False    



def verificar_empate(tablueiro):
    for linha in tablueiro:
        for casa in linha:
            if casa not in ["X", "O"]:
                return False
    return True 
     


tabuleiro = [["1", "2", "3"],["4","5","6"], ["7","8","9"]] ##Cria uma lista de listas (matriz 3x3) para formar os espaços do tabuleiro



jogador_atual = "X" ## Cria o jogador que irá começar, no caso será sempre o X



for rodada in range(9):
    mostrar_tabuleiro(tabuleiro) 
    escolha = input(f"0 Jogador {jogador_atual}, escolha uma posição de (1-9): ")
    print("\n")
    posicao = int(escolha) - 1
    linha, coluna = posicao // 3, posicao % 3 ## basicamente nessa parte estamos pegando o valor da variavel
    ##"escolha" que recebe o valor da posição que o jogador deseja e colocando em outra variavel inteira
    ## na variavel linha atribuimos uma conta que pega o valor digitado -1 e faz a divisão exata por 3
    ## na variavel coluna atribuimis uma conta que pega o valor digitado -1 divide por 3 e pega o resto
    ## Exemplo: O jogador quer a posição 9. então 9-1 = 8 | linha: 8 // 3 = 2 | coluna: 8 % 3 sobra 2 | então linha 2 e coluna = 2 



    if tabuleiro[linha][coluna] in ["X", "O"]:
        print("Posição já está preenchida. Tente novamente")
        continue
    tabuleiro[linha][coluna] = jogador_atual



    if verificar_vitoria(tabuleiro, jogador_atual):
        mostrar_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual} venceu!")
        break


    if verificar_empate(tabuleiro):
        mostrar_tabuleiro(tabuleiro)
        print("Deu velha! O jogo empatou.")
        break


    if jogador_atual == "O":
        jogador_atual = "X" 
    else: 
        jogador_atual = "O"    



