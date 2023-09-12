
'''
class Funcionarios:
    
    nome = 'Elena'
    sobrenome = 'Cabral'

usuario1 = Funcionarios()

print(usuario1.nome)
print(usuario1.sobrenome)
...

#modulo

from datetime import datetime


# criar a classe
class Funcionarios:
    def __init__( self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano
        _nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome 
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)   
        return self.ano_nascimento
        

# criar objeto
usuario1=Funcionarios('Elena','Cabral', 2009)
usuario2=Funcionarios('Lucia','Lima',2005)

#print(usuario1.nome, usuario1.sobrenome)
#print(usuario2.nome, usuario2.sobrenome)
#print(usuario1.nome_completo())
print(Funcionarios.idade_funcionario(usuario1))
'''
#criar paramentros#################
#usuario1,nome = 'Elena'
#usuario1.sobrenome ='Cabral'
#usuario1.data_nascimento = '12/01/2009'

#usuario2,nome = 'Lucia'
#usuario2.sobrenome ='Lima'
#usuario2.data_nascimento = '12/01/2023'

#print
#print(usuario1.nome)
#print(usuario2.nome)



class Computador:

   def __init__(self, marca, memoria_ram, placa_de_video):
       self.marca  = marca
       self.memoria_ram = memoria_ram
       self.placa_de_video = placa_de_video

   def ExibirInformacoes(self):
       print(self.marca, self.memoria_ram, self.placa_de_video)   

   def Desligar(self):
       print ('estou desligando')  


# criar objeto

computador1 = Computador('Asus', '16gb', 'Samsung')
computador1.ExibirInformacoes()
computador1.Desligar() 


class Automoveis:

    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
    def ExibirInformacoes(self):
        print(self.marca, self.ano)    

    def valor(self):
        print('R$25000')   

locadora1 = Automoveis('Celta', 'ano 2000') 
locadora1.ExibirInformacoes()
locadora1.valor()  


class Carro:
    def __init__(self, velMax, ligado, cor):
        self.velMax = velMax
        self.ligado = ligado
        self.cor = cor

    def Mostrar(self):
        print('Velocidade maxima:' + str(self.velMax))
        print('cor ........:' + self.cor)
        estado = 'sim' if self.ligado else 'n'
        print('ligado..........:' + estado)
        print('.....................')

    def ligar(self):
        self.ligado=True
     
    def desligar(self):
        self.ligado=False

c1 = Carro(200, False,'preto')   
c2 = Carro(120,False,'branco')
c3 = Carro(300,False,'vermelho') 

c1.ligar()

c1.Mostrar()
c2.Mostrar()
c3.Mostrar()        
        



