## Função criar tabuleiro: Cria uma matriz de 3x3 que será a estrutura do tabuleiro
## Exemplo: folha de papel


def criar_tabuleiro():
    tabuleiro = [[" 1 "," 2 "," 3 "],
                 [" 4 "," 5 "," 6 "],
                 [" 7 "," 8 "," 9 "]
    ]
    return tabuleiro

## Função imprimir tabuleiro: Vai utilizar a variavel "tabuleiro" como parametro 
## para de fato imprimir as linhas do nosso tabuleiro Exemplo: o jogador desenha 
## os espaços na folha

def imprimir_tabuleiro(tabuleiro):
    print("\n") ##pula uma linha 

    print(f"{tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} | ") ## Coluna 0
    print("---+---+---") ## Linha horizontal

    print(f"{tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} | ") ## Coluna 1
    print("---+---+---") ## Linha horizontal
       
    print(f"{tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} | ") ## Coluna 2
    print("---+---+---")  ## Linha horizontal

    print("\n") ##pula uma linha 
    ## O f dentro do print serve para que possamos colocar as variaveis junto com a string
    ## Dentro das chaves temos o "Endereço" da das jogadas
    ## "|" são as linhas verticais

def fazer_jogada(jogador, tabuleiro):
        





