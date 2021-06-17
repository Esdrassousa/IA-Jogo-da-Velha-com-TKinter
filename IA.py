
def movimentoIa(self,vetor_de_Vitoria1,jogador_estado):
    
    lance = posicoesBranco(vetor_de_Vitoria1)
    melhor_valor = None
    melhor_movimento = None
    for lance_joga in lance:
        
        # jogador_estado = 1
        vetor_de_Vitoria1[lance_joga[0]][lance_joga[1]] = jogador_estado
        
        self.valor = minimax(vetor_de_Vitoria1, jogador_estado)
        vetor_de_Vitoria1[lance_joga[0]][lance_joga[1]] = ""
        
    
    
        if(melhor_valor is None):
            melhor_valor = self.valor
            melhor_movimento = lance_joga
        elif(jogador_estado == 1):
            if(self.valor > melhor_valor):
                melhor_valor = self.valor 
                melhor_movimento = lance_joga
        elif(jogador_estado == 0):
            if(self.valor < melhor_valor):
                melhor_valor = self.valor
                melhor_movimento = lance_joga

    
    
    a = melhor_movimento[0]
    b= melhor_movimento[1]
    return a,b
    
    # print(lance)
def posicoesBranco(vetor_de_Vitoria1):
    
    Posi = []
    
    for i in range(3):
        
        for j in range(3):
            
            if vetor_de_Vitoria1[i][j] == "":
                
                Posi.append([i,j])
                print(Posi)
        
        
    return Posi 
        
def minimax(vetor_de_Vitoria1, jogador_estado):
    verifica_vitoria = VerificaVitoria(vetor_de_Vitoria1)
    
    if verifica_vitoria == 'empate':
            print('aqui deu impate')
            pontuacao = 1
            return pontuacao
            
    elif verifica_vitoria == 'vitoria_0':
            print('aqui deu 0')
            pontuacao = 2
            return pontuacao
            
    elif verifica_vitoria == 'vitoria_X':
            print('aqui deu X')
            pontuacao = 0
            return pontuacao 
    
    
   
   
    # jogador_estado = jogador(jogador_estado)
    # 
    
    lance = posicoesBranco(vetor_de_Vitoria1)
    melhor_valor = None
    jogador_estado = jogador(jogador_estado)
    for lance_joga in lance:
        vetor_de_Vitoria1[lance_joga[0]][lance_joga[1]] = jogador_estado
        
        valor = minimax(vetor_de_Vitoria1, jogador_estado)
        vetor_de_Vitoria1[lance_joga[0]][lance_joga[1]] = ""
        
        
        if(melhor_valor is None):
            melhor_valor = valor
        elif(jogador_estado == 1):
            if(valor > melhor_valor):
                melhor_valor = valor
        elif(jogador_estado == 0):
            if(valor < melhor_valor):
                melhor_valor = valor

    return melhor_valor
    
def jogador(jogador_estado):
        # global jogador_estado
        
        if jogador_estado == 0:
            
            jogador_estado = 1
        
        else:
            jogador_estado = 0
        
        print(jogador_estado)   
        
        return jogador_estado


def VerificaVitoria(vetor_de_Vitoria1):
        vetor_situacao =None
        Posicao = []
        print('o vetor de0 vitoria é ' ,vetor_de_Vitoria1)
        for i in range(3):
        
            for j in range(3):
            
                if vetor_de_Vitoria1[i][j] == "":
                
                    Posicao.append([i,j])
        
        if Posicao == []:
            print('empate')
            vetor_situacao = 'empate'
            
        
        if (vetor_de_Vitoria1[0] == [1,1,1] or vetor_de_Vitoria1[1] == [1,1,1] or vetor_de_Vitoria1[2] == [1,1,1]):
            print('vitoria O')
            vetor_situacao = 'vitoria_0'
            
            
             
        if vetor_de_Vitoria1[0][0]==1 and vetor_de_Vitoria1[1][0]==1 and vetor_de_Vitoria1[2][0]==1:
            print('vitoria O')
            vetor_situacao = 'vitoria_0'
           
        if vetor_de_Vitoria1[0][1]==1 and vetor_de_Vitoria1[1][1]==1 and vetor_de_Vitoria1[2][1]==1:
            print('vitoria O')
            vetor_situacao = 'vitoria_0'
        if vetor_de_Vitoria1[0][2]==1 and vetor_de_Vitoria1[1][2]==1 and vetor_de_Vitoria1[2][2]==1:
            print('vitoria O')
            vetor_situacao = 'vitoria_0'
        if vetor_de_Vitoria1[0][0]==1 and vetor_de_Vitoria1[1][1]==1 and vetor_de_Vitoria1[2][2]==1:
            print('vitoria O')
            vetor_situacao = 'vitoria_0'
        if vetor_de_Vitoria1[0][2]==1 and vetor_de_Vitoria1[1][1]==1 and vetor_de_Vitoria1[2][0]==1:
            print('vitoria O')
            vetor_situacao = 'vitoria_0'
            
         
            
            
            
            
            
        if (vetor_de_Vitoria1[0] == [0,0,0] or vetor_de_Vitoria1[1] == [0,0,0] or vetor_de_Vitoria1[2] == [0,0,0]):
            print('vitoria X')
            vetor_situacao = 'vitoria_X'
     
        if vetor_de_Vitoria1[0][0]==0 and vetor_de_Vitoria1[1][0]==0 and vetor_de_Vitoria1[2][0]==0:
            print('vitoria X')
            vetor_situacao = 'vitoria_X'
        if vetor_de_Vitoria1[0][1]==0 and vetor_de_Vitoria1[1][1]==0 and vetor_de_Vitoria1[2][1]==0:
            print('vitoria X')
            vetor_situacao = 'vitoria_X'
        if vetor_de_Vitoria1[0][2]==0 and vetor_de_Vitoria1[1][2]==0 and vetor_de_Vitoria1[2][2]==0:
           print('vitoria X')
           vetor_situacao = 'vitoria_X'
        if vetor_de_Vitoria1[0][0]==0 and vetor_de_Vitoria1[1][1]==0 and vetor_de_Vitoria1[2][2]==0:
           print('vitoria X')
           vetor_situacao = 'vitoria_X'
        if vetor_de_Vitoria1[0][2]==0 and vetor_de_Vitoria1[1][1]==0 and vetor_de_Vitoria1[2][0]==0:
            print('vitoria X')
            vetor_situacao = 'vitoria_X'
        return(vetor_situacao)