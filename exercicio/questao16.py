# Fatorial de um numero 
# receba um numero inteiro positivo e exiba 
# seu fatorial (ex.: 5! = 5 * 4*3*2*1 = 120).

# 1. receber um numero 
numero = int(input('digite um numero: '))
# 2. contagem regressiva multiplicando:
if numero < 0: 
    print ('numero nao valido')
# 3. exibir resultado
else: 
    resultado = 1
    while numero >= 1:
        resultado *= numero
        numero-= 1

print (f'o fatorial é: {resultado}')
