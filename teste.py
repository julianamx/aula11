import moeda
from moeda import diminuir
import math

#p = float(input('digite o Preço: R$'))
#print(f'a metade de {p} e {moeda.metade(p)}')


p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')



