# Para este desafio, crie duas funções. A primeira função deve aceitar um número
# e retornar o dobro desse número. A segunda função deve aceitar um número e retornar
# o quadrado desse número. Em seguida, chame a primeira função dentro da segunda para retornar
# o quadrado do dobro de um número.


n1= int(input('digite um numero:'))
funcao1 = n1*2
print(funcao1)
n2= int(input('digite outro numero:'))
funcao2 = n2 ** 2
print(funcao2)
funcao3 = funcao1**2
print(funcao3)

# criar um programa que calcule  a quantidade de tinta necessária para pintar uma parede.
# O usuário deverá fornecer as seguintes informações: Rendimento, altura e largura.
# O programa deve mostrar na tela a mensagem 'você necessita de x latas de tintas'
#==============================================


altura = float(input('Digite a alturada parede: '))

largura = float(input('Digite a largura da parede: '))

area = altura * largura

redimento = area / 2

print(f'A área a ser pintada é de {area:.2f} m² e serão necessários {redimento} latas de tinta para pinta-la.')