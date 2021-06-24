from tkinter import *
import tkinter as tk
import  IA
import random  
import threading
jogador_estado = 0

vator_botoes = [
    ["","",""],
    ["","",""],
    ["","",""]
    ]

#vetor que controla X e 0 a aprtir de qual 
#estado o usuario estava ao precionar o botao
vetor_de_Vitoria = [
    ["","",""],
    ["","",""],
    ["","",""]
    ]



cor_botao = '#%02x%02x%02x' % (64, 204, 208)

class Jogo(threading.Thread):        
        
    def __init__(self):
        threading.Thread.__init__(self)
        janela = tk.Tk()
        janela.geometry("420x480+200+200")
        
        self.bt_1 = Button(janela,  width = 15 , height = 10, text="", bg = cor_botao,command=lambda: self.mudaBotao('bt_1'))
        self.bt_1.place(x=0,y=0)
        
        self.bt_2 = Button(janela,  width = 15 , height = 10, text="" ,bg = cor_botao, command=lambda: self.mudaBotao('bt_2'))
        self.bt_2.place(x=140,y=0)
        self.bt_3 = Button(janela,  width = 15 , height = 10, text="" , bg = cor_botao,command=lambda: self.mudaBotao('bt_3'))
        self.bt_3.place(x=280,y=0)
        
        self.bt_4 = Button(janela,  width = 15 , height = 10, text="" ,bg = cor_botao, command=lambda: self.mudaBotao('bt_4'))
        self.bt_4.place(x=0,y=130)
        self.bt_5 = Button(janela,  width = 15 , height = 10, text="" , bg = cor_botao,command=lambda: self.mudaBotao('bt_5'))
        self.bt_5.place(x=140,y=130)
        self.bt_6 = Button(janela,  width = 15 , height = 10, text="" ,bg = cor_botao, command=lambda: self.mudaBotao('bt_6'))
        self.bt_6.place(x=280,y=130)
        
        
        self.bt_7 = Button(janela,  width = 15 , height = 10, text="" , bg = cor_botao, command=lambda: self.mudaBotao('bt_7'))
        self.bt_7.place(x=0,y=260)
        self.bt_8 = Button(janela,  width = 15 , height = 10, text="" , bg = cor_botao,command=lambda: self.mudaBotao('bt_8'))
        self.bt_8.place(x=140,y=260)
        self.bt_9 = Button(janela,  width = 15 , height = 10, text="" , bg = cor_botao,command=lambda: self.mudaBotao('bt_9'))
        self.bt_9.place(x=280,y=260)
        
        self.bt_reinicia = Button(janela, width=15 , text="Reinicia" , bg = 'red',command=lambda: self.zeraJogo())
        self.bt_reinicia.place(x=140,y=400)
        
        self.bt_inicia = Button(janela, width=15 , text="2 IA" , bg = 'red',command=lambda: (threading.Thread(target = self.iniciar).start()))
        self.bt_inicia.place(x=140,y=430)
        
        janela.title("Jogo da Velha")
        
        janela.mainloop()
        
    def jogador(self,bt):
        global jogador_estado
        
        if jogador_estado == 0:
            
            jogador_estado = 1
        
        else:
            jogador_estado = 0
        
        
        
        
        
    
    def lanceIa(self):
       
       global vetor_de_Vitoria
       Posicao = []
       for i in range(3):
        
             for j in range(3):
            
                 if vetor_de_Vitoria[i][j] == "":
                
                     Posicao.append([i,j])
        
       if Posicao == []:
             
             self.fimJogo()
             
       
       [a,b] = IA.movimentoIa(self,vetor_de_Vitoria, jogador_estado)
       
       if a == None  and b == None:
           self.fimJogo()
           
       self.verifica_jogada_IA(a,b)
        
       self.VerificaVitori()
       
    def verifica_jogada_IA(self, a ,b):
       
       if a ==0 and b==0:
           vator_botoes[0][0] = 'bt_1'
           vetor_de_Vitoria[0][0] = jogador_estado
           if jogador_estado==0:
                self.bt_1["text"] = 'X'
           else:
                self.bt_1["text"] = 'O'
           self.jogador('bt')
           
       if a ==0 and b==1:
           vator_botoes[0][1] = 'bt_2'
           vetor_de_Vitoria[0][1] = jogador_estado
           if jogador_estado==0:
                self.bt_2["text"] = 'X'
           else:
                self.bt_2["text"] = 'O'
           self.jogador('bt')
       if a ==0 and b==2:
           vator_botoes[0][2] = 'bt_3'
           vetor_de_Vitoria[0][2] = jogador_estado
           if jogador_estado==0:
                self.bt_3["text"] = 'X'
           else:
                self.bt_3["text"] = 'O'
           self.jogador('bt')
       if a ==1 and b==0:
           vator_botoes[1][0] = 'bt_4'
           vetor_de_Vitoria[1][0] = jogador_estado
           if jogador_estado==0:
                self.bt_4["text"] = 'X'
           else:
                self.bt_4["text"] = 'O'
           self.jogador('bt')
       if a ==1 and b==1:
           vator_botoes[1][1] = 'bt_5'
           vetor_de_Vitoria[1][1] = jogador_estado
           if jogador_estado==0:
                self.bt_5["text"] = 'X'
           else:
                self.bt_5["text"] = 'O'
           self.jogador('bt')
       
       if a ==1 and b==2:
           vator_botoes[1][2] = 'bt_6'
           vetor_de_Vitoria[1][2] = jogador_estado
           if jogador_estado==0:
                self.bt_6["text"] = 'X'
           else:
                self.bt_6["text"] = 'O'
           self.jogador('bt')
       if a ==2 and b==0:
           vator_botoes[2][0] = 'bt_7'
           vetor_de_Vitoria[2][0] = jogador_estado
           if jogador_estado==0:
                self.bt_7["text"] = 'X'
           else:
                self.bt_7["text"] = 'O'
           self.jogador('bt')
       if a ==2 and b==1:
           vator_botoes[2][1] = 'bt_8'
           vetor_de_Vitoria[2][1] = jogador_estado
           if jogador_estado==0:
                self.bt_8["text"] = 'X'
           else:
                self.bt_8["text"] = 'O'
           self.jogador('bt')
       if a ==2 and b==2:
           vator_botoes[2][2] = 'bt_9'
           vetor_de_Vitoria[2][2] = jogador_estado
           if jogador_estado==0:
                self.bt_9["text"] = 'X'
           else:
                self.bt_9["text"] = 'O'
           self.jogador('bt')
    
    def iniciar (self):
        
        vetor = [[0,0],[0,1],[0,2],
         [1,0],[1,1],[1,2],
         [2,0],[2,1],[2,2]
         ]
        a = random.choice(vetor)
        
        self.verifica_jogada_IA(a[0],a[1])
        
        global vetor_de_Vitoria
        Posicao = []
        for i in range(3):
        
             for j in range(3):
            
                 if vetor_de_Vitoria[i][j] == "":
                
                     Posicao.append([i,j])
        
        
             
        while Posicao != []:
            Posicao = []
            for i in range(3):
        
             for j in range(3):
            
                 if vetor_de_Vitoria[i][j] == "":
                
                     Posicao.append([i,j])
            self.lanceIa()
        
        
    def fimJogo(self):
        
        self.bt_1.config(state = DISABLED) 
        self.bt_2.config(state = DISABLED) 
        self.bt_3.config(state = DISABLED)
        self.bt_4.config(state = DISABLED)
        self.bt_5.config(state = DISABLED)
        self.bt_6.config(state = DISABLED)
        self.bt_7.config(state = DISABLED)
        self.bt_8.config(state = DISABLED)
        self.bt_9.config(state = DISABLED)
    
    def zeraJogo(self):
        global vetor_de_Vitoria
        global vator_botoes
        self.bt_1["text"] = ''
        self.bt_2["text"] = ''
        self.bt_3["text"] = ''
        self.bt_4["text"] = ''
        self.bt_5["text"] = ''
        self.bt_6["text"] = ''
        self.bt_7["text"] = ''
        self.bt_8["text"] = ''
        self.bt_9["text"] = ''
        vetor_de_Vitoria = [
                ["","",""],
                ["","",""],
                ["","",""]
                ]
        vator_botoes = [
                ["","",""],
                ["","",""],
                ["","",""]
                ]
        self.bt_1.config(state = "normal") 
        self.bt_2.config(state = "normal") 
        self.bt_3.config(state = "normal")
        self.bt_4.config(state = "normal")
        self.bt_5.config(state = "normal")
        self.bt_6.config(state = "normal")
        self.bt_7.config(state = "normal")
        self.bt_8.config(state = "normal")
        self.bt_9.config(state = "normal")
        
        self.bt_1.configure(bg=cor_botao)
        self.bt_2.configure(bg=cor_botao)
        self.bt_3.configure(bg=cor_botao)
        self.bt_4.configure(bg=cor_botao)
        self.bt_5.configure(bg=cor_botao)
        self.bt_6.configure(bg=cor_botao)
        self.bt_7.configure(bg=cor_botao)
        self.bt_8.configure(bg=cor_botao)
        self.bt_9.configure(bg=cor_botao)
        
    def VerificaVitori(self):
        global vetor_de_Vitoria
        Posicao = []
        for i in range(3):
        
            for j in range(3):
            
                if vetor_de_Vitoria[i][j] == "":
                
                    Posicao.append([i,j])
        
        if Posicao == []:
            self.bt_1.configure(bg="blue")
            self.bt_2.configure(bg="blue")
            self.bt_3.configure(bg="blue")
            self.bt_4.configure(bg="blue")
            self.bt_5.configure(bg="blue")
            self.bt_6.configure(bg="blue") 
            self.bt_7.configure(bg="blue")
            self.bt_8.configure(bg="blue")
            self.bt_9.configure(bg="blue") 
            self.fimJogo()
            
        if (vetor_de_Vitoria[0] == [1,1,1] or vetor_de_Vitoria[1] == [1,1,1] or vetor_de_Vitoria[2] == [1,1,1]):
            print('vitoria O')
            if vetor_de_Vitoria[0] == [1,1,1]:
                self.bt_1.configure(bg="blue")
                self.bt_2.configure(bg="blue")
                self.bt_3.configure(bg="blue") 
            
            if vetor_de_Vitoria[1] == [1,1,1]:
                self.bt_4.configure(bg="blue")
                self.bt_5.configure(bg="blue")
                self.bt_6.configure(bg="blue") 
            
            if vetor_de_Vitoria[2] == [1,1,1]:
                self.bt_7.configure(bg="blue")
                self.bt_8.configure(bg="blue")
                self.bt_9.configure(bg="blue") 
            self.fimJogo()
             
        if vetor_de_Vitoria[0][0]==1 and vetor_de_Vitoria[1][0]==1 and vetor_de_Vitoria[2][0]==1:
            print('vitoria O')
            self.bt_1.configure(bg="blue")
            self.bt_4.configure(bg="blue")
            self.bt_7.configure(bg="blue") 
            self.fimJogo()
        if vetor_de_Vitoria[0][1]==1 and vetor_de_Vitoria[1][1]==1 and vetor_de_Vitoria[2][1]==1:
            print('vitoria O')
            self.bt_2.configure(bg="blue")
            self.bt_5.configure(bg="blue")
            self.bt_8.configure(bg="blue") 
            self.fimJogo()
        if vetor_de_Vitoria[0][2]==1 and vetor_de_Vitoria[1][2]==1 and vetor_de_Vitoria[2][2]==1:
            print('vitoria O')
            self.bt_3.configure(bg="blue")
            self.bt_6.configure(bg="blue")
            self.bt_9.configure(bg="blue") 
            self.fimJogo()
        if vetor_de_Vitoria[0][0]==1 and vetor_de_Vitoria[1][1]==1 and vetor_de_Vitoria[2][2]==1:
            print('vitoria O')
            self.bt_1.configure(bg="blue")
            self.bt_5.configure(bg="blue")
            self.bt_9.configure(bg="blue") 
            self.fimJogo()
        if vetor_de_Vitoria[0][2]==1 and vetor_de_Vitoria[1][1]==1 and vetor_de_Vitoria[2][0]==1:
            print('vitoria O')
            self.bt_3.configure(bg="blue")
            self.bt_5.configure(bg="blue")
            self.bt_7.configure(bg="blue") 
            self.fimJogo()
            
         
            
            
            
            
            
        if (vetor_de_Vitoria[0] == [0,0,0] or vetor_de_Vitoria[1] == [0,0,0] or vetor_de_Vitoria[2] == [0,0,0]):
            print('vitoria X')
            if vetor_de_Vitoria[0] == [0,0,0]:
                self.bt_1.configure(bg="blue")
                self.bt_2.configure(bg="blue")
                self.bt_3.configure(bg="blue") 
            
            if vetor_de_Vitoria[1] == [0,0,0]:
                self.bt_4.configure(bg="blue")
                self.bt_5.configure(bg="blue")
                self.bt_6.configure(bg="blue") 
            
            if vetor_de_Vitoria[2] == [0,0,0]:
                self.bt_7.configure(bg="blue")
                self.bt_8.configure(bg="blue")
                self.bt_9.configure(bg="blue")
            self.fimJogo() 
     
        if vetor_de_Vitoria[0][0]==0 and vetor_de_Vitoria[1][0]==0 and vetor_de_Vitoria[2][0]==0:
            print('vitoria X')
            self.bt_1.configure(bg="blue")
            self.bt_4.configure(bg="blue")
            self.bt_7.configure(bg="blue") 
            self.fimJogo()
        if vetor_de_Vitoria[0][1]==0 and vetor_de_Vitoria[1][1]==0 and vetor_de_Vitoria[2][1]==0:
            print('vitoria X')
            self.bt_2.configure(bg="blue")
            self.bt_5.configure(bg="blue")
            self.bt_8.configure(bg="blue") 
            self.fimJogo()
        if vetor_de_Vitoria[0][2]==0 and vetor_de_Vitoria[1][2]==0 and vetor_de_Vitoria[2][2]==0:
           print('vitoria X')
           self.bt_3.configure(bg="blue")
           self.bt_6.configure(bg="blue")
           self.bt_9.configure(bg="blue") 
           self.fimJogo()
        if vetor_de_Vitoria[0][0]==0 and vetor_de_Vitoria[1][1]==0 and vetor_de_Vitoria[2][2]==0:
           print('vitoria X')
           self.bt_1.configure(bg="blue")
           self.bt_5.configure(bg="blue")
           self.bt_9.configure(bg="blue") 
           self.fimJogo()
        if vetor_de_Vitoria[0][2]==0 and vetor_de_Vitoria[1][1]==0 and vetor_de_Vitoria[2][0]==0:
            print('vitoria X')
            self.bt_3.configure(bg="blue")
            self.bt_5.configure(bg="blue")
            self.bt_7.configure(bg="blue") 
            self.fimJogo()
            
            
    def mudaBotao(self,bt):
    
        global vator_botoes
        global vetor_de_Vitoria
        if (bt == 'bt_1' and vator_botoes[0][0] == ''):
            vator_botoes[0][0] = 'bt_1'
            vetor_de_Vitoria[0][0] = jogador_estado
            if jogador_estado==0:
                self.bt_1["text"] = 'X'
            else:
                self.bt_1["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        if (bt == 'bt_2' and vator_botoes[0][1] == ''):
            vator_botoes[0][1] = 'bt_2'
            vetor_de_Vitoria[0][1] = jogador_estado
            if jogador_estado==0:
                self.bt_2["text"] = 'X'
            else:
                self.bt_2["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        if (bt == 'bt_3' and vator_botoes[0][2] == ''):
            vator_botoes[0][2] = 'bt_3'
            vetor_de_Vitoria[0][2] = jogador_estado
            if jogador_estado==0:
                self.bt_3["text"] = 'X'
            else:
                self.bt_3["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        if (bt == 'bt_4' and vator_botoes[1][0] == ''):
            vator_botoes[1][0] = 'bt_4'
            vetor_de_Vitoria[1][0] = jogador_estado
            if jogador_estado==0:
                self.bt_4["text"] = 'X'
            else:
                self.bt_4["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        if (bt == 'bt_5' and vator_botoes[1][1] == ''):
            vator_botoes[1][1] = 'bt_5'
            vetor_de_Vitoria[1][1] = jogador_estado
            if jogador_estado==0:
                self.bt_5["text"] = 'X'
            else:
                self.bt_5["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        if (bt == 'bt_6' and vator_botoes[1][2] == ''):
            vator_botoes[1][2] = 'bt_6'
            vetor_de_Vitoria[1][2] = jogador_estado
            if jogador_estado==0:
                self.bt_6["text"] = 'X'
            else:
                self.bt_6["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        if (bt == 'bt_7' and vator_botoes[2][0] == ''):
            vator_botoes[2][0] = 'bt_7'
            vetor_de_Vitoria[2][0] = jogador_estado
            if jogador_estado==0:
                self.bt_7["text"] = 'X'
            else:
                self.bt_7["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        if (bt == 'bt_8' and vator_botoes[2][1] == ''):
            vator_botoes[2][1] = 'bt_8'
            vetor_de_Vitoria[2][1] = jogador_estado
            if jogador_estado==0:
                self.bt_8["text"] = 'X'
            else:
                self.bt_8["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        if (bt == 'bt_9' and vator_botoes[2][2] == ''):
            vator_botoes[2][2] = 'bt_9'
            vetor_de_Vitoria[2][2] = jogador_estado
            if jogador_estado==0:
                self.bt_9["text"] = 'X'
            else:
                self.bt_9["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        print(vetor_de_Vitoria)
        self.VerificaVitori() 
        
    
Jogo()


