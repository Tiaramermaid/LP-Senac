# Tabuada de um numero
# peça um numero e exiba a tabuada dele de 1 a 10

# 1. contador de 1 a 10

# 2. pedir o numero
numero = int(input('digite um numero para exibir sua tabuada: '))
# 3. somar o numero + contador
for cont in range (1, 11, 1):
    soma = cont + numero
# 4. exibir o contador + o numero solicitado = resposta 
    print(f'{cont} + {numero} = {soma}')