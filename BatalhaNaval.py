import random
import itertools
random.seed(42)
class CriarJogo():
    cor_id = itertools.count(1)
    ## Constructor do tabuleiro
    def __init__(self, name):
        self.cor = next(self.cor_id)
        self.name = name 
        self.fim = False
        self.dificuldade = 10
        self.afundadas = {}
        self.acertos = {}
        self.campo = {}
        self.jogadas = {}
        frota = [["P", "P", "P", "P"],
                 ["D", "D", "D"], ["D", "D", "D"], ["D", "D", "D"], 
                 "S", "S", "S", "S"  ]
        tam_frota = len(frota)
        c = 0
        # Seleciona aleatoriamente um local no tabuleiro para cada peça 
        while c != tam_frota: 
            i = random.randint(0, self.dificuldade- 1)
            j = random.randint(0, self.dificuldade- 1)
            campo_escolhido = [i,j]
            # Veriica se o campo aleatório escolhido já foi adicionado em acertos
            if (campo_escolhido not in list(self.acertos.keys())):
                if (frota[c][0] == "D"):
                        sentido = input(f'\033[3{self.cor}m{self.name}\033[0m, selecione a sentido do Destróier [H] ou [V]? ').upper()
                        tam_barco = len(frota[c])
                        peca = 0
                        if sentido == "H" and j <= 3 and (i,j) not in list(self.acertos.keys()) :
                            while tam_barco != peca: 
                                self.acertos[i,j] = frota[c][peca]
                                j += 1
                                peca += 1
                            c += 1
                        elif sentido == "H" and j > 3 and (i,j) not in list(self.acertos.keys()):
                            while tam_barco != peca: 
                                self.acertos[i,j] = frota[c][peca]
                                j -= 1
                                peca += 1
                            c += 1
                        if sentido == "V" and i <= 3 and (i,j) not in list(self.acertos.keys()) :
                            while tam_barco != peca: 
                                self.acertos[i,j] = frota[c][peca]
                                i += 1
                                peca += 1
                            c += 1
                        elif sentido == "V" and i > 3 and (i,j) not in list(self.acertos.keys()):
                            while tam_barco != peca: 
                                self.acertos[i,j] = frota[c][peca]
                                i -= 1
                                peca += 1
                            c += 1
                elif (frota[c][0] == "P"):
                        sentido = input(f'\033[3{self.cor}m{self.name}\033[0m, selecione a sentido do Porta-Aviões [H] ou [V]? ').upper()     
                        tam_barco = len(frota[c])
                        peca = 0
                        if sentido == "H" and j <= 3 and (i,j) not in list(self.acertos.keys()) :
                            while tam_barco != peca: 
                                self.acertos[i,j] = frota[c][peca]
                                j += 1
                                peca += 1
                            c += 1
                        elif sentido == "H" and j > 3 and (i,j) not in list(self.acertos.keys()):
                            while tam_barco != peca: 
                                self.acertos[i,j] = frota[c][peca]
                                j -= 1
                                peca += 1
                            c += 1
                        if sentido == "V" and i <= 3 and (i,j) not in list(self.acertos.keys()) :
                            while tam_barco != peca: 
                                self.acertos[i,j] = frota[c][peca]
                                i += 1
                                peca += 1
                            c += 1
                        elif sentido == "V" and i > 3 and (i,j) not in list(self.acertos.keys()):
                            while tam_barco != peca: 
                                self.acertos[i,j] = frota[c][peca]
                                i -= 1
                                peca += 1
                            c += 1
                elif frota[c][0] == "S" and (i,j) not in list(self.acertos.keys()):
                    self.acertos[i,j] = frota[c]
                    c += 1
        ## Cria tabuleiro 
        for i in range(0, self.dificuldade):
            for j in range(0, self.dificuldade):
                if [i,j] in list(self.acertos.keys()):
                    self.campo[i,j] = self.acertos[i,j]
                else:
                    self.campo[i,j] = " "
    # Verifica se a jogada do usuário acertou alguma embarcação
    # e adiciona a jogada ao tabuleiro
    def mostrarAlvo(self, p1, p2):
        alvo = (p1, p2)
        # for acerto in self.acertos.keys():
        if alvo in list(self.acertos.keys()): 
            self.campo[alvo[0], alvo[1]] = "O"
            return "O"
        else:
            self.campo[(alvo[0], alvo[1])] = "X"
            return "X"
    # Mostra uma representação visual do tabuleiro
    def mostrarCampo(self):
        print("Formato atual da Partida")
        print("------------------------")
        for i in range(self.dificuldade + 1):
            for j in range(self.dificuldade + 1):
                if (i - 1, j - 1) not in list(self.jogadas.keys()):
                    if i == 0 and j > 0:
                        print(f'\033[33m{j - 1}|\033[0m', end='')
                    elif j == 0 and i > 0:
                        print(f'\033[33m{i - 1}|\033[0m', end='')
                    else:
                        print(f'{"\033[33m |\033[0m"}', end='')
                else:
                    if self.campo[i - 1,j - 1] == " ":
                        print(f'[0m\033[33m |\033[0m', end='')
                    elif self.campo[i - 1,j - 1] == "X":
                        print(f'\033[31m{self.campo[i - 1,j - 1]}\033[0m\033[33m|\033[0m', end='')
                    elif self.campo[i - 1,j - 1] == "O":
                        print(f'\033[32m{self.campo[i - 1,j - 1]}\033[0m\033[33m|\033[0m', end='')
                    # print(f'{self.campo[i][j]}', end='')
            print()
        print("------------------------")
    # Mostra todas as peças do jogador perdedor
    def MostrarPosicoes(self):
        print("------------------------")
        for i in range(self.dificuldade + 1):
            for j in range(self.dificuldade + 1):
                if (i - 1, j - 1) not in list(self.jogadas.keys()):
                    if i == 0 and j > 0:
                        print(f'\033[33m{j - 1}|\033[0m', end='')
                    elif j == 0 and i > 0:
                        print(f'\033[33m{i - 1}|\033[0m', end='')
                    elif (i - 1, j - 1) not in list(self.afundadas.keys()) and (i - 1, j - 1)  in list(self.acertos.keys()) :
                        print(f"\033[36m{self.acertos[i - 1, j - 1]}\033[0m|", end='')
                    else:
                        print(f'\033[33m |\033[0m', end='')
                else:
                    if (i - 1, j - 1) in list(self.jogadas.keys()) and self.jogadas[i - 1,j - 1] == "X":
                        print(f'\033[31m{self.campo[i - 1,j - 1]}\033[0m\033[33m|\033[0m', end='')
                    elif (i - 1, j - 1) in list(self.jogadas.keys()) and self.jogadas[i - 1,j - 1] == "O":
                        print(f'\033[32m{self.campo[i - 1,j - 1]}\033[0m\033[33m|\033[0m', end='')
            print()
        print("------------------------")
    
    def realizarJogada(self, p1, p2):
        # Verificação para saber se a jogada é válida ou não
        if [p1, p2] not in [[i,j] for i in range(self.dificuldade) for j in range(self.dificuldade)] \
            or self.jogadas.get((p1, p2)) != None :

            print("Nenhuma modificação foi feita: Jogada inválida")
            entrada = input(f"\033[3{self.cor}m{self.name}\033[0m: por favor \033[31mREFAÇA\033[0m  Faça sua jogada: ")
            p1, p2 = map(int  , entrada.split())
            return self.realizarJogada(p1, p2) 
        # Caso a jogada seja válida a jogada será adicionada ao tabuleiro
        else:
            self.campo[p1, p2] = f"\033[32m{self.mostrarAlvo(p1,p2)}\033[0m"
            self.jogadas[(p1,p2)] = self.mostrarAlvo(p1,p2)
            #Verifica se o jogador acertou uma embarção ou não
            if (p1,p2) in list(self.acertos.keys()):
                self.afundadas[(p1,p2)] = self.acertos[(p1,p2)]
                self.jogadas[(p1,p2)] = self.mostrarAlvo(p1,p2)
                self.mostrarCampo()
                # Caso o jogador vença a partida, esse código terminará a jogo
                if self.afundadas == self.acertos:
                    self.fim = True
                    print("\033[32m-----FIM DE JOGO!!!-----\033[0m")
                    self.mostrarCampo()
                    print(f"🥇 O \033[3{self.cor}m{self.name}\033[0m Venceu!!!")
                    return ...
                print("🟢 Você acertou uma embarcação do seu adversário")
                entrada = input(f"\033[3{self.cor}m{self.name}\033[0m: por favor, \033[32mREFAÇA\033[0m  Faça sua jogada: ")
                p1, p2 = map(int  , entrada.split())
                
                return self.realizarJogada(p1, p2)
            # Retorno que aparece quando o jogador não acertar a embarcação 
            else:
                print()
                print("❌ O seu adversário não acertou nenhuma embarcação")

                    
                
        
