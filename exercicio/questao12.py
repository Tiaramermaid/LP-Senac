# Soma de 1 a N
# Peça ao usuario um numero N e exiba a soma de todos os numeros de 1 ate N

i = 0
soma = 0
# 1. solicitar o numero
numero = int(input('digite um numero para soma-lo: '))
# 2. contar ate o numero
for i in range (1, numero, 1):
# 3. somar cada numero ate o numero inserido
    soma = soma + i
# 4. exibir resposta
    print(f'{soma}')