import tkinter as tk
import random
from tkinter import messagebox
class Jogador():
    def __init__(self,nome):
        self.nome = nome 
        self.escolhas = []
        self.embarcacao = 0
        self.contar_afundandas = 0
        self.acertos = {}
        self.campo = {}
        self.jogadas = {}
        self.tabuleiro = [[0] * 10 for _ in range(10)]
        self.botao = [[None] * 10 for _ in range(10)]
        self.frota = [ 
                        "S", "S", "S", "S",
                        ["P", "P", "P", "P"],   
                        ["D", "D", "D"], ["D", "D", "D"], 
                    ]
    

class BatalhaNaval:
    def __init__(self, master):
        self.master = master
        self.title_frame = tk.Frame(self.master)
        self.frame_tabuleiro = None  
        self.contador = 0
        self.frotas = ["1º Submarino", "2º Submarino", "3º Submarino",
                       "4º Submarino", "1º Porta-aviões", "1º Destróier", "2º Destróier"]
        self.tela()
        self.frames_da_tela()
        self.primeira_tela()
        
        
    def tela(self):
        self.master.title("Batalha Naval")
        self.master.geometry("900x500")
        self.master.configure(background="#1e3743")
        self.master.resizable(False, False)
        self.msg = tk.Label(self.master, text="Batalha Naval", font=("Arial", 16)).place(relx=0.4, rely=0.05)
    
    def escolher_posicoes(self):
        answer = messagebox.askyesno("Alerta", "Você está certo dos nomes?")
        if answer == 1:
            self.jogador1 =  Jogador("Jogador 1" if self.player1.get() == "" else self.player1.get())
            self.jogador2 =  Jogador("Jogador 2" if self.player2.get() == "" else self.player2.get())
            self.frame_1.destroy()
            self.segunda_tela()
            
    def horizontal(self, j: Jogador):
        j.escolhas.append("H")
        self.contador += 1
        j.embarcacao += 1
        self.frame_2.destroy()
        self.segunda_tela()
        
    def vertical(self, j: Jogador):
        j.escolhas.append("V")
        self.contador += 1
        j.embarcacao += 1
        self.frame_2.destroy()
        self.segunda_tela()
        
        
    def primeira_tela(self):
        #Tela de seleção de personagens
        # Primeiro jogador
        self.player1 = tk.Entry(self.frame_1)
        self.player1.place(relx=0.1, rely=0.2,)
        self.l1 = tk.Label(self.frame_1, text="Digite o nome do 1º Jogador")
        self.l1.place(relx=0.1, rely=0.05)
        # Segundo jogador 
        self.l2 = tk.Label(self.frame_1, text="Digite o nome do 2º Jogador")
        self.l2.place(relx=0.1, rely=0.35)
        self.player2 = tk.Entry(self.frame_1)
        self.player2.place(relx=0.1, rely=0.45)
        self.confirmar = tk.Button(self.frame_1, text="Confirmar", command=self.escolher_posicoes)
        self.confirmar.place(relx=0.33, rely=0.7)
        
    def segunda_tela(self):
        # Tela de posicionamento das peças 
        if self.contador == 14:
            self.contador = 0
            self.criar_campo(self.jogador1)
            self.criar_campo(self.jogador2)
            self.frame_3 = tk.Frame(self.master)
            self.frame_3.place(relx=0.1, rely=0.12, height=380, width=350)
            self.frame_4 = tk.Frame(self.master)
            self.frame_4.place(relx=0.5, rely=0.12, height=380, width=350)

            print("Acertos do primeiro jogador")
            print(self.jogador1.acertos)
            print("Acertos do segundo jogador")
            print(self.jogador2.acertos)
            messagebox.showinfo("Sucesso", "O jogo está pronto para começar")
            return self.terceira_tela()

        current_player = self.jogador2 if self.contador % 2 != 0 else self.jogador1

        self.frame_2 = tk.Frame(self.master)
        self.frame_2.place(relx=0.33, rely=0.2, height=200, width=200)
        
        self.l1 = tk.Label(self.frame_2, text=f"{current_player.nome}")
        self.l2 = tk.Label(self.frame_2, text="Selecione a Posição do seu o seu:")
        self.l3 = tk.Label(self.frame_2, text=f"{self.frotas[current_player.embarcacao]}")
        print(self.jogador1.embarcacao, self.jogador2.embarcacao)
        self.l1.place(relx=0.33, rely=0.1)
        self.l2.place(relx=0.02, rely=0.2)
        self.l3.place(relx=0.1, rely=0.3)
        
        self.h = tk.Button(self.frame_2, text="H", command=lambda: self.horizontal(current_player))
        self.v = tk.Button(self.frame_2, text="V", command=lambda: self.vertical(current_player))
        self.h.place(relx=0.4, rely=0.5)
        self.v.place(relx=0.6, rely=0.5)
        
    def habilitar_botoes(self, jog: Jogador):
        for x in range(10):
            for y in range(10):
                jog.botao[x][y].config(state="normal", fg="white")
                
    def encerrar_jogo(self):
        # Configura a tela final do jogo
        
        if self.jogador1.contar_afundandas == 13:
            messagebox.showinfo("Batalha Naval", "FIM DE JOGO!!!")
            for i in range(0,10):
                for j in range(0,10):
                    self.jogador2.botao[i][j].destroy()
                    if (i,j) in list(self.jogador2.acertos.keys()):
                        self.jogador2.botao[i][j] = tk.Button(self.frame_tabuleiro2, width=3,bg='Blue',
                                                              text=f"{self.jogador2.acertos[(i,j)]}", fg="yellow",)
                        self.jogador2.botao[i][j].grid(row=i + 1, column=j + 1)
                    else:
                        self.jogador2.botao[i][j] = tk.Button(self.frame_tabuleiro2, width=3,bg='Red',
                                                              text=f"X", fg="yellow",)
                        self.jogador2.botao[i][j].grid(row=i + 1, column=j + 1)
                    
            self.t1.destroy()
            self.t2.destroy()
            self.t1 = tk.Label(self.frame_3, text=f"Você Ganhou!!!")
            self.t2 = tk.Label(self.frame_4, text=f"Você Perdeu!!!")
            self.t1.place(relx=0.35, rely=0.08)
            self.t2.place(relx=0.35, rely=0.08)
        if self.jogador2.contar_afundandas == 13:
            messagebox.showinfo("Batalha Naval", "FIM DE JOGO!!!")
            for i in range(0,10):
                for j in range(0,10):
                    self.jogador1.botao[i][j].destroy()
                    if (i,j) in list(self.jogador1.acertos.keys()):
                        self.jogador1.botao[i][j] = tk.Button(self.frame_tabuleiro1, width=3,bg='Blue',
                                                              text=f"{self.jogador1.acertos[(i,j)]}", fg="yellow",)
                        self.jogador1.botao[i][j].grid(row=i + 1, column=j + 1)
                    else:
                        self.jogador1.botao[i][j] = tk.Button(self.frame_tabuleiro1, width=3,bg='Red',
                                                              text=f"X", fg="yellow",)
                        self.jogador1.botao[i][j].grid(row=i + 1, column=j + 1)
            self.t1.destroy()
            self.t2.destroy()
            self.t2 = tk.Label(self.frame_3, text=f"Você Ganhou!!!")
            self.t1 = tk.Label(self.frame_4, text=f"Você Perdeu!!!")
            self.t2.place(relx=0.35, rely=0.08)
            self.t1.place(relx=0.35, rely=0.08)
            


    def atirar(self, i, j, jog: Jogador):
        self.contador += 1
        p1 = i - 1
        p2 = j - 1
        if jog.tabuleiro[p1][p2] != 1:
            if (p1,p2) not in list(jog.jogadas.keys()):
                jog.tabuleiro[p1][p2] = 1  # Marca como atingido
                if (p1,p2) in list(jog.acertos.keys()):
                    jog.jogadas[(p1,p2)] = jog.acertos[(p1, p2)]
                    jog.botao[p1][p2].config(bg='Blue', text=f"{jog.acertos[(p1,p2)]}", fg="yellow")
                    jog.contar_afundandas += 1
                else:
                    jog.tabuleiro[p1][p2] = 1  # Marca como atingido
                    jog.botao[p1][p2].config(bg='red', text='X', fg="yellow")
                    jog.jogadas[(p1,p2)] = "X"
                
            for x in range(0,10):
                for y in range(0,10):
                    jog.botao[x][y].config(state="disabled", fg="green")
                    
            if jog == self.jogador1:
                self.habilitar_botoes(self.jogador2)
            else:
                self.habilitar_botoes(self.jogador1)
            self.atualizar_titulos()
        else:
            messagebox.showinfo("Batalha Naval", "Você já atirou aqui!")
        self.encerrar_jogo()
        
        
        
            
            
    def mostrar_tabuleiro(self, jog: Jogador, frame_tabuleiro):

        for i in range(0, 11):
            for j in range(0, 11):
                p1 = i - 1
                p2 = j - 1
                
                if i == 0 and j == 0:
                    continue  
                elif i == 0 or j == 0:
                    tk.Label(frame_tabuleiro, text=f"{p1 if i != 0 else p2}").grid(row=i, column=j)
                else:
                    # Cria botões
                    jog.botao[p1][p2] = tk.Button(frame_tabuleiro, text=f" ", width=3,
                                                    command=lambda i=i, j=j: self.atirar(i, j, jog))
                    jog.botao[p1][p2].grid(row=i, column=j)
                
    def atualizar_titulos(self):
        if self.t1 is not None or self.t2 is not  None:
            self.t1.destroy()
            self.t2.destroy()
        self.t1 = tk.Label(self.frame_3, text=f"Restam {13 - self.jogador1.contar_afundandas} Embarcações para serem destruídas")
        self.t1.place(relx=0.05, rely=0.08)
        self.t2 = tk.Label(self.frame_4, text=f"Restam {13 - self.jogador2.contar_afundandas} Embarcações para serem destruídas")
        self.t2.place(relx=0.05, rely=0.08)
        
        
    def terceira_tela(self):
        self.t1 = None
        self.t2 = None
        self.l1 = tk.Label(self.frame_3, text=f"{self.jogador1.nome}")
        self.l1.place(relx=0.4, rely=0.02)
        self.frame_botoes = tk.Frame(self.frame_3)
        self.frame_botoes.place(relx=0.33, rely=0.9)
        self.reset1 = tk.Button(self.frame_botoes, text="Resetar", command=self.resetar_tabuleiro).grid(row=0, column=0, padx=10)
        self.sair2 = tk.Button(self.frame_botoes, text="Sair", command=self.master.destroy).grid(row=0, column=1, padx=10)
        self.frame_tabuleiro1 = tk.Frame(self.frame_3)
        self.frame_tabuleiro1.place(relx=0.02, rely=0.15)
        self.mostrar_tabuleiro(self.jogador1, self.frame_tabuleiro1)
        
        # Tela do Jogador 2
        self.l1 = tk.Label(self.frame_4, text=f"{self.jogador2.nome}")
        self.l1.place(relx=0.4, rely=0.02)
        self.frame_botoes = tk.Frame(self.frame_4)
        self.frame_botoes.place(relx=0.33, rely=0.9)
        self.reset1 = tk.Button(self.frame_botoes, text="Resetar", command=self.resetar_tabuleiro).grid(row=0, column=0, padx=10)
        self.sair2 = tk.Button(self.frame_botoes, text="Sair", command=self.master.destroy).grid(row=0, column=1, padx=10)
        self.frame_tabuleiro2 = tk.Frame(self.frame_4)
        self.frame_tabuleiro2.place(relx=0.02, rely=0.15)
        self.atualizar_titulos()
        self.mostrar_tabuleiro(self.jogador2, self.frame_tabuleiro2)
        
    
        
    def criar_campo(self, jog: Jogador):
        jog.campo = {}
        jog.acertos = {}
        jog.embarcacao = 0
        print(jog.embarcacao)

        for barco in jog.frota:
            placed = False
            while not placed:
                p1 = random.randint(0, 9)
                p2 = random.randint(0, 9)

                if jog.escolhas[jog.embarcacao] == "H":  # Horizontal
                    if p2 + len(barco) <= 10:  # Garantindo que o tamanho esteja correto
                        if all(jog.tabuleiro[p1][p2 + k] == 0 for k in range(len(barco))):
                            for k in range(len(barco)):
                                jog.tabuleiro[p1][p2 + k] = barco[k]
                                jog.acertos[(p1, p2 + k)] = barco[k]
                            placed = True

                elif jog.escolhas[jog.embarcacao] == "V":  # Vertical
                    if p1 + len(barco) <= 10:  # Garantindo que o tamanho esteja correto
                        if all(jog.tabuleiro[p1 + k][p2] == 0 for k in range(len(barco))):
                            for k in range(len(barco)):
                                jog.tabuleiro[p1 + k][p2] = barco[k]
                                jog.acertos[(p1 + k, p2)] = barco[k]
                            placed = True

            jog.embarcacao += 1
        
        
        
    def frames_da_tela(self):
        self.frame_1 = tk.Frame(self.master)
        self.frame_1.place(relx=0.33, rely=0.2, height=200, width=200)

        
        
    def resetar_tabuleiro(self):
        # Reinicia o tabuleiro
        answer = messagebox.askyesno("Alerta", "Começar o jogo do início?")
        self.jogador1
        if answer == 1:
            self.contador = 0
            self.frame_3.destroy()
            self.frame_4.destroy()
            self.tela()
            self.frames_da_tela()
            self.primeira_tela()

def main():
    root = tk.Tk()
    BatalhaNaval(root)
    root.mainloop()

if __name__ == "__main__":
    main()