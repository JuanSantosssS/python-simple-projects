import random

nomes = []

for i in range (10):
    nome = input(f'Digite o nome  do jogador {i + 1}: ')
    nomes.append(nome)

random.shuffle(nomes)


tamanho_times = len(nomes) //2

#Operadores de fatiamento

time1 = nomes [:tamanho_times]
time2 = nomes [tamanho_times:]

print ('Time 1:', time1)
print ('Time 2:', time2)