jogador_1 = CriarJogo("Jogador 1")
jogador_2 = CriarJogo("Jogador 2")
jogar_novamente = "S"
print("\033[32m-----INÍCIO DA PARTIDA-----\033[0m")

while jogar_novamente != "N":
    jogador_1.mostrarCampo()
    entrada = input(f"\033[3{jogador_1.cor}m{jogador_1.name}\033[0m, faça sua jogada: ")
    p1, p2 = map(int  , entrada.split())
    jogador_1.realizarJogada(p1, p2)
    #Verificar se o jogador 1 ganhou o jogo
    if jogador_1.fim:
        jogador_2.MostrarPosicoes()
        jogar_novamente = input("Deseja jogar novamente? Presione \033[31m[N]\033[0m para não jogar: ").upper()
        if jogar_novamente == "N":
            break
        else:
            jogar_novamente = "S"
        jogador_1 = CriarJogo("Jogador 1")
        jogador_2 = CriarJogo("Jogador 2")
    
    jogador_2.mostrarCampo()
    entrada = input(f"\033[3{jogador_2.cor}m{jogador_2.name}\033[0m faça sua jogada: ")
    p3, p4 = map(int  , entrada.split())
    jogador_2.realizarJogada(p3, p4)
    #Verificar se o jogador 1 ganhou o jogo
    if jogador_2.fim:
        jogador_1.MostrarPosicoes()
        jogar_novamente = input("Deseja jogar novamente? Presione \033[31m[N]\033[0m para não jogar: ").upper()
        if jogar_novamente == "N":
            break
        else:
            jogar_novamente = "S"
        jogador_1 = CriarJogo("Jogador 1")
        jogador_2 = CriarJogo("Jogador 2")
