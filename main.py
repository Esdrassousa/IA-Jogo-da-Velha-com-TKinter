from tkinter import *
import tkinter as tk
import  IA
  
jogador_estado = 0

vetorBotao = [
    ["","",""],
    ["","",""],
    ["","",""]
    ]
vetor_de_Vitoria = [
    ["","",""],
    ["","",""],
    ["","",""]
    ]



mycolor = '#%02x%02x%02x' % (64, 204, 208)

class janelas():        
        
    def __init__(self): 
        janela = tk.Tk()
        janela.geometry("420x450+200+200")
        
        self.bt_1 = Button(janela,  width = 15 , height = 10, text="", bg = mycolor,command=lambda: self.mudaBotao('bt_1'))
        self.bt_1.place(x=0,y=0)
        
        self.bt_2 = Button(janela,  width = 15 , height = 10, text="" ,bg = mycolor, command=lambda: self.mudaBotao('bt_2'))
        self.bt_2.place(x=140,y=0)
        self.bt_3 = Button(janela,  width = 15 , height = 10, text="" , bg = mycolor,command=lambda: self.mudaBotao('bt_3'))
        self.bt_3.place(x=280,y=0)
        
        self.bt_4 = Button(janela,  width = 15 , height = 10, text="" ,bg = mycolor, command=lambda: self.mudaBotao('bt_4'))
        self.bt_4.place(x=0,y=130)
        self.bt_5 = Button(janela,  width = 15 , height = 10, text="" , bg = mycolor,command=lambda: self.mudaBotao('bt_5'))
        self.bt_5.place(x=140,y=130)
        self.bt_6 = Button(janela,  width = 15 , height = 10, text="" ,bg = mycolor, command=lambda: self.mudaBotao('bt_6'))
        self.bt_6.place(x=280,y=130)
        
        
        self.bt_7 = Button(janela,  width = 15 , height = 10, text="" , bg = mycolor, command=lambda: self.mudaBotao('bt_7'))
        self.bt_7.place(x=0,y=260)
        self.bt_8 = Button(janela,  width = 15 , height = 10, text="" , bg = mycolor,command=lambda: self.mudaBotao('bt_8'))
        self.bt_8.place(x=140,y=260)
        self.bt_9 = Button(janela,  width = 15 , height = 10, text="" , bg = mycolor,command=lambda: self.mudaBotao('bt_9'))
        self.bt_9.place(x=280,y=260)
        
        self.bt_reinicia = Button(janela, width=15 , text="Reinicia" , bg = 'red',command=lambda: self.zeraJogo())
        self.bt_reinicia.place(x=140,y=400)
        
        janela.title("Jogo da Velha")
        janela.mainloop()
        
    def jogador(self,bt):
        global jogador_estado
        
        if jogador_estado == 0:
            
            jogador_estado = 1
        
        else:
            jogador_estado = 0
        
        print(jogador_estado)
        
        
        
    def lanceIa(self):
       global vetor_de_Vitoria
       vetor_de_Vitoria2 = vetor_de_Vitoria
       vetor_de_Vitoria1=vetor_de_Vitoria
       print("vetor de vitori: ",vetor_de_Vitoria2)
       [a,b] = IA.movimentoIa(self,vetor_de_Vitoria, jogador_estado)
       # a = melhor[0]
       # b =melhor[1]
       print("veto1r de vitori: ",vetor_de_Vitoria2)
       print('return a e b', a,b)
       print(vetor_de_Vitoria)
       if a ==0 and b==0:
           vetorBotao[0][0] = 'bt_1'
           vetor_de_Vitoria[0][0] = jogador_estado
           if jogador_estado==0:
                self.bt_1["text"] = 'X'
           else:
                self.bt_1["text"] = 'O'
           self.jogador('bt')
           
       if a ==0 and b==1:
           vetorBotao[0][1] = 'bt_2'
           vetor_de_Vitoria[0][1] = jogador_estado
           if jogador_estado==0:
                self.bt_2["text"] = 'X'
           else:
                self.bt_2["text"] = 'O'
           self.jogador('bt')
       if a ==0 and b==2:
           vetorBotao[0][2] = 'bt_3'
           vetor_de_Vitoria[0][2] = jogador_estado
           if jogador_estado==0:
                self.bt_3["text"] = 'X'
           else:
                self.bt_3["text"] = 'O'
           self.jogador('bt')
       if a ==1 and b==0:
           vetorBotao[1][0] = 'bt_4'
           vetor_de_Vitoria[1][0] = jogador_estado
           if jogador_estado==0:
                self.bt_4["text"] = 'X'
           else:
                self.bt_4["text"] = 'O'
           self.jogador('bt')
       if a ==1 and b==1:
           vetorBotao[1][1] = 'bt_5'
           vetor_de_Vitoria[1][1] = jogador_estado
           if jogador_estado==0:
                self.bt_5["text"] = 'X'
           else:
                self.bt_5["text"] = 'O'
           self.jogador('bt')
       
       if a ==1 and b==2:
           vetorBotao[1][2] = 'bt_6'
           vetor_de_Vitoria[1][2] = jogador_estado
           if jogador_estado==0:
                self.bt_6["text"] = 'X'
           else:
                self.bt_6["text"] = 'O'
           self.jogador('bt')
       if a ==2 and b==0:
           vetorBotao[2][0] = 'bt_7'
           vetor_de_Vitoria[2][0] = jogador_estado
           if jogador_estado==0:
                self.bt_7["text"] = 'X'
           else:
                self.bt_7["text"] = 'O'
           self.jogador('bt')
       if a ==2 and b==1:
           vetorBotao[2][1] = 'bt_8'
           vetor_de_Vitoria[2][1] = jogador_estado
           if jogador_estado==0:
                self.bt_8["text"] = 'X'
           else:
                self.bt_8["text"] = 'O'
           self.jogador('bt')
       if a ==2 and b==2:
           vetorBotao[2][2] = 'bt_9'
           vetor_de_Vitoria[2][2] = jogador_estado
           if jogador_estado==0:
                self.bt_9["text"] = 'X'
           else:
                self.bt_9["text"] = 'O'
           self.jogador('bt')
           
    
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
        global vetorBotao
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
        vetorBotao = [
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
        
        self.bt_1.configure(bg=mycolor)
        self.bt_2.configure(bg=mycolor)
        self.bt_3.configure(bg=mycolor)
        self.bt_4.configure(bg=mycolor)
        self.bt_5.configure(bg=mycolor)
        self.bt_6.configure(bg=mycolor)
        self.bt_7.configure(bg=mycolor)
        self.bt_8.configure(bg=mycolor)
        self.bt_9.configure(bg=mycolor)
    def VerificaVitori(self):
        global vetor_de_Vitoria
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
    
        global vetorBotao
        global vetor_de_Vitoria
        if (bt == 'bt_1' and vetorBotao[0][0] == ''):
            vetorBotao[0][0] = 'bt_1'
            vetor_de_Vitoria[0][0] = jogador_estado
            if jogador_estado==0:
                self.bt_1["text"] = 'X'
            else:
                self.bt_1["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        if (bt == 'bt_2' and vetorBotao[0][1] == ''):
            vetorBotao[0][1] = 'bt_2'
            vetor_de_Vitoria[0][1] = jogador_estado
            if jogador_estado==0:
                self.bt_2["text"] = 'X'
            else:
                self.bt_2["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        if (bt == 'bt_3' and vetorBotao[0][2] == ''):
            vetorBotao[0][2] = 'bt_3'
            vetor_de_Vitoria[0][2] = jogador_estado
            if jogador_estado==0:
                self.bt_3["text"] = 'X'
            else:
                self.bt_3["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        if (bt == 'bt_4' and vetorBotao[1][0] == ''):
            vetorBotao[1][0] = 'bt_4'
            vetor_de_Vitoria[1][0] = jogador_estado
            if jogador_estado==0:
                self.bt_4["text"] = 'X'
            else:
                self.bt_4["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        if (bt == 'bt_5' and vetorBotao[1][1] == ''):
            vetorBotao[1][1] = 'bt_5'
            vetor_de_Vitoria[1][1] = jogador_estado
            if jogador_estado==0:
                self.bt_5["text"] = 'X'
            else:
                self.bt_5["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        if (bt == 'bt_6' and vetorBotao[1][2] == ''):
            vetorBotao[1][2] = 'bt_6'
            vetor_de_Vitoria[1][2] = jogador_estado
            if jogador_estado==0:
                self.bt_6["text"] = 'X'
            else:
                self.bt_6["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        if (bt == 'bt_7' and vetorBotao[2][0] == ''):
            vetorBotao[2][0] = 'bt_7'
            vetor_de_Vitoria[2][0] = jogador_estado
            if jogador_estado==0:
                self.bt_7["text"] = 'X'
            else:
                self.bt_7["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        if (bt == 'bt_8' and vetorBotao[2][1] == ''):
            vetorBotao[2][1] = 'bt_8'
            vetor_de_Vitoria[2][1] = jogador_estado
            if jogador_estado==0:
                self.bt_8["text"] = 'X'
            else:
                self.bt_8["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        if (bt == 'bt_9' and vetorBotao[2][2] == ''):
            vetorBotao[2][2] = 'bt_9'
            vetor_de_Vitoria[2][2] = jogador_estado
            if jogador_estado==0:
                self.bt_9["text"] = 'X'
            else:
                self.bt_9["text"] = 'O'
            self.jogador(bt)
            self.lanceIa()
        print(vetor_de_Vitoria)
        self.VerificaVitori() 
        
    

janelas()
