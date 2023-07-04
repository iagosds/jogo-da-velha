tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
time = 'X' 

def prt(tab): #PRINTANDO O TABULEIRO
    for l in range(0, len(tab)):
        if l > 0:
            print('---|---|---')
        for c in range (0, len(tab[l])):
            if c <2:
                print("", tab[l][c], '|', end='')
            else:
                print(tab[l][c])

def play(tab, time):
    pos = int(input("Onde deseja jogar? [1-9] "))
    if pos >= 0 and pos <=3: #JOGANDO NA PRIMEIRA LINHA DO TABULEIRO
        if tab[0][pos - 1] == ' ': #DEFININDO SE É POSSÍVEL JOGAR NESSA POSIÇÃO OU NÃO
            tab[0][pos - 1] = time
        else:
            print("Jogada inválida")
            play(tabuleiro, time)

    elif pos > 3 and pos <=6: #JOGANDO NA SEGUNDA LINHA DO TABULEIRO
        if tab[1][pos-4] == ' ':
            tab[1][pos-4] = time
        else:
            print("Jogada inválida")
            play(tabuleiro, time)

    else: #JOGANDO NA TERCEIRA LINHA DO TABULEIRO
        if tab[2][pos-7] == ' ':
            tab[2][pos-7]=time
        else:
            print("Jogada inválida")
            play(tabuleiro, time)

def win(): #DEFININDO OS CASOS POSSÍVEIS DE VITÓRIA PARA QUALQUER TIME
    for l in range(0, len(tabuleiro)):
        for c in range(0, len(tabuleiro[l])):
            if tabuleiro[l][0]==time and tabuleiro[l][0]==tabuleiro[l][1] and tabuleiro[l][1] == tabuleiro[l][2]:
                return True
            elif tabuleiro[0][c] == time and tabuleiro[0][c]==tabuleiro[1][c] and tabuleiro[1][c]==tabuleiro[2][c]:
                return True
            elif tabuleiro[0][0]==time and tabuleiro[0][0]==tabuleiro[1][1] and tabuleiro[1][1]==tabuleiro[2][2]:
                return True
            elif tabuleiro[0][2]==time and tabuleiro[0][2]==tabuleiro[1][1] and tabuleiro[1][1]==tabuleiro[2][0]:
                return True
    return False

def velha(): #DEFININDO CENÁRIO ONDE NÃO HOUVE VITÓRIA
    cont = 0
    for l in range(0, len(tabuleiro)):
        for c in range(0, len(tabuleiro[l])):
            if tabuleiro[l][c]==' ':
                cont+=1
    if cont==0:
        print("O jogo terminou em velha! Tente novamente!")
        return True
    return False

while win()==False or velha():
    prt(tabuleiro)
    play(tabuleiro, time)
    win()
    if win():
        break #ENCERRANDO O JOGO EM CASO DE VITÓRIA
    if time =='X':
        time = 'O' #TROCA DE TIME/JOGADOR EXECUTADA EM TODA RODADA
    else:
        time = 'X'
    if velha():
        break # ENCERRANDO O JOGO EM CASO DE EMPATE
    
prt(tabuleiro)
if velha()==False:
    print("\nO '%s' ganhou! Parabéns"%time)